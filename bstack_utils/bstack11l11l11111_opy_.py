# coding: UTF-8
import sys
bstack11_opy_ = sys.version_info [0] == 2
bstack1l111ll_opy_ = 2048
bstack11lll1l_opy_ = 7
def bstack1lll11l_opy_ (bstack11l11l_opy_):
    global bstack11l1l1_opy_
    bstack1l111_opy_ = ord (bstack11l11l_opy_ [-1])
    bstack1ll11l1_opy_ = bstack11l11l_opy_ [:-1]
    bstack1l_opy_ = bstack1l111_opy_ % len (bstack1ll11l1_opy_)
    bstack1l11ll1_opy_ = bstack1ll11l1_opy_ [:bstack1l_opy_] + bstack1ll11l1_opy_ [bstack1l_opy_:]
    if bstack11_opy_:
        bstack1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack1l111ll_opy_ - (bstack1l11ll_opy_ + bstack1l111_opy_) % bstack11lll1l_opy_) for bstack1l11ll_opy_, char in enumerate (bstack1l11ll1_opy_)])
    else:
        bstack1ll_opy_ = str () .join ([chr (ord (char) - bstack1l111ll_opy_ - (bstack1l11ll_opy_ + bstack1l111_opy_) % bstack11lll1l_opy_) for bstack1l11ll_opy_, char in enumerate (bstack1l11ll1_opy_)])
    return eval (bstack1ll_opy_)
import threading
import logging
logger = logging.getLogger(__name__)
bstack111l1lll11l_opy_ = 1000
bstack111l1llll1l_opy_ = 2
class bstack111l1lll1l1_opy_:
    def __init__(self, handler, bstack111l1llllll_opy_=bstack111l1lll11l_opy_, bstack111l1ll1ll1_opy_=bstack111l1llll1l_opy_):
        self.queue = []
        self.handler = handler
        self.bstack111l1llllll_opy_ = bstack111l1llllll_opy_
        self.bstack111l1ll1ll1_opy_ = bstack111l1ll1ll1_opy_
        self.lock = threading.Lock()
        self.timer = None
        self.bstack1l1ll1l1111_opy_ = None
    def start(self):
        if not (self.timer and self.timer.is_alive()):
            self.bstack111l1ll1lll_opy_()
    def bstack111l1ll1lll_opy_(self):
        self.bstack1l1ll1l1111_opy_ = threading.Event()
        def bstack111l1lllll1_opy_():
            self.bstack1l1ll1l1111_opy_.wait(self.bstack111l1ll1ll1_opy_)
            if not self.bstack1l1ll1l1111_opy_.is_set():
                self.bstack111l1llll11_opy_()
        self.timer = threading.Thread(target=bstack111l1lllll1_opy_, daemon=True)
        self.timer.start()
    def bstack111l1lll1ll_opy_(self):
        try:
            if self.bstack1l1ll1l1111_opy_ and not self.bstack1l1ll1l1111_opy_.is_set():
                self.bstack1l1ll1l1111_opy_.set()
            if self.timer and self.timer.is_alive() and self.timer != threading.current_thread():
                self.timer.join()
        except Exception as e:
            logger.debug(bstack1lll11l_opy_ (u"ࠪ࡟ࡸࡺ࡯ࡱࡡࡷ࡭ࡲ࡫ࡲ࡞ࠢࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲ࠿ࠦࠧ᯼") + (str(e) or bstack1lll11l_opy_ (u"ࠦࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡤࡱࡸࡰࡩࠦ࡮ࡰࡶࠣࡦࡪࠦࡣࡰࡰࡹࡩࡷࡺࡥࡥࠢࡷࡳࠥࡹࡴࡳ࡫ࡱ࡫ࠧ᯽")))
        finally:
            self.timer = None
    def bstack111l1lll111_opy_(self):
        if self.timer:
            self.bstack111l1lll1ll_opy_()
        self.bstack111l1ll1lll_opy_()
    def add(self, event):
        with self.lock:
            self.queue.append(event)
            if len(self.queue) >= self.bstack111l1llllll_opy_:
                threading.Thread(target=self.bstack111l1llll11_opy_).start()
    def bstack111l1llll11_opy_(self, source = bstack1lll11l_opy_ (u"ࠬ࠭᯾")):
        with self.lock:
            if not self.queue:
                self.bstack111l1lll111_opy_()
                return
            data = self.queue[:self.bstack111l1llllll_opy_]
            del self.queue[:self.bstack111l1llllll_opy_]
        self.handler(data)
        if source != bstack1lll11l_opy_ (u"࠭ࡳࡩࡷࡷࡨࡴࡽ࡮ࠨ᯿"):
            self.bstack111l1lll111_opy_()
    def shutdown(self):
        self.bstack111l1lll1ll_opy_()
        while self.queue:
            self.bstack111l1llll11_opy_(source=bstack1lll11l_opy_ (u"ࠧࡴࡪࡸࡸࡩࡵࡷ࡯ࠩᰀ"))