# coding: UTF-8
import sys
bstack1lllll1_opy_ = sys.version_info [0] == 2
bstack11lll1l_opy_ = 2048
bstack1lll1l_opy_ = 7
def bstack11l11l1_opy_ (bstack111l1ll_opy_):
    global bstack1ll1l_opy_
    bstack1l1l1ll_opy_ = ord (bstack111l1ll_opy_ [-1])
    bstack1l11l_opy_ = bstack111l1ll_opy_ [:-1]
    bstack1lllll1l_opy_ = bstack1l1l1ll_opy_ % len (bstack1l11l_opy_)
    bstack11ll1l1_opy_ = bstack1l11l_opy_ [:bstack1lllll1l_opy_] + bstack1l11l_opy_ [bstack1lllll1l_opy_:]
    if bstack1lllll1_opy_:
        bstack1lll_opy_ = unicode () .join ([unichr (ord (char) - bstack11lll1l_opy_ - (bstack1l1ll11_opy_ + bstack1l1l1ll_opy_) % bstack1lll1l_opy_) for bstack1l1ll11_opy_, char in enumerate (bstack11ll1l1_opy_)])
    else:
        bstack1lll_opy_ = str () .join ([chr (ord (char) - bstack11lll1l_opy_ - (bstack1l1ll11_opy_ + bstack1l1l1ll_opy_) % bstack1lll1l_opy_) for bstack1l1ll11_opy_, char in enumerate (bstack11ll1l1_opy_)])
    return eval (bstack1lll_opy_)
import threading
import tempfile
import os
import time
from datetime import datetime
from bstack_utils.bstack11ll1llllll_opy_ import bstack11ll1llll11_opy_
from bstack_utils.constants import bstack11ll1ll1ll1_opy_, bstack11l1l11ll1_opy_
from bstack_utils.bstack111lll1l_opy_ import bstack1lll11ll1_opy_
from bstack_utils import bstack11111l1l1_opy_
bstack11l1lll1ll1_opy_ = 10
class bstack1llllll111_opy_:
    def __init__(self, bstack1l11lllll_opy_, config, bstack11l1llll11l_opy_=0):
        self.bstack11ll11111ll_opy_ = set()
        self.lock = threading.Lock()
        self.bstack11l1lll11ll_opy_ = bstack11l11l1_opy_ (u"ࠣࡽࢀ࠳ࡹ࡫ࡳࡵࡱࡵࡧ࡭࡫ࡳࡵࡴࡤࡸ࡮ࡵ࡮࠰ࡣࡳ࡭࠴ࡼ࠱࠰ࡨࡤ࡭ࡱ࡫ࡤ࠮ࡶࡨࡷࡹࡹࠢ᜿").format(bstack11ll1ll1ll1_opy_)
        self.bstack11l1llllll1_opy_ = os.path.join(tempfile.gettempdir(), bstack11l11l1_opy_ (u"ࠤࡤࡦࡴࡸࡴࡠࡤࡸ࡭ࡱࡪ࡟ࡼࡿࠥᝀ").format(os.environ.get(bstack11l11l1_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚ࡈࡖࡄࡢ࡙࡚ࡏࡄࠨᝁ"))))
        self.bstack11l1lll1l1l_opy_ = os.path.join(tempfile.gettempdir(), bstack11l11l1_opy_ (u"ࠦ࡫ࡧࡩ࡭ࡧࡧࡣࡹ࡫ࡳࡵࡵࡢࡿࢂ࠴ࡴࡹࡶࠥᝂ").format(os.environ.get(bstack11l11l1_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡊࡘࡆࡤ࡛ࡕࡊࡆࠪᝃ"))))
        self.bstack11l1lllllll_opy_ = 2
        self.bstack1l11lllll_opy_ = bstack1l11lllll_opy_
        self.config = config
        self.logger = bstack11111l1l1_opy_.get_logger(__name__, bstack11l1l11ll1_opy_)
        self.bstack11l1llll11l_opy_ = bstack11l1llll11l_opy_
        self.bstack11l1lll11l1_opy_ = False
        self.bstack11l1lllll11_opy_ = not (
                            os.environ.get(bstack11l11l1_opy_ (u"ࠨࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡈࡕࡊࡎࡇࡣࡗ࡛ࡎࡠࡋࡇࡉࡓ࡚ࡉࡇࡋࡈࡖࠧᝄ")) and
                            os.environ.get(bstack11l11l1_opy_ (u"ࠢࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡎࡐࡆࡈࡣࡎࡔࡄࡆ࡚ࠥᝅ")) and
                            os.environ.get(bstack11l11l1_opy_ (u"ࠣࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡑࡗࡅࡑࡥࡎࡐࡆࡈࡣࡈࡕࡕࡏࡖࠥᝆ"))
                        )
        if bstack1lll11ll1_opy_.bstack11ll111111l_opy_(config):
            self.bstack11l1lllllll_opy_ = bstack1lll11ll1_opy_.bstack11l1lllll1l_opy_(config, self.bstack11l1llll11l_opy_)
            self.bstack11ll1111111_opy_()
    def bstack11l1llll1ll_opy_(self):
        return bstack11l11l1_opy_ (u"ࠤࡾࢁࡤࢁࡽࠣᝇ").format(self.config.get(bstack11l11l1_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡐࡤࡱࡪ࠭ᝈ")), os.environ.get(bstack11l11l1_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡆ࡚ࡏࡌࡅࡡࡕ࡙ࡓࡥࡉࡅࡇࡑࡘࡎࡌࡉࡆࡔࠪᝉ")))
    def bstack11l1lll1111_opy_(self):
        try:
            if self.bstack11l1lllll11_opy_:
                return
            with self.lock:
                try:
                    with open(self.bstack11l1lll1l1l_opy_, bstack11l11l1_opy_ (u"ࠧࡸࠢᝊ")) as f:
                        bstack11l1lll1lll_opy_ = set(line.strip() for line in f if line.strip())
                except FileNotFoundError:
                    bstack11l1lll1lll_opy_ = set()
                bstack11l1llll111_opy_ = bstack11l1lll1lll_opy_ - self.bstack11ll11111ll_opy_
                if not bstack11l1llll111_opy_:
                    return
                self.bstack11ll11111ll_opy_.update(bstack11l1llll111_opy_)
                data = {bstack11l11l1_opy_ (u"ࠨࡦࡢ࡫࡯ࡩࡩ࡚ࡥࡴࡶࡶࠦᝋ"): list(self.bstack11ll11111ll_opy_), bstack11l11l1_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡔࡡ࡮ࡧࠥᝌ"): self.config.get(bstack11l11l1_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡎࡢ࡯ࡨࠫᝍ")), bstack11l11l1_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡓࡷࡱࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠢᝎ"): os.environ.get(bstack11l11l1_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡅ࡙ࡎࡒࡄࡠࡔࡘࡒࡤࡏࡄࡆࡐࡗࡍࡋࡏࡅࡓࠩᝏ")), bstack11l11l1_opy_ (u"ࠦࡵࡸ࡯࡫ࡧࡦࡸࡓࡧ࡭ࡦࠤᝐ"): self.config.get(bstack11l11l1_opy_ (u"ࠬࡶࡲࡰ࡬ࡨࡧࡹࡔࡡ࡮ࡧࠪᝑ"))}
            response = bstack11ll1llll11_opy_.bstack11ll111l1ll_opy_(self.bstack11l1lll11ll_opy_, data)
            if response.get(bstack11l11l1_opy_ (u"ࠨࡳࡵࡣࡷࡹࡸࠨᝒ")) == 200:
                self.logger.debug(bstack11l11l1_opy_ (u"ࠢࡔࡷࡦࡧࡪࡹࡳࡧࡷ࡯ࡰࡾࠦࡳࡦࡰࡷࠤ࡫ࡧࡩ࡭ࡧࡧࠤࡹ࡫ࡳࡵࡵ࠽ࠤࢀࢃࠢᝓ").format(data))
            else:
                self.logger.debug(bstack11l11l1_opy_ (u"ࠣࡈࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤࡸ࡫࡮ࡥࠢࡩࡥ࡮ࡲࡥࡥࠢࡷࡩࡸࡺࡳ࠻ࠢࡾࢁࠧ᝔").format(response))
        except Exception as e:
            self.logger.debug(bstack11l11l1_opy_ (u"ࠤࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥࡪࡵࡳ࡫ࡱ࡫ࠥࡹࡥ࡯ࡦ࡬ࡲ࡬ࠦࡦࡢ࡫࡯ࡩࡩࠦࡴࡦࡵࡷࡷ࠿ࠦࡻࡾࠤ᝕").format(e))
    def bstack11ll11l111l_opy_(self):
        if self.bstack11l1lllll11_opy_:
            with self.lock:
                try:
                    with open(self.bstack11l1lll1l1l_opy_, bstack11l11l1_opy_ (u"ࠥࡶࠧ᝖")) as f:
                        bstack11ll11111l1_opy_ = set(line.strip() for line in f if line.strip())
                    failed_count = len(bstack11ll11111l1_opy_)
                except FileNotFoundError:
                    failed_count = 0
                self.logger.debug(bstack11l11l1_opy_ (u"ࠦࡕࡵ࡬࡭ࡧࡧࠤ࡫ࡧࡩ࡭ࡧࡧࠤࡹ࡫ࡳࡵࡵࠣࡧࡴࡻ࡮ࡵࠢࠫࡰࡴࡩࡡ࡭ࠫ࠽ࠤࢀࢃࠢ᝗").format(failed_count))
                if failed_count >= self.bstack11l1lllllll_opy_:
                    self.logger.info(bstack11l11l1_opy_ (u"࡚ࠧࡨࡳࡧࡶ࡬ࡴࡲࡤࠡࡥࡵࡳࡸࡹࡥࡥࠢࠫࡰࡴࡩࡡ࡭ࠫ࠽ࠤࢀࢃࠠ࠿࠿ࠣࡿࢂࠨ᝘").format(failed_count, self.bstack11l1lllllll_opy_))
                    self.bstack11l1lll1l11_opy_(failed_count)
                    self.bstack11l1lll11l1_opy_ = True
            return
        try:
            response = bstack11ll1llll11_opy_.bstack11ll11l111l_opy_(bstack11l11l1_opy_ (u"ࠨࡻࡾࡁࡥࡹ࡮ࡲࡤࡏࡣࡰࡩࡂࢁࡽࠧࡤࡸ࡭ࡱࡪࡒࡶࡰࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷࡃࡻࡾࠨࡳࡶࡴࡰࡥࡤࡶࡑࡥࡲ࡫࠽ࡼࡿࠥ᝙").format(self.bstack11l1lll11ll_opy_, self.config.get(bstack11l11l1_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡔࡡ࡮ࡧࠪ᝚")), os.environ.get(bstack11l11l1_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡃࡗࡌࡐࡉࡥࡒࡖࡐࡢࡍࡉࡋࡎࡕࡋࡉࡍࡊࡘࠧ᝛")), self.config.get(bstack11l11l1_opy_ (u"ࠩࡳࡶࡴࡰࡥࡤࡶࡑࡥࡲ࡫ࠧ᝜"))))
            if response.get(bstack11l11l1_opy_ (u"ࠥࡷࡹࡧࡴࡶࡵࠥ᝝")) == 200:
                failed_count = response.get(bstack11l11l1_opy_ (u"ࠦ࡫ࡧࡩ࡭ࡧࡧࡘࡪࡹࡴࡴࡅࡲࡹࡳࡺࠢ᝞"), 0)
                self.logger.debug(bstack11l11l1_opy_ (u"ࠧࡖ࡯࡭࡮ࡨࡨࠥ࡬ࡡࡪ࡮ࡨࡨࠥࡺࡥࡴࡶࡶࠤࡨࡵࡵ࡯ࡶ࠽ࠤࢀࢃࠢ᝟").format(failed_count))
                if failed_count >= self.bstack11l1lllllll_opy_:
                    self.logger.info(bstack11l11l1_opy_ (u"ࠨࡔࡩࡴࡨࡷ࡭ࡵ࡬ࡥࠢࡦࡶࡴࡹࡳࡦࡦ࠽ࠤࢀࢃࠠ࠿࠿ࠣࡿࢂࠨᝠ").format(failed_count, self.bstack11l1lllllll_opy_))
                    self.bstack11l1lll1l11_opy_(failed_count)
                    self.bstack11l1lll11l1_opy_ = True
            else:
                self.logger.error(bstack11l11l1_opy_ (u"ࠢࡇࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡴࡴࡲ࡬ࠡࡨࡤ࡭ࡱ࡫ࡤࠡࡶࡨࡷࡹࡹ࠺ࠡࡽࢀࠦᝡ").format(response))
        except Exception as e:
            self.logger.error(bstack11l11l1_opy_ (u"ࠣࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤࡩࡻࡲࡪࡰࡪࠤࡵࡵ࡬࡭࡫ࡱ࡫࠿ࠦࡻࡾࠤᝢ").format(e))
    def bstack11l1lll1l11_opy_(self, failed_count):
        with open(self.bstack11l1llllll1_opy_, bstack11l11l1_opy_ (u"ࠤࡺࠦᝣ")) as f:
            f.write(bstack11l11l1_opy_ (u"ࠥࡘ࡭ࡸࡥࡴࡪࡲࡰࡩࠦࡣࡳࡱࡶࡷࡪࡪࠠࡢࡶࠣࡿࢂࡢ࡮ࠣᝤ").format(datetime.now()))
            f.write(bstack11l11l1_opy_ (u"ࠦࡋࡧࡩ࡭ࡧࡧࠤࡹ࡫ࡳࡵࡵࠣࡧࡴࡻ࡮ࡵ࠼ࠣࡿࢂࡢ࡮ࠣᝥ").format(failed_count))
        self.logger.debug(bstack11l11l1_opy_ (u"ࠧࡇࡢࡰࡴࡷࠤࡇࡻࡩ࡭ࡦࠣࡪ࡮ࡲࡥࠡࡥࡵࡩࡦࡺࡥࡥ࠼ࠣࡿࢂࠨᝦ").format(self.bstack11l1llllll1_opy_))
    def bstack11ll1111111_opy_(self):
        def bstack11l1lll111l_opy_():
            while not self.bstack11l1lll11l1_opy_:
                time.sleep(bstack11l1lll1ll1_opy_)
                self.bstack11l1lll1111_opy_()
                self.bstack11ll11l111l_opy_()
        bstack11l1llll1l1_opy_ = threading.Thread(target=bstack11l1lll111l_opy_, daemon=True)
        bstack11l1llll1l1_opy_.start()