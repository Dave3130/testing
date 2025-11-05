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
import logging
logger = logging.getLogger(__name__)
bstack111l1lll111_opy_ = 1000
bstack111l1ll11l1_opy_ = 2
class bstack111l1ll11ll_opy_:
    def __init__(self, handler, bstack111l1lll11l_opy_=bstack111l1lll111_opy_, bstack111l1ll1l11_opy_=bstack111l1ll11l1_opy_):
        self.queue = []
        self.handler = handler
        self.bstack111l1lll11l_opy_ = bstack111l1lll11l_opy_
        self.bstack111l1ll1l11_opy_ = bstack111l1ll1l11_opy_
        self.lock = threading.Lock()
        self.timer = None
        self.bstack1l1ll11ll11_opy_ = None
    def start(self):
        if not (self.timer and self.timer.is_alive()):
            self.bstack111l1lll1ll_opy_()
    def bstack111l1lll1ll_opy_(self):
        self.bstack1l1ll11ll11_opy_ = threading.Event()
        def bstack111l1ll1ll1_opy_():
            self.bstack1l1ll11ll11_opy_.wait(self.bstack111l1ll1l11_opy_)
            if not self.bstack1l1ll11ll11_opy_.is_set():
                self.bstack111l1lll1l1_opy_()
        self.timer = threading.Thread(target=bstack111l1ll1ll1_opy_, daemon=True)
        self.timer.start()
    def bstack111l1ll1lll_opy_(self):
        try:
            if self.bstack1l1ll11ll11_opy_ and not self.bstack1l1ll11ll11_opy_.is_set():
                self.bstack1l1ll11ll11_opy_.set()
            if self.timer and self.timer.is_alive() and self.timer != threading.current_thread():
                self.timer.join()
        except Exception as e:
            logger.debug(bstack11ll1ll_opy_ (u"ࠩ࡞ࡷࡹࡵࡰࡠࡶ࡬ࡱࡪࡸ࡝ࠡࡇࡻࡧࡪࡶࡴࡪࡱࡱ࠾ࠥ࠭ᰗ") + (str(e) or bstack11ll1ll_opy_ (u"ࠥࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡣࡰࡷ࡯ࡨࠥࡴ࡯ࡵࠢࡥࡩࠥࡩ࡯࡯ࡸࡨࡶࡹ࡫ࡤࠡࡶࡲࠤࡸࡺࡲࡪࡰࡪࠦᰘ")))
        finally:
            self.timer = None
    def bstack111l1ll1l1l_opy_(self):
        if self.timer:
            self.bstack111l1ll1lll_opy_()
        self.bstack111l1lll1ll_opy_()
    def add(self, event):
        with self.lock:
            self.queue.append(event)
            if len(self.queue) >= self.bstack111l1lll11l_opy_:
                threading.Thread(target=self.bstack111l1lll1l1_opy_).start()
    def bstack111l1lll1l1_opy_(self, source = bstack11ll1ll_opy_ (u"ࠫࠬᰙ")):
        with self.lock:
            if not self.queue:
                self.bstack111l1ll1l1l_opy_()
                return
            data = self.queue[:self.bstack111l1lll11l_opy_]
            del self.queue[:self.bstack111l1lll11l_opy_]
        self.handler(data)
        if source != bstack11ll1ll_opy_ (u"ࠬࡹࡨࡶࡶࡧࡳࡼࡴࠧᰚ"):
            self.bstack111l1ll1l1l_opy_()
    def shutdown(self):
        self.bstack111l1ll1lll_opy_()
        while self.queue:
            self.bstack111l1lll1l1_opy_(source=bstack11ll1ll_opy_ (u"࠭ࡳࡩࡷࡷࡨࡴࡽ࡮ࠨᰛ"))