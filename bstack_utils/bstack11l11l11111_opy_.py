# coding: UTF-8
import sys
bstack1ll1lll_opy_ = sys.version_info [0] == 2
bstack1l1ll_opy_ = 2048
bstack11l1l1_opy_ = 7
def bstack111l1l_opy_ (bstack1l_opy_):
    global bstack11111ll_opy_
    bstack1lll11l_opy_ = ord (bstack1l_opy_ [-1])
    bstack111ll1_opy_ = bstack1l_opy_ [:-1]
    bstack1ll11l_opy_ = bstack1lll11l_opy_ % len (bstack111ll1_opy_)
    bstack11l111_opy_ = bstack111ll1_opy_ [:bstack1ll11l_opy_] + bstack111ll1_opy_ [bstack1ll11l_opy_:]
    if bstack1ll1lll_opy_:
        bstack1l11l11_opy_ = unicode () .join ([unichr (ord (char) - bstack1l1ll_opy_ - (bstack11llll_opy_ + bstack1lll11l_opy_) % bstack11l1l1_opy_) for bstack11llll_opy_, char in enumerate (bstack11l111_opy_)])
    else:
        bstack1l11l11_opy_ = str () .join ([chr (ord (char) - bstack1l1ll_opy_ - (bstack11llll_opy_ + bstack1lll11l_opy_) % bstack11l1l1_opy_) for bstack11llll_opy_, char in enumerate (bstack11l111_opy_)])
    return eval (bstack1l11l11_opy_)
import threading
import logging
logger = logging.getLogger(__name__)
bstack111l1llll1l_opy_ = 1000
bstack111l1lll1l1_opy_ = 2
class bstack111ll1111l1_opy_:
    def __init__(self, handler, bstack111ll11111l_opy_=bstack111l1llll1l_opy_, bstack111l1llllll_opy_=bstack111l1lll1l1_opy_):
        self.queue = []
        self.handler = handler
        self.bstack111ll11111l_opy_ = bstack111ll11111l_opy_
        self.bstack111l1llllll_opy_ = bstack111l1llllll_opy_
        self.lock = threading.Lock()
        self.timer = None
        self.bstack1l1ll1l1111_opy_ = None
    def start(self):
        if not (self.timer and self.timer.is_alive()):
            self.bstack111l1lll1ll_opy_()
    def bstack111l1lll1ll_opy_(self):
        self.bstack1l1ll1l1111_opy_ = threading.Event()
        def bstack111ll1111ll_opy_():
            self.bstack1l1ll1l1111_opy_.wait(self.bstack111l1llllll_opy_)
            if not self.bstack1l1ll1l1111_opy_.is_set():
                self.bstack111ll111111_opy_()
        self.timer = threading.Thread(target=bstack111ll1111ll_opy_, daemon=True)
        self.timer.start()
    def bstack111l1llll11_opy_(self):
        try:
            if self.bstack1l1ll1l1111_opy_ and not self.bstack1l1ll1l1111_opy_.is_set():
                self.bstack1l1ll1l1111_opy_.set()
            if self.timer and self.timer.is_alive() and self.timer != threading.current_thread():
                self.timer.join()
        except Exception as e:
            logger.debug(bstack111l1l_opy_ (u"࡛࠭ࡴࡶࡲࡴࡤࡺࡩ࡮ࡧࡵࡡࠥࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮࠻ࠢࠪᯣ") + (str(e) or bstack111l1l_opy_ (u"ࠢࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣࡧࡴࡻ࡬ࡥࠢࡱࡳࡹࠦࡢࡦࠢࡦࡳࡳࡼࡥࡳࡶࡨࡨࠥࡺ࡯ࠡࡵࡷࡶ࡮ࡴࡧࠣᯤ")))
        finally:
            self.timer = None
    def bstack111l1lllll1_opy_(self):
        if self.timer:
            self.bstack111l1llll11_opy_()
        self.bstack111l1lll1ll_opy_()
    def add(self, event):
        with self.lock:
            self.queue.append(event)
            if len(self.queue) >= self.bstack111ll11111l_opy_:
                threading.Thread(target=self.bstack111ll111111_opy_).start()
    def bstack111ll111111_opy_(self, source = bstack111l1l_opy_ (u"ࠨࠩᯥ")):
        with self.lock:
            if not self.queue:
                self.bstack111l1lllll1_opy_()
                return
            data = self.queue[:self.bstack111ll11111l_opy_]
            del self.queue[:self.bstack111ll11111l_opy_]
        self.handler(data)
        if source != bstack111l1l_opy_ (u"ࠩࡶ࡬ࡺࡺࡤࡰࡹࡱ᯦ࠫ"):
            self.bstack111l1lllll1_opy_()
    def shutdown(self):
        self.bstack111l1llll11_opy_()
        while self.queue:
            self.bstack111ll111111_opy_(source=bstack111l1l_opy_ (u"ࠪࡷ࡭ࡻࡴࡥࡱࡺࡲࠬᯧ"))