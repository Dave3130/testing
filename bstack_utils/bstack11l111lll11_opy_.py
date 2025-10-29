# coding: UTF-8
import sys
bstack1l1l111_opy_ = sys.version_info [0] == 2
bstack11l1ll_opy_ = 2048
bstack1llll11_opy_ = 7
def bstack11ll1l_opy_ (bstack1llllll1_opy_):
    global bstack1ll11_opy_
    bstack11ll111_opy_ = ord (bstack1llllll1_opy_ [-1])
    bstack1lll111_opy_ = bstack1llllll1_opy_ [:-1]
    bstack11l11l_opy_ = bstack11ll111_opy_ % len (bstack1lll111_opy_)
    bstack1l1ll11_opy_ = bstack1lll111_opy_ [:bstack11l11l_opy_] + bstack1lll111_opy_ [bstack11l11l_opy_:]
    if bstack1l1l111_opy_:
        bstack11111l1_opy_ = unicode () .join ([unichr (ord (char) - bstack11l1ll_opy_ - (bstack1l11111_opy_ + bstack11ll111_opy_) % bstack1llll11_opy_) for bstack1l11111_opy_, char in enumerate (bstack1l1ll11_opy_)])
    else:
        bstack11111l1_opy_ = str () .join ([chr (ord (char) - bstack11l1ll_opy_ - (bstack1l11111_opy_ + bstack11ll111_opy_) % bstack1llll11_opy_) for bstack1l11111_opy_, char in enumerate (bstack1l1ll11_opy_)])
    return eval (bstack11111l1_opy_)
import threading
import logging
logger = logging.getLogger(__name__)
bstack111l1lllll1_opy_ = 1000
bstack111l1lll1ll_opy_ = 2
class bstack111l1lll111_opy_:
    def __init__(self, handler, bstack111l1lll1l1_opy_=bstack111l1lllll1_opy_, bstack111ll111111_opy_=bstack111l1lll1ll_opy_):
        self.queue = []
        self.handler = handler
        self.bstack111l1lll1l1_opy_ = bstack111l1lll1l1_opy_
        self.bstack111ll111111_opy_ = bstack111ll111111_opy_
        self.lock = threading.Lock()
        self.timer = None
        self.bstack1l1ll11ll1l_opy_ = None
    def start(self):
        if not (self.timer and self.timer.is_alive()):
            self.bstack111l1llllll_opy_()
    def bstack111l1llllll_opy_(self):
        self.bstack1l1ll11ll1l_opy_ = threading.Event()
        def bstack111l1llll11_opy_():
            self.bstack1l1ll11ll1l_opy_.wait(self.bstack111ll111111_opy_)
            if not self.bstack1l1ll11ll1l_opy_.is_set():
                self.bstack111l1ll1lll_opy_()
        self.timer = threading.Thread(target=bstack111l1llll11_opy_, daemon=True)
        self.timer.start()
    def bstack111l1llll1l_opy_(self):
        try:
            if self.bstack1l1ll11ll1l_opy_ and not self.bstack1l1ll11ll1l_opy_.is_set():
                self.bstack1l1ll11ll1l_opy_.set()
            if self.timer and self.timer.is_alive() and self.timer != threading.current_thread():
                self.timer.join()
        except Exception as e:
            logger.debug(bstack11ll1l_opy_ (u"ࠫࡠࡹࡴࡰࡲࡢࡸ࡮ࡳࡥࡳ࡟ࠣࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࡀࠠࠨᰄ") + (str(e) or bstack11ll1l_opy_ (u"ࠧࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡࡥࡲࡹࡱࡪࠠ࡯ࡱࡷࠤࡧ࡫ࠠࡤࡱࡱࡺࡪࡸࡴࡦࡦࠣࡸࡴࠦࡳࡵࡴ࡬ࡲ࡬ࠨᰅ")))
        finally:
            self.timer = None
    def bstack111l1lll11l_opy_(self):
        if self.timer:
            self.bstack111l1llll1l_opy_()
        self.bstack111l1llllll_opy_()
    def add(self, event):
        with self.lock:
            self.queue.append(event)
            if len(self.queue) >= self.bstack111l1lll1l1_opy_:
                threading.Thread(target=self.bstack111l1ll1lll_opy_).start()
    def bstack111l1ll1lll_opy_(self, source = bstack11ll1l_opy_ (u"࠭ࠧᰆ")):
        with self.lock:
            if not self.queue:
                self.bstack111l1lll11l_opy_()
                return
            data = self.queue[:self.bstack111l1lll1l1_opy_]
            del self.queue[:self.bstack111l1lll1l1_opy_]
        self.handler(data)
        if source != bstack11ll1l_opy_ (u"ࠧࡴࡪࡸࡸࡩࡵࡷ࡯ࠩᰇ"):
            self.bstack111l1lll11l_opy_()
    def shutdown(self):
        self.bstack111l1llll1l_opy_()
        while self.queue:
            self.bstack111l1ll1lll_opy_(source=bstack11ll1l_opy_ (u"ࠨࡵ࡫ࡹࡹࡪ࡯ࡸࡰࠪᰈ"))