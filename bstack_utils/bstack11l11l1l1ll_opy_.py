# coding: UTF-8
import sys
bstack1_opy_ = sys.version_info [0] == 2
bstack11l1ll1_opy_ = 2048
bstack1l1l1ll_opy_ = 7
def bstack11l1l11_opy_ (bstack111l1ll_opy_):
    global bstack1l1lll1_opy_
    bstack1l1l11_opy_ = ord (bstack111l1ll_opy_ [-1])
    bstack111l1l1_opy_ = bstack111l1ll_opy_ [:-1]
    bstack111ll_opy_ = bstack1l1l11_opy_ % len (bstack111l1l1_opy_)
    bstack11l11l1_opy_ = bstack111l1l1_opy_ [:bstack111ll_opy_] + bstack111l1l1_opy_ [bstack111ll_opy_:]
    if bstack1_opy_:
        bstack1111l1l_opy_ = unicode () .join ([unichr (ord (char) - bstack11l1ll1_opy_ - (bstack1l111ll_opy_ + bstack1l1l11_opy_) % bstack1l1l1ll_opy_) for bstack1l111ll_opy_, char in enumerate (bstack11l11l1_opy_)])
    else:
        bstack1111l1l_opy_ = str () .join ([chr (ord (char) - bstack11l1ll1_opy_ - (bstack1l111ll_opy_ + bstack1l1l11_opy_) % bstack1l1l1ll_opy_) for bstack1l111ll_opy_, char in enumerate (bstack11l11l1_opy_)])
    return eval (bstack1111l1l_opy_)
import threading
import logging
logger = logging.getLogger(__name__)
bstack111ll11l111_opy_ = 1000
bstack111ll11l1ll_opy_ = 2
class bstack111ll11l1l1_opy_:
    def __init__(self, handler, bstack111ll11ll11_opy_=bstack111ll11l111_opy_, bstack111ll11l11l_opy_=bstack111ll11l1ll_opy_):
        self.queue = []
        self.handler = handler
        self.bstack111ll11ll11_opy_ = bstack111ll11ll11_opy_
        self.bstack111ll11l11l_opy_ = bstack111ll11l11l_opy_
        self.lock = threading.Lock()
        self.timer = None
        self.bstack1l1ll1lll1l_opy_ = None
    def start(self):
        if not (self.timer and self.timer.is_alive()):
            self.bstack111ll111ll1_opy_()
    def bstack111ll111ll1_opy_(self):
        self.bstack1l1ll1lll1l_opy_ = threading.Event()
        def bstack111ll11lll1_opy_():
            self.bstack1l1ll1lll1l_opy_.wait(self.bstack111ll11l11l_opy_)
            if not self.bstack1l1ll1lll1l_opy_.is_set():
                self.bstack111ll111lll_opy_()
        self.timer = threading.Thread(target=bstack111ll11lll1_opy_, daemon=True)
        self.timer.start()
    def bstack111ll111l1l_opy_(self):
        try:
            if self.bstack1l1ll1lll1l_opy_ and not self.bstack1l1ll1lll1l_opy_.is_set():
                self.bstack1l1ll1lll1l_opy_.set()
            if self.timer and self.timer.is_alive() and self.timer != threading.current_thread():
                self.timer.join()
        except Exception as e:
            logger.debug(bstack11l1l11_opy_ (u"ࠫࡠࡹࡴࡰࡲࡢࡸ࡮ࡳࡥࡳ࡟ࠣࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࡀࠠࠨᮾ") + (str(e) or bstack11l1l11_opy_ (u"ࠧࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡࡥࡲࡹࡱࡪࠠ࡯ࡱࡷࠤࡧ࡫ࠠࡤࡱࡱࡺࡪࡸࡴࡦࡦࠣࡸࡴࠦࡳࡵࡴ࡬ࡲ࡬ࠨᮿ")))
        finally:
            self.timer = None
    def bstack111ll11ll1l_opy_(self):
        if self.timer:
            self.bstack111ll111l1l_opy_()
        self.bstack111ll111ll1_opy_()
    def add(self, event):
        with self.lock:
            self.queue.append(event)
            if len(self.queue) >= self.bstack111ll11ll11_opy_:
                threading.Thread(target=self.bstack111ll111lll_opy_).start()
    def bstack111ll111lll_opy_(self, source = bstack11l1l11_opy_ (u"࠭ࠧᯀ")):
        with self.lock:
            if not self.queue:
                self.bstack111ll11ll1l_opy_()
                return
            data = self.queue[:self.bstack111ll11ll11_opy_]
            del self.queue[:self.bstack111ll11ll11_opy_]
        self.handler(data)
        if source != bstack11l1l11_opy_ (u"ࠧࡴࡪࡸࡸࡩࡵࡷ࡯ࠩᯁ"):
            self.bstack111ll11ll1l_opy_()
    def shutdown(self):
        self.bstack111ll111l1l_opy_()
        while self.queue:
            self.bstack111ll111lll_opy_(source=bstack11l1l11_opy_ (u"ࠨࡵ࡫ࡹࡹࡪ࡯ࡸࡰࠪᯂ"))