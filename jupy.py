from jupyter_client import KernelManager
from jupyter_client.blocking.client import BlockingKernelClient

# Start a new local Python kernel
km = KernelManager()
km.start_kernel()

# Get a client object from the kernel manager
kc = BlockingKernelClient(connection_file=km.connection_file)
kc.load_connection_file()
kc.start_channels()

# Define a function to process output messages
def output_callback(msg):
    if msg['msg_type'] == 'stream':
        print(msg['content']['text'])
    elif msg['msg_type'] == 'execute_result':
        print(f"Execution Result: {msg['content']['data']['text/plain']}")
    elif msg['msg_type'] == 'error':
        print(f"Error: {msg['content']['ename']}: {msg['content']['evalue']}")

# Execute the code interactively, providing the output_hook
kc.execute_interactive(
    code="print('Hello from execute_interactive!')\na = 1 + 2\nprint(f'The result is: {a}')",
    output_hook=output_callback,
    stop_on_error=True  # Optional: stop if an error occurs
)

kc.execute_interactive(
    code="print(f'The result is: {a}')",
    output_hook=output_callback,
    stop_on_error=True  # Optional: stop if an error occurs
)

# Shut down the kernel
km.shutdown_kernel()
