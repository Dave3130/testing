# coding: UTF-8
import sys
bstack11l1ll_opy_ = sys.version_info [0] == 2
bstack1111ll1_opy_ = 2048
bstack11llll_opy_ = 7
def bstack11ll1ll_opy_ (bstack1111l11_opy_):
    global bstack1l111l1_opy_
    bstack1llll11_opy_ = ord (bstack1111l11_opy_ [-1])
    bstack1l1lll1_opy_ = bstack1111l11_opy_ [:-1]
    bstack11111l1_opy_ = bstack1llll11_opy_ % len (bstack1l1lll1_opy_)
    bstack1111l_opy_ = bstack1l1lll1_opy_ [:bstack11111l1_opy_] + bstack1l1lll1_opy_ [bstack11111l1_opy_:]
    if bstack11l1ll_opy_:
        bstack11l11_opy_ = unicode () .join ([unichr (ord (char) - bstack1111ll1_opy_ - (bstack1l_opy_ + bstack1llll11_opy_) % bstack11llll_opy_) for bstack1l_opy_, char in enumerate (bstack1111l_opy_)])
    else:
        bstack11l11_opy_ = str () .join ([chr (ord (char) - bstack1111ll1_opy_ - (bstack1l_opy_ + bstack1llll11_opy_) % bstack11llll_opy_) for bstack1l_opy_, char in enumerate (bstack1111l_opy_)])
    return eval (bstack11l11_opy_)
import threading
import queue
from typing import Callable, Union
class bstack1lll11l111l_opy_:
    timeout: int
    bstack1l1ll11l1ll_opy_: Union[None, Callable]
    bstack1l1ll11ll1l_opy_: Union[None, Callable]
    def __init__(self, timeout=1, bstack1l1ll11lll1_opy_=1, bstack1l1ll11l1ll_opy_=None, bstack1l1ll11ll1l_opy_=None):
        self.timeout = timeout
        self.bstack1l1ll11lll1_opy_ = bstack1l1ll11lll1_opy_
        self.bstack1l1ll11l1ll_opy_ = bstack1l1ll11l1ll_opy_
        self.bstack1l1ll11ll1l_opy_ = bstack1l1ll11ll1l_opy_
        self.queue = queue.Queue()
        self.bstack1l1ll11ll11_opy_ = threading.Event()
        self.threads = []
    def enqueue(self, job: Callable):
        if not callable(job):
            raise ValueError(bstack11ll1ll_opy_ (u"ࠢࡪࡰࡹࡥࡱ࡯ࡤࠡ࡬ࡲࡦ࠿ࠦࠢዺ") + type(job))
        self.queue.put(job)
    def start(self):
        if self.threads:
            return
        self.threads = [threading.Thread(target=self.worker, daemon=True) for _ in range(self.bstack1l1ll11lll1_opy_)]
        for thread in self.threads:
            thread.start()
    def stop(self):
        if not self.threads:
            return
        if not self.queue.empty():
            self.queue.join()
        self.bstack1l1ll11ll11_opy_.set()
        for _ in self.threads:
            self.queue.put(None)
        for thread in self.threads:
            thread.join()
        self.threads.clear()
    def worker(self):
        while not self.bstack1l1ll11ll11_opy_.is_set():
            try:
                job = self.queue.get(block=True, timeout=self.timeout)
                if job is None:
                    break
                try:
                    job()
                except Exception as e:
                    if callable(self.bstack1l1ll11l1ll_opy_):
                        self.bstack1l1ll11l1ll_opy_(e, job)
                finally:
                    self.queue.task_done()
            except queue.Empty:
                pass
            except Exception as e:
                if callable(self.bstack1l1ll11ll1l_opy_):
                    self.bstack1l1ll11ll1l_opy_(e)