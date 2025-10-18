# coding: UTF-8
import sys
bstack1ll1111_opy_ = sys.version_info [0] == 2
bstack1ll_opy_ = 2048
bstack1ll1l1_opy_ = 7
def bstack11l111_opy_ (bstack1ll1_opy_):
    global bstack11l1l_opy_
    bstack11l1l1_opy_ = ord (bstack1ll1_opy_ [-1])
    bstack111ll_opy_ = bstack1ll1_opy_ [:-1]
    bstack11111ll_opy_ = bstack11l1l1_opy_ % len (bstack111ll_opy_)
    bstack1l1lll_opy_ = bstack111ll_opy_ [:bstack11111ll_opy_] + bstack111ll_opy_ [bstack11111ll_opy_:]
    if bstack1ll1111_opy_:
        bstack1lll1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack1ll_opy_ - (bstack1l111_opy_ + bstack11l1l1_opy_) % bstack1ll1l1_opy_) for bstack1l111_opy_, char in enumerate (bstack1l1lll_opy_)])
    else:
        bstack1lll1ll_opy_ = str () .join ([chr (ord (char) - bstack1ll_opy_ - (bstack1l111_opy_ + bstack11l1l1_opy_) % bstack1ll1l1_opy_) for bstack1l111_opy_, char in enumerate (bstack1l1lll_opy_)])
    return eval (bstack1lll1ll_opy_)
import threading
import tempfile
import os
import time
from datetime import datetime
from bstack_utils.bstack11ll1l1ll1l_opy_ import bstack11ll1l1l11l_opy_
from bstack_utils.constants import bstack11ll1ll1l1l_opy_, bstack1111l1lll_opy_
from bstack_utils.bstack1111ll1l_opy_ import bstack1lll1l1ll_opy_
from bstack_utils import bstack11l111l1ll_opy_
bstack11l1lll11l1_opy_ = 10
class bstack1l11111ll1_opy_:
    def __init__(self, bstack111l11l11_opy_, config, bstack11ll1111111_opy_=0):
        self.bstack11l1ll1lll1_opy_ = set()
        self.lock = threading.Lock()
        self.bstack11l1lll1l11_opy_ = bstack11l111_opy_ (u"ࠢࡼࡿ࠲ࡸࡪࡹࡴࡰࡴࡦ࡬ࡪࡹࡴࡳࡣࡷ࡭ࡴࡴ࠯ࡢࡲ࡬࠳ࡻ࠷࠯ࡧࡣ࡬ࡰࡪࡪ࠭ࡵࡧࡶࡸࡸࠨᝌ").format(bstack11ll1ll1l1l_opy_)
        self.bstack11l1lll1ll1_opy_ = os.path.join(tempfile.gettempdir(), bstack11l111_opy_ (u"ࠣࡣࡥࡳࡷࡺ࡟ࡣࡷ࡬ࡰࡩࡥࡻࡾࠤᝍ").format(os.environ.get(bstack11l111_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡎࡕࡃࡡࡘ࡙ࡎࡊࠧᝎ"))))
        self.bstack11l1lll1111_opy_ = os.path.join(tempfile.gettempdir(), bstack11l111_opy_ (u"ࠥࡪࡦ࡯࡬ࡦࡦࡢࡸࡪࡹࡴࡴࡡࡾࢁ࠳ࡺࡸࡵࠤᝏ").format(os.environ.get(bstack11l111_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡉࡗࡅࡣ࡚࡛ࡉࡅࠩᝐ"))))
        self.bstack11l1lll11ll_opy_ = 2
        self.bstack111l11l11_opy_ = bstack111l11l11_opy_
        self.config = config
        self.logger = bstack11l111l1ll_opy_.get_logger(__name__, bstack1111l1lll_opy_)
        self.bstack11ll1111111_opy_ = bstack11ll1111111_opy_
        self.bstack11l1llll1l1_opy_ = False
        self.bstack11l1llllll1_opy_ = not (
                            os.environ.get(bstack11l111_opy_ (u"ࠧࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡇ࡛ࡉࡍࡆࡢࡖ࡚ࡔ࡟ࡊࡆࡈࡒ࡙ࡏࡆࡊࡇࡕࠦᝑ")) and
                            os.environ.get(bstack11l111_opy_ (u"ࠨࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡔࡏࡅࡇࡢࡍࡓࡊࡅ࡙ࠤᝒ")) and
                            os.environ.get(bstack11l111_opy_ (u"ࠢࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡐࡖࡄࡐࡤࡔࡏࡅࡇࡢࡇࡔ࡛ࡎࡕࠤᝓ"))
                        )
        if bstack1lll1l1ll_opy_.bstack11l1lllll1l_opy_(config):
            self.bstack11l1lll11ll_opy_ = bstack1lll1l1ll_opy_.bstack11l1lllllll_opy_(config, self.bstack11ll1111111_opy_)
            self.bstack11l1lll111l_opy_()
    def bstack11l1llll1ll_opy_(self):
        return bstack11l111_opy_ (u"ࠣࡽࢀࡣࢀࢃࠢ᝔").format(self.config.get(bstack11l111_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡏࡣࡰࡩࠬ᝕")), os.environ.get(bstack11l111_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡅ࡙ࡎࡒࡄࡠࡔࡘࡒࡤࡏࡄࡆࡐࡗࡍࡋࡏࡅࡓࠩ᝖")))
    def bstack11l1lllll11_opy_(self):
        try:
            if self.bstack11l1llllll1_opy_:
                return
            with self.lock:
                try:
                    with open(self.bstack11l1lll1111_opy_, bstack11l111_opy_ (u"ࠦࡷࠨ᝗")) as f:
                        bstack11l1ll1llll_opy_ = set(line.strip() for line in f if line.strip())
                except FileNotFoundError:
                    bstack11l1ll1llll_opy_ = set()
                bstack11l1llll11l_opy_ = bstack11l1ll1llll_opy_ - self.bstack11l1ll1lll1_opy_
                if not bstack11l1llll11l_opy_:
                    return
                self.bstack11l1ll1lll1_opy_.update(bstack11l1llll11l_opy_)
                data = {bstack11l111_opy_ (u"ࠧ࡬ࡡࡪ࡮ࡨࡨ࡙࡫ࡳࡵࡵࠥ᝘"): list(self.bstack11l1ll1lll1_opy_), bstack11l111_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡓࡧ࡭ࡦࠤ᝙"): self.config.get(bstack11l111_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡔࡡ࡮ࡧࠪ᝚")), bstack11l111_opy_ (u"ࠣࡤࡸ࡭ࡱࡪࡒࡶࡰࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷࠨ᝛"): os.environ.get(bstack11l111_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡄࡘࡍࡑࡊ࡟ࡓࡗࡑࡣࡎࡊࡅࡏࡖࡌࡊࡎࡋࡒࠨ᝜")), bstack11l111_opy_ (u"ࠥࡴࡷࡵࡪࡦࡥࡷࡒࡦࡳࡥࠣ᝝"): self.config.get(bstack11l111_opy_ (u"ࠫࡵࡸ࡯࡫ࡧࡦࡸࡓࡧ࡭ࡦࠩ᝞"))}
            response = bstack11ll1l1l11l_opy_.bstack11ll111ll1l_opy_(self.bstack11l1lll1l11_opy_, data)
            if response.get(bstack11l111_opy_ (u"ࠧࡹࡴࡢࡶࡸࡷࠧ᝟")) == 200:
                self.logger.debug(bstack11l111_opy_ (u"ࠨࡓࡶࡥࡦࡩࡸࡹࡦࡶ࡮࡯ࡽࠥࡹࡥ࡯ࡶࠣࡪࡦ࡯࡬ࡦࡦࠣࡸࡪࡹࡴࡴ࠼ࠣࡿࢂࠨᝠ").format(data))
            else:
                self.logger.debug(bstack11l111_opy_ (u"ࠢࡇࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡷࡪࡴࡤࠡࡨࡤ࡭ࡱ࡫ࡤࠡࡶࡨࡷࡹࡹ࠺ࠡࡽࢀࠦᝡ").format(response))
        except Exception as e:
            self.logger.debug(bstack11l111_opy_ (u"ࠣࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤࡩࡻࡲࡪࡰࡪࠤࡸ࡫࡮ࡥ࡫ࡱ࡫ࠥ࡬ࡡࡪ࡮ࡨࡨࠥࡺࡥࡴࡶࡶ࠾ࠥࢁࡽࠣᝢ").format(e))
    def bstack11ll11l11l1_opy_(self):
        if self.bstack11l1llllll1_opy_:
            with self.lock:
                try:
                    with open(self.bstack11l1lll1111_opy_, bstack11l111_opy_ (u"ࠤࡵࠦᝣ")) as f:
                        bstack11l1lll1l1l_opy_ = set(line.strip() for line in f if line.strip())
                    failed_count = len(bstack11l1lll1l1l_opy_)
                except FileNotFoundError:
                    failed_count = 0
                self.logger.debug(bstack11l111_opy_ (u"ࠥࡔࡴࡲ࡬ࡦࡦࠣࡪࡦ࡯࡬ࡦࡦࠣࡸࡪࡹࡴࡴࠢࡦࡳࡺࡴࡴࠡࠪ࡯ࡳࡨࡧ࡬ࠪ࠼ࠣࡿࢂࠨᝤ").format(failed_count))
                if failed_count >= self.bstack11l1lll11ll_opy_:
                    self.logger.info(bstack11l111_opy_ (u"࡙ࠦ࡮ࡲࡦࡵ࡫ࡳࡱࡪࠠࡤࡴࡲࡷࡸ࡫ࡤࠡࠪ࡯ࡳࡨࡧ࡬ࠪ࠼ࠣࡿࢂࠦ࠾࠾ࠢࡾࢁࠧᝥ").format(failed_count, self.bstack11l1lll11ll_opy_))
                    self.bstack11l1llll111_opy_(failed_count)
                    self.bstack11l1llll1l1_opy_ = True
            return
        try:
            response = bstack11ll1l1l11l_opy_.bstack11ll11l11l1_opy_(bstack11l111_opy_ (u"ࠧࢁࡽࡀࡤࡸ࡭ࡱࡪࡎࡢ࡯ࡨࡁࢀࢃࠦࡣࡷ࡬ࡰࡩࡘࡵ࡯ࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࡂࢁࡽࠧࡲࡵࡳ࡯࡫ࡣࡵࡐࡤࡱࡪࡃࡻࡾࠤᝦ").format(self.bstack11l1lll1l11_opy_, self.config.get(bstack11l111_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡓࡧ࡭ࡦࠩᝧ")), os.environ.get(bstack11l111_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡂࡖࡋࡏࡈࡤࡘࡕࡏࡡࡌࡈࡊࡔࡔࡊࡈࡌࡉࡗ࠭ᝨ")), self.config.get(bstack11l111_opy_ (u"ࠨࡲࡵࡳ࡯࡫ࡣࡵࡐࡤࡱࡪ࠭ᝩ"))))
            if response.get(bstack11l111_opy_ (u"ࠤࡶࡸࡦࡺࡵࡴࠤᝪ")) == 200:
                failed_count = response.get(bstack11l111_opy_ (u"ࠥࡪࡦ࡯࡬ࡦࡦࡗࡩࡸࡺࡳࡄࡱࡸࡲࡹࠨᝫ"), 0)
                self.logger.debug(bstack11l111_opy_ (u"ࠦࡕࡵ࡬࡭ࡧࡧࠤ࡫ࡧࡩ࡭ࡧࡧࠤࡹ࡫ࡳࡵࡵࠣࡧࡴࡻ࡮ࡵ࠼ࠣࡿࢂࠨᝬ").format(failed_count))
                if failed_count >= self.bstack11l1lll11ll_opy_:
                    self.logger.info(bstack11l111_opy_ (u"࡚ࠧࡨࡳࡧࡶ࡬ࡴࡲࡤࠡࡥࡵࡳࡸࡹࡥࡥ࠼ࠣࡿࢂࠦ࠾࠾ࠢࡾࢁࠧ᝭").format(failed_count, self.bstack11l1lll11ll_opy_))
                    self.bstack11l1llll111_opy_(failed_count)
                    self.bstack11l1llll1l1_opy_ = True
            else:
                self.logger.error(bstack11l111_opy_ (u"ࠨࡆࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡳࡳࡱࡲࠠࡧࡣ࡬ࡰࡪࡪࠠࡵࡧࡶࡸࡸࡀࠠࡼࡿࠥᝮ").format(response))
        except Exception as e:
            self.logger.error(bstack11l111_opy_ (u"ࠢࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣࡨࡺࡸࡩ࡯ࡩࠣࡴࡴࡲ࡬ࡪࡰࡪ࠾ࠥࢁࡽࠣᝯ").format(e))
    def bstack11l1llll111_opy_(self, failed_count):
        with open(self.bstack11l1lll1ll1_opy_, bstack11l111_opy_ (u"ࠣࡹࠥᝰ")) as f:
            f.write(bstack11l111_opy_ (u"ࠤࡗ࡬ࡷ࡫ࡳࡩࡱ࡯ࡨࠥࡩࡲࡰࡵࡶࡩࡩࠦࡡࡵࠢࡾࢁࡡࡴࠢ᝱").format(datetime.now()))
            f.write(bstack11l111_opy_ (u"ࠥࡊࡦ࡯࡬ࡦࡦࠣࡸࡪࡹࡴࡴࠢࡦࡳࡺࡴࡴ࠻ࠢࡾࢁࡡࡴࠢᝲ").format(failed_count))
        self.logger.debug(bstack11l111_opy_ (u"ࠦࡆࡨ࡯ࡳࡶࠣࡆࡺ࡯࡬ࡥࠢࡩ࡭ࡱ࡫ࠠࡤࡴࡨࡥࡹ࡫ࡤ࠻ࠢࡾࢁࠧᝳ").format(self.bstack11l1lll1ll1_opy_))
    def bstack11l1lll111l_opy_(self):
        def bstack11l1lll1lll_opy_():
            while not self.bstack11l1llll1l1_opy_:
                time.sleep(bstack11l1lll11l1_opy_)
                self.bstack11l1lllll11_opy_()
                self.bstack11ll11l11l1_opy_()
        bstack11ll111111l_opy_ = threading.Thread(target=bstack11l1lll1lll_opy_, daemon=True)
        bstack11ll111111l_opy_.start()