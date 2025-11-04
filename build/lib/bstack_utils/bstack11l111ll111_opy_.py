# coding: UTF-8
import sys
bstack11l111_opy_ = sys.version_info [0] == 2
bstack1l11ll_opy_ = 2048
bstack1l1l11_opy_ = 7
def bstack11l1111_opy_ (bstack111l11l_opy_):
    global bstack1ll1l1l_opy_
    bstack1ll1ll_opy_ = ord (bstack111l11l_opy_ [-1])
    bstack1lll11_opy_ = bstack111l11l_opy_ [:-1]
    bstack111l111_opy_ = bstack1ll1ll_opy_ % len (bstack1lll11_opy_)
    bstack1l1l1ll_opy_ = bstack1lll11_opy_ [:bstack111l111_opy_] + bstack1lll11_opy_ [bstack111l111_opy_:]
    if bstack11l111_opy_:
        bstack1l11_opy_ = unicode () .join ([unichr (ord (char) - bstack1l11ll_opy_ - (bstack1llll_opy_ + bstack1ll1ll_opy_) % bstack1l1l11_opy_) for bstack1llll_opy_, char in enumerate (bstack1l1l1ll_opy_)])
    else:
        bstack1l11_opy_ = str () .join ([chr (ord (char) - bstack1l11ll_opy_ - (bstack1llll_opy_ + bstack1ll1ll_opy_) % bstack1l1l11_opy_) for bstack1llll_opy_, char in enumerate (bstack1l1l1ll_opy_)])
    return eval (bstack1l11_opy_)
import threading
import logging
logger = logging.getLogger(__name__)
bstack111l1ll1lll_opy_ = 1000
bstack111l1lll1l1_opy_ = 2
class bstack111l1ll11l1_opy_:
    def __init__(self, handler, bstack111l1lll111_opy_=bstack111l1ll1lll_opy_, bstack111l1ll1l11_opy_=bstack111l1lll1l1_opy_):
        self.queue = []
        self.handler = handler
        self.bstack111l1lll111_opy_ = bstack111l1lll111_opy_
        self.bstack111l1ll1l11_opy_ = bstack111l1ll1l11_opy_
        self.lock = threading.Lock()
        self.timer = None
        self.bstack1l1ll11ll1l_opy_ = None
    def start(self):
        if not (self.timer and self.timer.is_alive()):
            self.bstack111l1lll11l_opy_()
    def bstack111l1lll11l_opy_(self):
        self.bstack1l1ll11ll1l_opy_ = threading.Event()
        def bstack111l1ll111l_opy_():
            self.bstack1l1ll11ll1l_opy_.wait(self.bstack111l1ll1l11_opy_)
            if not self.bstack1l1ll11ll1l_opy_.is_set():
                self.bstack111l1ll1l1l_opy_()
        self.timer = threading.Thread(target=bstack111l1ll111l_opy_, daemon=True)
        self.timer.start()
    def bstack111l1ll1ll1_opy_(self):
        try:
            if self.bstack1l1ll11ll1l_opy_ and not self.bstack1l1ll11ll1l_opy_.is_set():
                self.bstack1l1ll11ll1l_opy_.set()
            if self.timer and self.timer.is_alive() and self.timer != threading.current_thread():
                self.timer.join()
        except Exception as e:
            logger.debug(bstack11l1111_opy_ (u"ࠧ࡜ࡵࡷࡳࡵࡥࡴࡪ࡯ࡨࡶࡢࠦࡅࡹࡥࡨࡴࡹ࡯࡯࡯࠼ࠣࠫᰕ") + (str(e) or bstack11l1111_opy_ (u"ࠣࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤࡨࡵࡵ࡭ࡦࠣࡲࡴࡺࠠࡣࡧࠣࡧࡴࡴࡶࡦࡴࡷࡩࡩࠦࡴࡰࠢࡶࡸࡷ࡯࡮ࡨࠤᰖ")))
        finally:
            self.timer = None
    def bstack111l1ll11ll_opy_(self):
        if self.timer:
            self.bstack111l1ll1ll1_opy_()
        self.bstack111l1lll11l_opy_()
    def add(self, event):
        with self.lock:
            self.queue.append(event)
            if len(self.queue) >= self.bstack111l1lll111_opy_:
                threading.Thread(target=self.bstack111l1ll1l1l_opy_).start()
    def bstack111l1ll1l1l_opy_(self, source = bstack11l1111_opy_ (u"ࠩࠪᰗ")):
        with self.lock:
            if not self.queue:
                self.bstack111l1ll11ll_opy_()
                return
            data = self.queue[:self.bstack111l1lll111_opy_]
            del self.queue[:self.bstack111l1lll111_opy_]
        self.handler(data)
        if source != bstack11l1111_opy_ (u"ࠪࡷ࡭ࡻࡴࡥࡱࡺࡲࠬᰘ"):
            self.bstack111l1ll11ll_opy_()
    def shutdown(self):
        self.bstack111l1ll1ll1_opy_()
        while self.queue:
            self.bstack111l1ll1l1l_opy_(source=bstack11l1111_opy_ (u"ࠫࡸ࡮ࡵࡵࡦࡲࡻࡳ࠭ᰙ"))