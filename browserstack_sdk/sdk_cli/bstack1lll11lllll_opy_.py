# coding: UTF-8
import sys
bstack1l1lll_opy_ = sys.version_info [0] == 2
bstack1l1l1ll_opy_ = 2048
bstack1lllllll_opy_ = 7
def bstack1ll1l_opy_ (bstack1ll1l1l_opy_):
    global bstack11ll1l_opy_
    bstack111l111_opy_ = ord (bstack1ll1l1l_opy_ [-1])
    bstack1l111ll_opy_ = bstack1ll1l1l_opy_ [:-1]
    bstack1ll_opy_ = bstack111l111_opy_ % len (bstack1l111ll_opy_)
    bstack111l_opy_ = bstack1l111ll_opy_ [:bstack1ll_opy_] + bstack1l111ll_opy_ [bstack1ll_opy_:]
    if bstack1l1lll_opy_:
        bstack1lll1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack1l1l1ll_opy_ - (bstack1111lll_opy_ + bstack111l111_opy_) % bstack1lllllll_opy_) for bstack1111lll_opy_, char in enumerate (bstack111l_opy_)])
    else:
        bstack1lll1ll_opy_ = str () .join ([chr (ord (char) - bstack1l1l1ll_opy_ - (bstack1111lll_opy_ + bstack111l111_opy_) % bstack1lllllll_opy_) for bstack1111lll_opy_, char in enumerate (bstack111l_opy_)])
    return eval (bstack1lll1ll_opy_)
import threading
import queue
from typing import Callable, Union
class bstack1lll1l11111_opy_:
    timeout: int
    bstack1l1ll1lll11_opy_: Union[None, Callable]
    bstack1l1ll1lll1l_opy_: Union[None, Callable]
    def __init__(self, timeout=1, bstack1l1ll1ll1l1_opy_=1, bstack1l1ll1lll11_opy_=None, bstack1l1ll1lll1l_opy_=None):
        self.timeout = timeout
        self.bstack1l1ll1ll1l1_opy_ = bstack1l1ll1ll1l1_opy_
        self.bstack1l1ll1lll11_opy_ = bstack1l1ll1lll11_opy_
        self.bstack1l1ll1lll1l_opy_ = bstack1l1ll1lll1l_opy_
        self.queue = queue.Queue()
        self.bstack1l1ll1ll1ll_opy_ = threading.Event()
        self.threads = []
    def enqueue(self, job: Callable):
        if not callable(job):
            raise ValueError(bstack1ll1l_opy_ (u"ࠧ࡯࡮ࡷࡣ࡯࡭ࡩࠦࡪࡰࡤ࠽ࠤࠧዀ") + type(job))
        self.queue.put(job)
    def start(self):
        if self.threads:
            return
        self.threads = [threading.Thread(target=self.worker, daemon=True) for _ in range(self.bstack1l1ll1ll1l1_opy_)]
        for thread in self.threads:
            thread.start()
    def stop(self):
        if not self.threads:
            return
        if not self.queue.empty():
            self.queue.join()
        self.bstack1l1ll1ll1ll_opy_.set()
        for _ in self.threads:
            self.queue.put(None)
        for thread in self.threads:
            thread.join()
        self.threads.clear()
    def worker(self):
        while not self.bstack1l1ll1ll1ll_opy_.is_set():
            try:
                job = self.queue.get(block=True, timeout=self.timeout)
                if job is None:
                    break
                try:
                    job()
                except Exception as e:
                    if callable(self.bstack1l1ll1lll11_opy_):
                        self.bstack1l1ll1lll11_opy_(e, job)
                finally:
                    self.queue.task_done()
            except queue.Empty:
                pass
            except Exception as e:
                if callable(self.bstack1l1ll1lll1l_opy_):
                    self.bstack1l1ll1lll1l_opy_(e)