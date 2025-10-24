# coding: UTF-8
import sys
bstack1lllll1_opy_ = sys.version_info [0] == 2
bstack11lll1l_opy_ = 2048
bstack1lll1l_opy_ = 7
def bstack11l11l1_opy_ (bstack111l1ll_opy_):
    global bstack1ll1l_opy_
    bstack1l1l1ll_opy_ = ord (bstack111l1ll_opy_ [-1])
    bstack1l11l_opy_ = bstack111l1ll_opy_ [:-1]
    bstack1lllll1l_opy_ = bstack1l1l1ll_opy_ % len (bstack1l11l_opy_)
    bstack11ll1l1_opy_ = bstack1l11l_opy_ [:bstack1lllll1l_opy_] + bstack1l11l_opy_ [bstack1lllll1l_opy_:]
    if bstack1lllll1_opy_:
        bstack1lll_opy_ = unicode () .join ([unichr (ord (char) - bstack11lll1l_opy_ - (bstack1l1ll11_opy_ + bstack1l1l1ll_opy_) % bstack1lll1l_opy_) for bstack1l1ll11_opy_, char in enumerate (bstack11ll1l1_opy_)])
    else:
        bstack1lll_opy_ = str () .join ([chr (ord (char) - bstack11lll1l_opy_ - (bstack1l1ll11_opy_ + bstack1l1l1ll_opy_) % bstack1lll1l_opy_) for bstack1l1ll11_opy_, char in enumerate (bstack11ll1l1_opy_)])
    return eval (bstack1lll_opy_)
import threading
import queue
from typing import Callable, Union
class bstack1lll11l1lll_opy_:
    timeout: int
    bstack1l1ll1l1l1l_opy_: Union[None, Callable]
    bstack1l1ll1l1l11_opy_: Union[None, Callable]
    def __init__(self, timeout=1, bstack1l1ll1l11l1_opy_=1, bstack1l1ll1l1l1l_opy_=None, bstack1l1ll1l1l11_opy_=None):
        self.timeout = timeout
        self.bstack1l1ll1l11l1_opy_ = bstack1l1ll1l11l1_opy_
        self.bstack1l1ll1l1l1l_opy_ = bstack1l1ll1l1l1l_opy_
        self.bstack1l1ll1l1l11_opy_ = bstack1l1ll1l1l11_opy_
        self.queue = queue.Queue()
        self.bstack1l1ll1l11ll_opy_ = threading.Event()
        self.threads = []
    def enqueue(self, job: Callable):
        if not callable(job):
            raise ValueError(bstack11l11l1_opy_ (u"ࠦ࡮ࡴࡶࡢ࡮࡬ࡨࠥࡰ࡯ࡣ࠼ࠣࠦዛ") + type(job))
        self.queue.put(job)
    def start(self):
        if self.threads:
            return
        self.threads = [threading.Thread(target=self.worker, daemon=True) for _ in range(self.bstack1l1ll1l11l1_opy_)]
        for thread in self.threads:
            thread.start()
    def stop(self):
        if not self.threads:
            return
        if not self.queue.empty():
            self.queue.join()
        self.bstack1l1ll1l11ll_opy_.set()
        for _ in self.threads:
            self.queue.put(None)
        for thread in self.threads:
            thread.join()
        self.threads.clear()
    def worker(self):
        while not self.bstack1l1ll1l11ll_opy_.is_set():
            try:
                job = self.queue.get(block=True, timeout=self.timeout)
                if job is None:
                    break
                try:
                    job()
                except Exception as e:
                    if callable(self.bstack1l1ll1l1l1l_opy_):
                        self.bstack1l1ll1l1l1l_opy_(e, job)
                finally:
                    self.queue.task_done()
            except queue.Empty:
                pass
            except Exception as e:
                if callable(self.bstack1l1ll1l1l11_opy_):
                    self.bstack1l1ll1l1l11_opy_(e)