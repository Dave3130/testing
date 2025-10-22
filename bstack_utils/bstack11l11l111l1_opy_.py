# coding: UTF-8
import sys
bstack1l11l_opy_ = sys.version_info [0] == 2
bstack1111_opy_ = 2048
bstack1lll1_opy_ = 7
def bstack1lllll1l_opy_ (bstack1ll1l11_opy_):
    global bstack11l1ll_opy_
    bstack111lll_opy_ = ord (bstack1ll1l11_opy_ [-1])
    bstack1l111l1_opy_ = bstack1ll1l11_opy_ [:-1]
    bstack1111l_opy_ = bstack111lll_opy_ % len (bstack1l111l1_opy_)
    bstack1111ll_opy_ = bstack1l111l1_opy_ [:bstack1111l_opy_] + bstack1l111l1_opy_ [bstack1111l_opy_:]
    if bstack1l11l_opy_:
        bstack1l1l1_opy_ = unicode () .join ([unichr (ord (char) - bstack1111_opy_ - (bstack1ll1111_opy_ + bstack111lll_opy_) % bstack1lll1_opy_) for bstack1ll1111_opy_, char in enumerate (bstack1111ll_opy_)])
    else:
        bstack1l1l1_opy_ = str () .join ([chr (ord (char) - bstack1111_opy_ - (bstack1ll1111_opy_ + bstack111lll_opy_) % bstack1lll1_opy_) for bstack1ll1111_opy_, char in enumerate (bstack1111ll_opy_)])
    return eval (bstack1l1l1_opy_)
import threading
import logging
logger = logging.getLogger(__name__)
bstack111l1llll11_opy_ = 1000
bstack111l1llllll_opy_ = 2
class bstack111ll111111_opy_:
    def __init__(self, handler, bstack111ll1111l1_opy_=bstack111l1llll11_opy_, bstack111ll1111ll_opy_=bstack111l1llllll_opy_):
        self.queue = []
        self.handler = handler
        self.bstack111ll1111l1_opy_ = bstack111ll1111l1_opy_
        self.bstack111ll1111ll_opy_ = bstack111ll1111ll_opy_
        self.lock = threading.Lock()
        self.timer = None
        self.bstack1l1ll1l1111_opy_ = None
    def start(self):
        if not (self.timer and self.timer.is_alive()):
            self.bstack111l1lllll1_opy_()
    def bstack111l1lllll1_opy_(self):
        self.bstack1l1ll1l1111_opy_ = threading.Event()
        def bstack111ll111l11_opy_():
            self.bstack1l1ll1l1111_opy_.wait(self.bstack111ll1111ll_opy_)
            if not self.bstack1l1ll1l1111_opy_.is_set():
                self.bstack111ll111l1l_opy_()
        self.timer = threading.Thread(target=bstack111ll111l11_opy_, daemon=True)
        self.timer.start()
    def bstack111ll11111l_opy_(self):
        try:
            if self.bstack1l1ll1l1111_opy_ and not self.bstack1l1ll1l1111_opy_.is_set():
                self.bstack1l1ll1l1111_opy_.set()
            if self.timer and self.timer.is_alive() and self.timer != threading.current_thread():
                self.timer.join()
        except Exception as e:
            logger.debug(bstack1lllll1l_opy_ (u"ࠩ࡞ࡷࡹࡵࡰࡠࡶ࡬ࡱࡪࡸ࡝ࠡࡇࡻࡧࡪࡶࡴࡪࡱࡱ࠾᯦ࠥ࠭") + (str(e) or bstack1lllll1l_opy_ (u"ࠥࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡣࡰࡷ࡯ࡨࠥࡴ࡯ࡵࠢࡥࡩࠥࡩ࡯࡯ࡸࡨࡶࡹ࡫ࡤࠡࡶࡲࠤࡸࡺࡲࡪࡰࡪࠦᯧ")))
        finally:
            self.timer = None
    def bstack111l1llll1l_opy_(self):
        if self.timer:
            self.bstack111ll11111l_opy_()
        self.bstack111l1lllll1_opy_()
    def add(self, event):
        with self.lock:
            self.queue.append(event)
            if len(self.queue) >= self.bstack111ll1111l1_opy_:
                threading.Thread(target=self.bstack111ll111l1l_opy_).start()
    def bstack111ll111l1l_opy_(self, source = bstack1lllll1l_opy_ (u"ࠫࠬᯨ")):
        with self.lock:
            if not self.queue:
                self.bstack111l1llll1l_opy_()
                return
            data = self.queue[:self.bstack111ll1111l1_opy_]
            del self.queue[:self.bstack111ll1111l1_opy_]
        self.handler(data)
        if source != bstack1lllll1l_opy_ (u"ࠬࡹࡨࡶࡶࡧࡳࡼࡴࠧᯩ"):
            self.bstack111l1llll1l_opy_()
    def shutdown(self):
        self.bstack111ll11111l_opy_()
        while self.queue:
            self.bstack111ll111l1l_opy_(source=bstack1lllll1l_opy_ (u"࠭ࡳࡩࡷࡷࡨࡴࡽ࡮ࠨᯪ"))