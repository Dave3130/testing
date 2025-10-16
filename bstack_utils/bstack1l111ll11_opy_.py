# coding: UTF-8
import sys
bstack1llllll_opy_ = sys.version_info [0] == 2
bstack11l1l1l_opy_ = 2048
bstack1111ll_opy_ = 7
def bstack1lllll1_opy_ (bstack1l1_opy_):
    global bstack111ll11_opy_
    bstackl_opy_ = ord (bstack1l1_opy_ [-1])
    bstack1l1l_opy_ = bstack1l1_opy_ [:-1]
    bstack111ll_opy_ = bstackl_opy_ % len (bstack1l1l_opy_)
    bstack111l_opy_ = bstack1l1l_opy_ [:bstack111ll_opy_] + bstack1l1l_opy_ [bstack111ll_opy_:]
    if bstack1llllll_opy_:
        bstack1lll1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack11l1l1l_opy_ - (bstack11ll11_opy_ + bstackl_opy_) % bstack1111ll_opy_) for bstack11ll11_opy_, char in enumerate (bstack111l_opy_)])
    else:
        bstack1lll1ll_opy_ = str () .join ([chr (ord (char) - bstack11l1l1l_opy_ - (bstack11ll11_opy_ + bstackl_opy_) % bstack1111ll_opy_) for bstack11ll11_opy_, char in enumerate (bstack111l_opy_)])
    return eval (bstack1lll1ll_opy_)
import threading
import tempfile
import os
import time
from datetime import datetime
from bstack_utils.bstack11lll11l111_opy_ import bstack11lll111111_opy_
from bstack_utils.constants import bstack11lll11lll1_opy_, bstack11l11ll111_opy_
from bstack_utils.bstack1111l1l1_opy_ import bstack11l111ll_opy_
from bstack_utils import bstack1ll11111l1_opy_
bstack11ll1111l1l_opy_ = 10
class bstack1lll1lll1l_opy_:
    def __init__(self, bstack11ll111l1l_opy_, config, bstack11ll111111l_opy_=0):
        self.bstack11ll111l1ll_opy_ = set()
        self.lock = threading.Lock()
        self.bstack11l1lllllll_opy_ = bstack1lllll1_opy_ (u"ࠣࡽࢀ࠳ࡹ࡫ࡳࡵࡱࡵࡧ࡭࡫ࡳࡵࡴࡤࡸ࡮ࡵ࡮࠰ࡣࡳ࡭࠴ࡼ࠱࠰ࡨࡤ࡭ࡱ࡫ࡤ࠮ࡶࡨࡷࡹࡹࠢᜪ").format(bstack11lll11lll1_opy_)
        self.bstack11l1llll1ll_opy_ = os.path.join(tempfile.gettempdir(), bstack1lllll1_opy_ (u"ࠤࡤࡦࡴࡸࡴࡠࡤࡸ࡭ࡱࡪ࡟ࡼࡿࠥᜫ").format(os.environ.get(bstack1lllll1_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚ࡈࡖࡄࡢ࡙࡚ࡏࡄࠨᜬ"))))
        self.bstack11l1lllll11_opy_ = os.path.join(tempfile.gettempdir(), bstack1lllll1_opy_ (u"ࠦ࡫ࡧࡩ࡭ࡧࡧࡣࡹ࡫ࡳࡵࡵࡢࡿࢂ࠴ࡴࡹࡶࠥᜭ").format(os.environ.get(bstack1lllll1_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡊࡘࡆࡤ࡛ࡕࡊࡆࠪᜮ"))))
        self.bstack11ll111l11l_opy_ = 2
        self.bstack11ll111l1l_opy_ = bstack11ll111l1l_opy_
        self.config = config
        self.logger = bstack1ll11111l1_opy_.get_logger(__name__, bstack11l11ll111_opy_)
        self.bstack11ll111111l_opy_ = bstack11ll111111l_opy_
        self.bstack11l1llll1l1_opy_ = False
        self.bstack11ll111ll11_opy_ = not (
                            os.environ.get(bstack1lllll1_opy_ (u"ࠨࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡈࡕࡊࡎࡇࡣࡗ࡛ࡎࡠࡋࡇࡉࡓ࡚ࡉࡇࡋࡈࡖࠧᜯ")) and
                            os.environ.get(bstack1lllll1_opy_ (u"ࠢࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡎࡐࡆࡈࡣࡎࡔࡄࡆ࡚ࠥᜰ")) and
                            os.environ.get(bstack1lllll1_opy_ (u"ࠣࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡑࡗࡅࡑࡥࡎࡐࡆࡈࡣࡈࡕࡕࡏࡖࠥᜱ"))
                        )
        if bstack11l111ll_opy_.bstack11ll1111ll1_opy_(config):
            self.bstack11ll111l11l_opy_ = bstack11l111ll_opy_.bstack11ll111l111_opy_(config, self.bstack11ll111111l_opy_)
            self.bstack11ll111l1l1_opy_()
    def bstack11ll1111l11_opy_(self):
        return bstack1lllll1_opy_ (u"ࠤࡾࢁࡤࢁࡽࠣᜲ").format(self.config.get(bstack1lllll1_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡐࡤࡱࡪ࠭ᜳ")), os.environ.get(bstack1lllll1_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡆ࡚ࡏࡌࡅࡡࡕ࡙ࡓࡥࡉࡅࡇࡑࡘࡎࡌࡉࡆࡔ᜴ࠪ")))
    def bstack11l1llllll1_opy_(self):
        try:
            if self.bstack11ll111ll11_opy_:
                return
            with self.lock:
                try:
                    with open(self.bstack11l1lllll11_opy_, bstack1lllll1_opy_ (u"ࠧࡸࠢ᜵")) as f:
                        bstack11ll11111ll_opy_ = set(line.strip() for line in f if line.strip())
                except FileNotFoundError:
                    bstack11ll11111ll_opy_ = set()
                bstack11ll11111l1_opy_ = bstack11ll11111ll_opy_ - self.bstack11ll111l1ll_opy_
                if not bstack11ll11111l1_opy_:
                    return
                self.bstack11ll111l1ll_opy_.update(bstack11ll11111l1_opy_)
                data = {bstack1lllll1_opy_ (u"ࠨࡦࡢ࡫࡯ࡩࡩ࡚ࡥࡴࡶࡶࠦ᜶"): list(self.bstack11ll111l1ll_opy_), bstack1lllll1_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡔࡡ࡮ࡧࠥ᜷"): self.config.get(bstack1lllll1_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡎࡢ࡯ࡨࠫ᜸")), bstack1lllll1_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡓࡷࡱࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠢ᜹"): os.environ.get(bstack1lllll1_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡅ࡙ࡎࡒࡄࡠࡔࡘࡒࡤࡏࡄࡆࡐࡗࡍࡋࡏࡅࡓࠩ᜺")), bstack1lllll1_opy_ (u"ࠦࡵࡸ࡯࡫ࡧࡦࡸࡓࡧ࡭ࡦࠤ᜻"): self.config.get(bstack1lllll1_opy_ (u"ࠬࡶࡲࡰ࡬ࡨࡧࡹࡔࡡ࡮ࡧࠪ᜼"))}
            response = bstack11lll111111_opy_.bstack11ll11lll1l_opy_(self.bstack11l1lllllll_opy_, data)
            if response.get(bstack1lllll1_opy_ (u"ࠨࡳࡵࡣࡷࡹࡸࠨ᜽")) == 200:
                self.logger.debug(bstack1lllll1_opy_ (u"ࠢࡔࡷࡦࡧࡪࡹࡳࡧࡷ࡯ࡰࡾࠦࡳࡦࡰࡷࠤ࡫ࡧࡩ࡭ࡧࡧࠤࡹ࡫ࡳࡵࡵ࠽ࠤࢀࢃࠢ᜾").format(data))
            else:
                self.logger.debug(bstack1lllll1_opy_ (u"ࠣࡈࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤࡸ࡫࡮ࡥࠢࡩࡥ࡮ࡲࡥࡥࠢࡷࡩࡸࡺࡳ࠻ࠢࡾࢁࠧ᜿").format(response))
        except Exception as e:
            self.logger.debug(bstack1lllll1_opy_ (u"ࠤࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥࡪࡵࡳ࡫ࡱ࡫ࠥࡹࡥ࡯ࡦ࡬ࡲ࡬ࠦࡦࡢ࡫࡯ࡩࡩࠦࡴࡦࡵࡷࡷ࠿ࠦࡻࡾࠤᝀ").format(e))
    def bstack11ll11lllll_opy_(self):
        if self.bstack11ll111ll11_opy_:
            with self.lock:
                try:
                    with open(self.bstack11l1lllll11_opy_, bstack1lllll1_opy_ (u"ࠥࡶࠧᝁ")) as f:
                        bstack11l1llll11l_opy_ = set(line.strip() for line in f if line.strip())
                    failed_count = len(bstack11l1llll11l_opy_)
                except FileNotFoundError:
                    failed_count = 0
                self.logger.debug(bstack1lllll1_opy_ (u"ࠦࡕࡵ࡬࡭ࡧࡧࠤ࡫ࡧࡩ࡭ࡧࡧࠤࡹ࡫ࡳࡵࡵࠣࡧࡴࡻ࡮ࡵࠢࠫࡰࡴࡩࡡ࡭ࠫ࠽ࠤࢀࢃࠢᝂ").format(failed_count))
                if failed_count >= self.bstack11ll111l11l_opy_:
                    self.logger.info(bstack1lllll1_opy_ (u"࡚ࠧࡨࡳࡧࡶ࡬ࡴࡲࡤࠡࡥࡵࡳࡸࡹࡥࡥࠢࠫࡰࡴࡩࡡ࡭ࠫ࠽ࠤࢀࢃࠠ࠿࠿ࠣࡿࢂࠨᝃ").format(failed_count, self.bstack11ll111l11l_opy_))
                    self.bstack11ll1111lll_opy_(failed_count)
                    self.bstack11l1llll1l1_opy_ = True
            return
        try:
            response = bstack11lll111111_opy_.bstack11ll11lllll_opy_(bstack1lllll1_opy_ (u"ࠨࡻࡾࡁࡥࡹ࡮ࡲࡤࡏࡣࡰࡩࡂࢁࡽࠧࡤࡸ࡭ࡱࡪࡒࡶࡰࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷࡃࡻࡾࠨࡳࡶࡴࡰࡥࡤࡶࡑࡥࡲ࡫࠽ࡼࡿࠥᝄ").format(self.bstack11l1lllllll_opy_, self.config.get(bstack1lllll1_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡔࡡ࡮ࡧࠪᝅ")), os.environ.get(bstack1lllll1_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡃࡗࡌࡐࡉࡥࡒࡖࡐࡢࡍࡉࡋࡎࡕࡋࡉࡍࡊࡘࠧᝆ")), self.config.get(bstack1lllll1_opy_ (u"ࠩࡳࡶࡴࡰࡥࡤࡶࡑࡥࡲ࡫ࠧᝇ"))))
            if response.get(bstack1lllll1_opy_ (u"ࠥࡷࡹࡧࡴࡶࡵࠥᝈ")) == 200:
                failed_count = response.get(bstack1lllll1_opy_ (u"ࠦ࡫ࡧࡩ࡭ࡧࡧࡘࡪࡹࡴࡴࡅࡲࡹࡳࡺࠢᝉ"), 0)
                self.logger.debug(bstack1lllll1_opy_ (u"ࠧࡖ࡯࡭࡮ࡨࡨࠥ࡬ࡡࡪ࡮ࡨࡨࠥࡺࡥࡴࡶࡶࠤࡨࡵࡵ࡯ࡶ࠽ࠤࢀࢃࠢᝊ").format(failed_count))
                if failed_count >= self.bstack11ll111l11l_opy_:
                    self.logger.info(bstack1lllll1_opy_ (u"ࠨࡔࡩࡴࡨࡷ࡭ࡵ࡬ࡥࠢࡦࡶࡴࡹࡳࡦࡦ࠽ࠤࢀࢃࠠ࠿࠿ࠣࡿࢂࠨᝋ").format(failed_count, self.bstack11ll111l11l_opy_))
                    self.bstack11ll1111lll_opy_(failed_count)
                    self.bstack11l1llll1l1_opy_ = True
            else:
                self.logger.error(bstack1lllll1_opy_ (u"ࠢࡇࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡴࡴࡲ࡬ࠡࡨࡤ࡭ࡱ࡫ࡤࠡࡶࡨࡷࡹࡹ࠺ࠡࡽࢀࠦᝌ").format(response))
        except Exception as e:
            self.logger.error(bstack1lllll1_opy_ (u"ࠣࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤࡩࡻࡲࡪࡰࡪࠤࡵࡵ࡬࡭࡫ࡱ࡫࠿ࠦࡻࡾࠤᝍ").format(e))
    def bstack11ll1111lll_opy_(self, failed_count):
        with open(self.bstack11l1llll1ll_opy_, bstack1lllll1_opy_ (u"ࠤࡺࠦᝎ")) as f:
            f.write(bstack1lllll1_opy_ (u"ࠥࡘ࡭ࡸࡥࡴࡪࡲࡰࡩࠦࡣࡳࡱࡶࡷࡪࡪࠠࡢࡶࠣࡿࢂࡢ࡮ࠣᝏ").format(datetime.now()))
            f.write(bstack1lllll1_opy_ (u"ࠦࡋࡧࡩ࡭ࡧࡧࠤࡹ࡫ࡳࡵࡵࠣࡧࡴࡻ࡮ࡵ࠼ࠣࡿࢂࡢ࡮ࠣᝐ").format(failed_count))
        self.logger.debug(bstack1lllll1_opy_ (u"ࠧࡇࡢࡰࡴࡷࠤࡇࡻࡩ࡭ࡦࠣࡪ࡮ࡲࡥࠡࡥࡵࡩࡦࡺࡥࡥ࠼ࠣࡿࢂࠨᝑ").format(self.bstack11l1llll1ll_opy_))
    def bstack11ll111l1l1_opy_(self):
        def bstack11ll1111111_opy_():
            while not self.bstack11l1llll1l1_opy_:
                time.sleep(bstack11ll1111l1l_opy_)
                self.bstack11l1llllll1_opy_()
                self.bstack11ll11lllll_opy_()
        bstack11l1lllll1l_opy_ = threading.Thread(target=bstack11ll1111111_opy_, daemon=True)
        bstack11l1lllll1l_opy_.start()