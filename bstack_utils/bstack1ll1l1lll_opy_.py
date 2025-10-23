# coding: UTF-8
import sys
bstack111lll1_opy_ = sys.version_info [0] == 2
bstack11l1l1_opy_ = 2048
bstack11lllll_opy_ = 7
def bstack11lll1_opy_ (bstack111lll_opy_):
    global bstack11ll1l_opy_
    bstack11l11l1_opy_ = ord (bstack111lll_opy_ [-1])
    bstack1l1l_opy_ = bstack111lll_opy_ [:-1]
    bstack1l11l1_opy_ = bstack11l11l1_opy_ % len (bstack1l1l_opy_)
    bstack1lll1l_opy_ = bstack1l1l_opy_ [:bstack1l11l1_opy_] + bstack1l1l_opy_ [bstack1l11l1_opy_:]
    if bstack111lll1_opy_:
        bstack1111lll_opy_ = unicode () .join ([unichr (ord (char) - bstack11l1l1_opy_ - (bstack1ll1ll1_opy_ + bstack11l11l1_opy_) % bstack11lllll_opy_) for bstack1ll1ll1_opy_, char in enumerate (bstack1lll1l_opy_)])
    else:
        bstack1111lll_opy_ = str () .join ([chr (ord (char) - bstack11l1l1_opy_ - (bstack1ll1ll1_opy_ + bstack11l11l1_opy_) % bstack11lllll_opy_) for bstack1ll1ll1_opy_, char in enumerate (bstack1lll1l_opy_)])
    return eval (bstack1111lll_opy_)
import threading
import tempfile
import os
import time
from datetime import datetime
from bstack_utils.bstack11lll111111_opy_ import bstack11ll1l1ll1l_opy_
from bstack_utils.constants import bstack11ll1ll1l11_opy_, bstack1ll11l1lll_opy_
from bstack_utils.bstack1lll1l1l1_opy_ import bstack11111lll_opy_
from bstack_utils import bstack1l1l1llll1_opy_
bstack11l1lll11ll_opy_ = 10
class bstack11lll1l1l1_opy_:
    def __init__(self, bstack1ll11lll1l_opy_, config, bstack11l1lllllll_opy_=0):
        self.bstack11l1lll11l1_opy_ = set()
        self.lock = threading.Lock()
        self.bstack11l1ll1llll_opy_ = bstack11lll1_opy_ (u"ࠣࡽࢀ࠳ࡹ࡫ࡳࡵࡱࡵࡧ࡭࡫ࡳࡵࡴࡤࡸ࡮ࡵ࡮࠰ࡣࡳ࡭࠴ࡼ࠱࠰ࡨࡤ࡭ࡱ࡫ࡤ࠮ࡶࡨࡷࡹࡹࠢᝆ").format(bstack11ll1ll1l11_opy_)
        self.bstack11l1ll1ll1l_opy_ = os.path.join(tempfile.gettempdir(), bstack11lll1_opy_ (u"ࠤࡤࡦࡴࡸࡴࡠࡤࡸ࡭ࡱࡪ࡟ࡼࡿࠥᝇ").format(os.environ.get(bstack11lll1_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚ࡈࡖࡄࡢ࡙࡚ࡏࡄࠨᝈ"))))
        self.bstack11l1lll1lll_opy_ = os.path.join(tempfile.gettempdir(), bstack11lll1_opy_ (u"ࠦ࡫ࡧࡩ࡭ࡧࡧࡣࡹ࡫ࡳࡵࡵࡢࡿࢂ࠴ࡴࡹࡶࠥᝉ").format(os.environ.get(bstack11lll1_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡊࡘࡆࡤ࡛ࡕࡊࡆࠪᝊ"))))
        self.bstack11l1lll1111_opy_ = 2
        self.bstack1ll11lll1l_opy_ = bstack1ll11lll1l_opy_
        self.config = config
        self.logger = bstack1l1l1llll1_opy_.get_logger(__name__, bstack1ll11l1lll_opy_)
        self.bstack11l1lllllll_opy_ = bstack11l1lllllll_opy_
        self.bstack11l1lll1l11_opy_ = False
        self.bstack11l1llll11l_opy_ = not (
                            os.environ.get(bstack11lll1_opy_ (u"ࠨࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡈࡕࡊࡎࡇࡣࡗ࡛ࡎࡠࡋࡇࡉࡓ࡚ࡉࡇࡋࡈࡖࠧᝋ")) and
                            os.environ.get(bstack11lll1_opy_ (u"ࠢࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡎࡐࡆࡈࡣࡎࡔࡄࡆ࡚ࠥᝌ")) and
                            os.environ.get(bstack11lll1_opy_ (u"ࠣࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡑࡗࡅࡑࡥࡎࡐࡆࡈࡣࡈࡕࡕࡏࡖࠥᝍ"))
                        )
        if bstack11111lll_opy_.bstack11l1llll1l1_opy_(config):
            self.bstack11l1lll1111_opy_ = bstack11111lll_opy_.bstack11l1lllll1l_opy_(config, self.bstack11l1lllllll_opy_)
            self.bstack11l1lll1ll1_opy_()
    def bstack11l1lll111l_opy_(self):
        return bstack11lll1_opy_ (u"ࠤࡾࢁࡤࢁࡽࠣᝎ").format(self.config.get(bstack11lll1_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡐࡤࡱࡪ࠭ᝏ")), os.environ.get(bstack11lll1_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡆ࡚ࡏࡌࡅࡡࡕ࡙ࡓࡥࡉࡅࡇࡑࡘࡎࡌࡉࡆࡔࠪᝐ")))
    def bstack11l1llll111_opy_(self):
        try:
            if self.bstack11l1llll11l_opy_:
                return
            with self.lock:
                try:
                    with open(self.bstack11l1lll1lll_opy_, bstack11lll1_opy_ (u"ࠧࡸࠢᝑ")) as f:
                        bstack11l1llllll1_opy_ = set(line.strip() for line in f if line.strip())
                except FileNotFoundError:
                    bstack11l1llllll1_opy_ = set()
                bstack11l1ll1lll1_opy_ = bstack11l1llllll1_opy_ - self.bstack11l1lll11l1_opy_
                if not bstack11l1ll1lll1_opy_:
                    return
                self.bstack11l1lll11l1_opy_.update(bstack11l1ll1lll1_opy_)
                data = {bstack11lll1_opy_ (u"ࠨࡦࡢ࡫࡯ࡩࡩ࡚ࡥࡴࡶࡶࠦᝒ"): list(self.bstack11l1lll11l1_opy_), bstack11lll1_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡔࡡ࡮ࡧࠥᝓ"): self.config.get(bstack11lll1_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡎࡢ࡯ࡨࠫ᝔")), bstack11lll1_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡓࡷࡱࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠢ᝕"): os.environ.get(bstack11lll1_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡅ࡙ࡎࡒࡄࡠࡔࡘࡒࡤࡏࡄࡆࡐࡗࡍࡋࡏࡅࡓࠩ᝖")), bstack11lll1_opy_ (u"ࠦࡵࡸ࡯࡫ࡧࡦࡸࡓࡧ࡭ࡦࠤ᝗"): self.config.get(bstack11lll1_opy_ (u"ࠬࡶࡲࡰ࡬ࡨࡧࡹࡔࡡ࡮ࡧࠪ᝘"))}
            response = bstack11ll1l1ll1l_opy_.bstack11ll11l111l_opy_(self.bstack11l1ll1llll_opy_, data)
            if response.get(bstack11lll1_opy_ (u"ࠨࡳࡵࡣࡷࡹࡸࠨ᝙")) == 200:
                self.logger.debug(bstack11lll1_opy_ (u"ࠢࡔࡷࡦࡧࡪࡹࡳࡧࡷ࡯ࡰࡾࠦࡳࡦࡰࡷࠤ࡫ࡧࡩ࡭ࡧࡧࠤࡹ࡫ࡳࡵࡵ࠽ࠤࢀࢃࠢ᝚").format(data))
            else:
                self.logger.debug(bstack11lll1_opy_ (u"ࠣࡈࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤࡸ࡫࡮ࡥࠢࡩࡥ࡮ࡲࡥࡥࠢࡷࡩࡸࡺࡳ࠻ࠢࡾࢁࠧ᝛").format(response))
        except Exception as e:
            self.logger.debug(bstack11lll1_opy_ (u"ࠤࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥࡪࡵࡳ࡫ࡱ࡫ࠥࡹࡥ࡯ࡦ࡬ࡲ࡬ࠦࡦࡢ࡫࡯ࡩࡩࠦࡴࡦࡵࡷࡷ࠿ࠦࡻࡾࠤ᝜").format(e))
    def bstack11ll111llll_opy_(self):
        if self.bstack11l1llll11l_opy_:
            with self.lock:
                try:
                    with open(self.bstack11l1lll1lll_opy_, bstack11lll1_opy_ (u"ࠥࡶࠧ᝝")) as f:
                        bstack11ll1111111_opy_ = set(line.strip() for line in f if line.strip())
                    failed_count = len(bstack11ll1111111_opy_)
                except FileNotFoundError:
                    failed_count = 0
                self.logger.debug(bstack11lll1_opy_ (u"ࠦࡕࡵ࡬࡭ࡧࡧࠤ࡫ࡧࡩ࡭ࡧࡧࠤࡹ࡫ࡳࡵࡵࠣࡧࡴࡻ࡮ࡵࠢࠫࡰࡴࡩࡡ࡭ࠫ࠽ࠤࢀࢃࠢ᝞").format(failed_count))
                if failed_count >= self.bstack11l1lll1111_opy_:
                    self.logger.info(bstack11lll1_opy_ (u"࡚ࠧࡨࡳࡧࡶ࡬ࡴࡲࡤࠡࡥࡵࡳࡸࡹࡥࡥࠢࠫࡰࡴࡩࡡ࡭ࠫ࠽ࠤࢀࢃࠠ࠿࠿ࠣࡿࢂࠨ᝟").format(failed_count, self.bstack11l1lll1111_opy_))
                    self.bstack11l1lllll11_opy_(failed_count)
                    self.bstack11l1lll1l11_opy_ = True
            return
        try:
            response = bstack11ll1l1ll1l_opy_.bstack11ll111llll_opy_(bstack11lll1_opy_ (u"ࠨࡻࡾࡁࡥࡹ࡮ࡲࡤࡏࡣࡰࡩࡂࢁࡽࠧࡤࡸ࡭ࡱࡪࡒࡶࡰࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷࡃࡻࡾࠨࡳࡶࡴࡰࡥࡤࡶࡑࡥࡲ࡫࠽ࡼࡿࠥᝠ").format(self.bstack11l1ll1llll_opy_, self.config.get(bstack11lll1_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡔࡡ࡮ࡧࠪᝡ")), os.environ.get(bstack11lll1_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡃࡗࡌࡐࡉࡥࡒࡖࡐࡢࡍࡉࡋࡎࡕࡋࡉࡍࡊࡘࠧᝢ")), self.config.get(bstack11lll1_opy_ (u"ࠩࡳࡶࡴࡰࡥࡤࡶࡑࡥࡲ࡫ࠧᝣ"))))
            if response.get(bstack11lll1_opy_ (u"ࠥࡷࡹࡧࡴࡶࡵࠥᝤ")) == 200:
                failed_count = response.get(bstack11lll1_opy_ (u"ࠦ࡫ࡧࡩ࡭ࡧࡧࡘࡪࡹࡴࡴࡅࡲࡹࡳࡺࠢᝥ"), 0)
                self.logger.debug(bstack11lll1_opy_ (u"ࠧࡖ࡯࡭࡮ࡨࡨࠥ࡬ࡡࡪ࡮ࡨࡨࠥࡺࡥࡴࡶࡶࠤࡨࡵࡵ࡯ࡶ࠽ࠤࢀࢃࠢᝦ").format(failed_count))
                if failed_count >= self.bstack11l1lll1111_opy_:
                    self.logger.info(bstack11lll1_opy_ (u"ࠨࡔࡩࡴࡨࡷ࡭ࡵ࡬ࡥࠢࡦࡶࡴࡹࡳࡦࡦ࠽ࠤࢀࢃࠠ࠿࠿ࠣࡿࢂࠨᝧ").format(failed_count, self.bstack11l1lll1111_opy_))
                    self.bstack11l1lllll11_opy_(failed_count)
                    self.bstack11l1lll1l11_opy_ = True
            else:
                self.logger.error(bstack11lll1_opy_ (u"ࠢࡇࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡴࡴࡲ࡬ࠡࡨࡤ࡭ࡱ࡫ࡤࠡࡶࡨࡷࡹࡹ࠺ࠡࡽࢀࠦᝨ").format(response))
        except Exception as e:
            self.logger.error(bstack11lll1_opy_ (u"ࠣࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤࡩࡻࡲࡪࡰࡪࠤࡵࡵ࡬࡭࡫ࡱ࡫࠿ࠦࡻࡾࠤᝩ").format(e))
    def bstack11l1lllll11_opy_(self, failed_count):
        with open(self.bstack11l1ll1ll1l_opy_, bstack11lll1_opy_ (u"ࠤࡺࠦᝪ")) as f:
            f.write(bstack11lll1_opy_ (u"ࠥࡘ࡭ࡸࡥࡴࡪࡲࡰࡩࠦࡣࡳࡱࡶࡷࡪࡪࠠࡢࡶࠣࡿࢂࡢ࡮ࠣᝫ").format(datetime.now()))
            f.write(bstack11lll1_opy_ (u"ࠦࡋࡧࡩ࡭ࡧࡧࠤࡹ࡫ࡳࡵࡵࠣࡧࡴࡻ࡮ࡵ࠼ࠣࡿࢂࡢ࡮ࠣᝬ").format(failed_count))
        self.logger.debug(bstack11lll1_opy_ (u"ࠧࡇࡢࡰࡴࡷࠤࡇࡻࡩ࡭ࡦࠣࡪ࡮ࡲࡥࠡࡥࡵࡩࡦࡺࡥࡥ࠼ࠣࡿࢂࠨ᝭").format(self.bstack11l1ll1ll1l_opy_))
    def bstack11l1lll1ll1_opy_(self):
        def bstack11l1lll1l1l_opy_():
            while not self.bstack11l1lll1l11_opy_:
                time.sleep(bstack11l1lll11ll_opy_)
                self.bstack11l1llll111_opy_()
                self.bstack11ll111llll_opy_()
        bstack11l1llll1ll_opy_ = threading.Thread(target=bstack11l1lll1l1l_opy_, daemon=True)
        bstack11l1llll1ll_opy_.start()