import platform

def detect_os():
    system = platform.system()
    if system == 'Windows':
        return "Windows OS detected"
    elif system == 'Linux':
        distribution = platform.linux_distribution()
        if distribution[0] == 'Ubuntu':
            return "Ubuntu OS detected"
        else:
            return "Linux OS detected"
    elif system == 'Darwin':
        return "Mac OS detected"
    else:
        return "Unknown OS detected"

# Call the function to detect the OS and retrieve the result
os_string = detect_os()
print(os_string)