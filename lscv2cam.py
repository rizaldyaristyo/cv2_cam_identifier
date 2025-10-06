import pyudev # pyright: ignore[reportMissingImports]
import subprocess
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

def list_physical_cameras():
    cameras = {}
    def is_capture_device(devnode: str) -> bool:
        try:
            out = subprocess.check_output(
                ["v4l2-ctl", "-d", devnode, "--all"],
                text=True,
                stderr=subprocess.DEVNULL,
            )
            return "Video Capture" in out
        except Exception:
            return False
    def list_physical_cameras():
        context = pyudev.Context()
        results = []
        seen_ids = set()
        for device in sorted(context.list_devices(subsystem='video4linux'),
                            key=lambda d: d.device_node):
            devnode = device.device_node
            parent = device.find_parent('usb', 'usb_device')
            if not parent:
                continue
            bus = parent.attributes.get('busnum').decode()
            port = parent.attributes.get('devpath').decode()
            identifier = f"{port}-{bus}"
            if identifier not in seen_ids and is_capture_device(devnode):
                results.append((devnode, identifier))
                seen_ids.add(identifier)
            else:
                continue
        return results
    for idx, (devnode, ident) in enumerate(list_physical_cameras()):
        cameras.update({
            ident: devnode
        })
    
    return cameras

if __name__ == "__main__":
    print("Camera IDs:", list_physical_cameras())