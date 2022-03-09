import asyncio
import signal

from lifecyclemanager.i_runnable import IRunnable

class LifecycleManager:
    def __init__(self):
        self.loop = asyncio.new_event_loop()

    def run(self, task):
        self.loop.run_until_complete(task())

    def run_forever(self, runnable: IRunnable):
        try:
            for sig in ('SIGINT', 'SIGTERM'):
                self.loop.add_signal_handler(getattr(signal, sig), self.create_stop_callback(runnable))
        except NotImplementedError:
            print("Signal handler unavailable")

        try:
            self.loop.run_until_complete(runnable.run())
            self.loop.run_forever()
        finally:
            self.loop.close()

    async def stop(self):
        await asyncio.sleep(1)
        self.loop.stop()

    def create_stop_callback(self, runnable):
        def callback():
            asyncio.create_task(runnable.destruct())
            asyncio.create_task(self.stop())
        return callback

