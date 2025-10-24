# coding: UTF-8
import sys
bstack1lll1_opy_ = sys.version_info [0] == 2
bstack11l11_opy_ = 2048
bstack1_opy_ = 7
def bstack1l1_opy_ (bstack1llllll_opy_):
    global bstack1l11111_opy_
    bstack1l111l_opy_ = ord (bstack1llllll_opy_ [-1])
    bstack11l1ll1_opy_ = bstack1llllll_opy_ [:-1]
    bstack11l1l1l_opy_ = bstack1l111l_opy_ % len (bstack11l1ll1_opy_)
    bstack11111l1_opy_ = bstack11l1ll1_opy_ [:bstack11l1l1l_opy_] + bstack11l1ll1_opy_ [bstack11l1l1l_opy_:]
    if bstack1lll1_opy_:
        bstack1lllll1_opy_ = unicode () .join ([unichr (ord (char) - bstack11l11_opy_ - (bstack1l1ll11_opy_ + bstack1l111l_opy_) % bstack1_opy_) for bstack1l1ll11_opy_, char in enumerate (bstack11111l1_opy_)])
    else:
        bstack1lllll1_opy_ = str () .join ([chr (ord (char) - bstack11l11_opy_ - (bstack1l1ll11_opy_ + bstack1l111l_opy_) % bstack1_opy_) for bstack1l1ll11_opy_, char in enumerate (bstack11111l1_opy_)])
    return eval (bstack1lllll1_opy_)
import threading
import logging
logger = logging.getLogger(__name__)
bstack111l1llll1l_opy_ = 1000
bstack111ll111ll1_opy_ = 2
class bstack111ll1111l1_opy_:
    def __init__(self, handler, bstack111ll1111ll_opy_=bstack111l1llll1l_opy_, bstack111ll11111l_opy_=bstack111ll111ll1_opy_):
        self.queue = []
        self.handler = handler
        self.bstack111ll1111ll_opy_ = bstack111ll1111ll_opy_
        self.bstack111ll11111l_opy_ = bstack111ll11111l_opy_
        self.lock = threading.Lock()
        self.timer = None
        self.bstack1l1ll1l1l11_opy_ = None
    def start(self):
        if not (self.timer and self.timer.is_alive()):
            self.bstack111ll111l11_opy_()
    def bstack111ll111l11_opy_(self):
        self.bstack1l1ll1l1l11_opy_ = threading.Event()
        def bstack111ll111111_opy_():
            self.bstack1l1ll1l1l11_opy_.wait(self.bstack111ll11111l_opy_)
            if not self.bstack1l1ll1l1l11_opy_.is_set():
                self.bstack111l1lllll1_opy_()
        self.timer = threading.Thread(target=bstack111ll111111_opy_, daemon=True)
        self.timer.start()
    def bstack111l1llllll_opy_(self):
        try:
            if self.bstack1l1ll1l1l11_opy_ and not self.bstack1l1ll1l1l11_opy_.is_set():
                self.bstack1l1ll1l1l11_opy_.set()
            if self.timer and self.timer.is_alive() and self.timer != threading.current_thread():
                self.timer.join()
        except Exception as e:
            logger.debug(bstack1l1_opy_ (u"ࠧ࡜ࡵࡷࡳࡵࡥࡴࡪ࡯ࡨࡶࡢࠦࡅࡹࡥࡨࡴࡹ࡯࡯࡯࠼ࠣࠫᯝ") + (str(e) or bstack1l1_opy_ (u"ࠣࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤࡨࡵࡵ࡭ࡦࠣࡲࡴࡺࠠࡣࡧࠣࡧࡴࡴࡶࡦࡴࡷࡩࡩࠦࡴࡰࠢࡶࡸࡷ࡯࡮ࡨࠤᯞ")))
        finally:
            self.timer = None
    def bstack111ll111l1l_opy_(self):
        if self.timer:
            self.bstack111l1llllll_opy_()
        self.bstack111ll111l11_opy_()
    def add(self, event):
        with self.lock:
            self.queue.append(event)
            if len(self.queue) >= self.bstack111ll1111ll_opy_:
                threading.Thread(target=self.bstack111l1lllll1_opy_).start()
    def bstack111l1lllll1_opy_(self, source = bstack1l1_opy_ (u"ࠩࠪᯟ")):
        with self.lock:
            if not self.queue:
                self.bstack111ll111l1l_opy_()
                return
            data = self.queue[:self.bstack111ll1111ll_opy_]
            del self.queue[:self.bstack111ll1111ll_opy_]
        self.handler(data)
        if source != bstack1l1_opy_ (u"ࠪࡷ࡭ࡻࡴࡥࡱࡺࡲࠬᯠ"):
            self.bstack111ll111l1l_opy_()
    def shutdown(self):
        self.bstack111l1llllll_opy_()
        while self.queue:
            self.bstack111l1lllll1_opy_(source=bstack1l1_opy_ (u"ࠫࡸ࡮ࡵࡵࡦࡲࡻࡳ࠭ᯡ"))