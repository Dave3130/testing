# coding: UTF-8
import sys
bstack11ll1l1_opy_ = sys.version_info [0] == 2
bstack11111ll_opy_ = 2048
bstack111lll1_opy_ = 7
def bstack1l1lll1_opy_ (bstack1lllll_opy_):
    global bstack111111l_opy_
    bstack1llll_opy_ = ord (bstack1lllll_opy_ [-1])
    bstack11lll1l_opy_ = bstack1lllll_opy_ [:-1]
    bstack1111_opy_ = bstack1llll_opy_ % len (bstack11lll1l_opy_)
    bstack11ll11l_opy_ = bstack11lll1l_opy_ [:bstack1111_opy_] + bstack11lll1l_opy_ [bstack1111_opy_:]
    if bstack11ll1l1_opy_:
        bstack1llll1_opy_ = unicode () .join ([unichr (ord (char) - bstack11111ll_opy_ - (bstack1l1l1ll_opy_ + bstack1llll_opy_) % bstack111lll1_opy_) for bstack1l1l1ll_opy_, char in enumerate (bstack11ll11l_opy_)])
    else:
        bstack1llll1_opy_ = str () .join ([chr (ord (char) - bstack11111ll_opy_ - (bstack1l1l1ll_opy_ + bstack1llll_opy_) % bstack111lll1_opy_) for bstack1l1l1ll_opy_, char in enumerate (bstack11ll11l_opy_)])
    return eval (bstack1llll1_opy_)
import threading
import logging
logger = logging.getLogger(__name__)
bstack111ll11ll1l_opy_ = 1000
bstack111ll11l1l1_opy_ = 2
class bstack111ll111l11_opy_:
    def __init__(self, handler, bstack111ll111lll_opy_=bstack111ll11ll1l_opy_, bstack111ll11l1ll_opy_=bstack111ll11l1l1_opy_):
        self.queue = []
        self.handler = handler
        self.bstack111ll111lll_opy_ = bstack111ll111lll_opy_
        self.bstack111ll11l1ll_opy_ = bstack111ll11l1ll_opy_
        self.lock = threading.Lock()
        self.timer = None
        self.bstack1l1ll1ll1ll_opy_ = None
    def start(self):
        if not (self.timer and self.timer.is_alive()):
            self.bstack111ll11ll11_opy_()
    def bstack111ll11ll11_opy_(self):
        self.bstack1l1ll1ll1ll_opy_ = threading.Event()
        def bstack111ll11l111_opy_():
            self.bstack1l1ll1ll1ll_opy_.wait(self.bstack111ll11l1ll_opy_)
            if not self.bstack1l1ll1ll1ll_opy_.is_set():
                self.bstack111ll111l1l_opy_()
        self.timer = threading.Thread(target=bstack111ll11l111_opy_, daemon=True)
        self.timer.start()
    def bstack111ll11l11l_opy_(self):
        try:
            if self.bstack1l1ll1ll1ll_opy_ and not self.bstack1l1ll1ll1ll_opy_.is_set():
                self.bstack1l1ll1ll1ll_opy_.set()
            if self.timer and self.timer.is_alive() and self.timer != threading.current_thread():
                self.timer.join()
        except Exception as e:
            logger.debug(bstack1l1lll1_opy_ (u"ࠧ࡜ࡵࡷࡳࡵࡥࡴࡪ࡯ࡨࡶࡢࠦࡅࡹࡥࡨࡴࡹ࡯࡯࡯࠼ࠣࠫᯁ") + (str(e) or bstack1l1lll1_opy_ (u"ࠣࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤࡨࡵࡵ࡭ࡦࠣࡲࡴࡺࠠࡣࡧࠣࡧࡴࡴࡶࡦࡴࡷࡩࡩࠦࡴࡰࠢࡶࡸࡷ࡯࡮ࡨࠤᯂ")))
        finally:
            self.timer = None
    def bstack111ll111ll1_opy_(self):
        if self.timer:
            self.bstack111ll11l11l_opy_()
        self.bstack111ll11ll11_opy_()
    def add(self, event):
        with self.lock:
            self.queue.append(event)
            if len(self.queue) >= self.bstack111ll111lll_opy_:
                threading.Thread(target=self.bstack111ll111l1l_opy_).start()
    def bstack111ll111l1l_opy_(self, source = bstack1l1lll1_opy_ (u"ࠩࠪᯃ")):
        with self.lock:
            if not self.queue:
                self.bstack111ll111ll1_opy_()
                return
            data = self.queue[:self.bstack111ll111lll_opy_]
            del self.queue[:self.bstack111ll111lll_opy_]
        self.handler(data)
        if source != bstack1l1lll1_opy_ (u"ࠪࡷ࡭ࡻࡴࡥࡱࡺࡲࠬᯄ"):
            self.bstack111ll111ll1_opy_()
    def shutdown(self):
        self.bstack111ll11l11l_opy_()
        while self.queue:
            self.bstack111ll111l1l_opy_(source=bstack1l1lll1_opy_ (u"ࠫࡸ࡮ࡵࡵࡦࡲࡻࡳ࠭ᯅ"))