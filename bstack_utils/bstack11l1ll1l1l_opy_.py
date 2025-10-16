# coding: UTF-8
import sys
bstack11llll1_opy_ = sys.version_info [0] == 2
bstack11lll1l_opy_ = 2048
bstack1l1l1l1_opy_ = 7
def bstack1ll11_opy_ (bstack11l11ll_opy_):
    global bstack11l1lll_opy_
    bstack1l1l111_opy_ = ord (bstack11l11ll_opy_ [-1])
    bstack11_opy_ = bstack11l11ll_opy_ [:-1]
    bstack1l1llll_opy_ = bstack1l1l111_opy_ % len (bstack11_opy_)
    bstack11111_opy_ = bstack11_opy_ [:bstack1l1llll_opy_] + bstack11_opy_ [bstack1l1llll_opy_:]
    if bstack11llll1_opy_:
        bstack111_opy_ = unicode () .join ([unichr (ord (char) - bstack11lll1l_opy_ - (bstack1111ll1_opy_ + bstack1l1l111_opy_) % bstack1l1l1l1_opy_) for bstack1111ll1_opy_, char in enumerate (bstack11111_opy_)])
    else:
        bstack111_opy_ = str () .join ([chr (ord (char) - bstack11lll1l_opy_ - (bstack1111ll1_opy_ + bstack1l1l111_opy_) % bstack1l1l1l1_opy_) for bstack1111ll1_opy_, char in enumerate (bstack11111_opy_)])
    return eval (bstack111_opy_)
import threading
import tempfile
import os
import time
from datetime import datetime
from bstack_utils.bstack11lll1111ll_opy_ import bstack11ll1llllll_opy_
from bstack_utils.constants import bstack11lll11l1ll_opy_, bstack111lll1l1l_opy_
from bstack_utils.bstack1lll1ll1l_opy_ import bstack11l11l1l_opy_
from bstack_utils import bstack1l1l1l1111_opy_
bstack11ll111l11l_opy_ = 10
class bstack1l11111l11_opy_:
    def __init__(self, bstack111lll111_opy_, config, bstack11ll11111ll_opy_=0):
        self.bstack11ll111l1ll_opy_ = set()
        self.lock = threading.Lock()
        self.bstack11l1lllll11_opy_ = bstack1ll11_opy_ (u"ࠢࡼࡿ࠲ࡸࡪࡹࡴࡰࡴࡦ࡬ࡪࡹࡴࡳࡣࡷ࡭ࡴࡴ࠯ࡢࡲ࡬࠳ࡻ࠷࠯ࡧࡣ࡬ࡰࡪࡪ࠭ࡵࡧࡶࡸࡸࠨᜩ").format(bstack11lll11l1ll_opy_)
        self.bstack11l1llll1ll_opy_ = os.path.join(tempfile.gettempdir(), bstack1ll11_opy_ (u"ࠣࡣࡥࡳࡷࡺ࡟ࡣࡷ࡬ࡰࡩࡥࡻࡾࠤᜪ").format(os.environ.get(bstack1ll11_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡎࡕࡃࡡࡘ࡙ࡎࡊࠧᜫ"))))
        self.bstack11l1lllll1l_opy_ = os.path.join(tempfile.gettempdir(), bstack1ll11_opy_ (u"ࠥࡪࡦ࡯࡬ࡦࡦࡢࡸࡪࡹࡴࡴࡡࡾࢁ࠳ࡺࡸࡵࠤᜬ").format(os.environ.get(bstack1ll11_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡉࡗࡅࡣ࡚࡛ࡉࡅࠩᜭ"))))
        self.bstack11l1lllllll_opy_ = 2
        self.bstack111lll111_opy_ = bstack111lll111_opy_
        self.config = config
        self.logger = bstack1l1l1l1111_opy_.get_logger(__name__, bstack111lll1l1l_opy_)
        self.bstack11ll11111ll_opy_ = bstack11ll11111ll_opy_
        self.bstack11ll11111l1_opy_ = False
        self.bstack11l1llll1l1_opy_ = not (
                            os.environ.get(bstack1ll11_opy_ (u"ࠧࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡇ࡛ࡉࡍࡆࡢࡖ࡚ࡔ࡟ࡊࡆࡈࡒ࡙ࡏࡆࡊࡇࡕࠦᜮ")) and
                            os.environ.get(bstack1ll11_opy_ (u"ࠨࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡔࡏࡅࡇࡢࡍࡓࡊࡅ࡙ࠤᜯ")) and
                            os.environ.get(bstack1ll11_opy_ (u"ࠢࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡐࡖࡄࡐࡤࡔࡏࡅࡇࡢࡇࡔ࡛ࡎࡕࠤᜰ"))
                        )
        if bstack11l11l1l_opy_.bstack11ll1111111_opy_(config):
            self.bstack11l1lllllll_opy_ = bstack11l11l1l_opy_.bstack11ll1111l11_opy_(config, self.bstack11ll11111ll_opy_)
            self.bstack11ll1111l1l_opy_()
    def bstack11l1llll11l_opy_(self):
        return bstack1ll11_opy_ (u"ࠣࡽࢀࡣࢀࢃࠢᜱ").format(self.config.get(bstack1ll11_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡏࡣࡰࡩࠬᜲ")), os.environ.get(bstack1ll11_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡅ࡙ࡎࡒࡄࡠࡔࡘࡒࡤࡏࡄࡆࡐࡗࡍࡋࡏࡅࡓࠩᜳ")))
    def bstack11ll1111ll1_opy_(self):
        try:
            if self.bstack11l1llll1l1_opy_:
                return
            with self.lock:
                try:
                    with open(self.bstack11l1lllll1l_opy_, bstack1ll11_opy_ (u"ࠦࡷࠨ᜴")) as f:
                        bstack11l1llllll1_opy_ = set(line.strip() for line in f if line.strip())
                except FileNotFoundError:
                    bstack11l1llllll1_opy_ = set()
                bstack11ll111l111_opy_ = bstack11l1llllll1_opy_ - self.bstack11ll111l1ll_opy_
                if not bstack11ll111l111_opy_:
                    return
                self.bstack11ll111l1ll_opy_.update(bstack11ll111l111_opy_)
                data = {bstack1ll11_opy_ (u"ࠧ࡬ࡡࡪ࡮ࡨࡨ࡙࡫ࡳࡵࡵࠥ᜵"): list(self.bstack11ll111l1ll_opy_), bstack1ll11_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡓࡧ࡭ࡦࠤ᜶"): self.config.get(bstack1ll11_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡔࡡ࡮ࡧࠪ᜷")), bstack1ll11_opy_ (u"ࠣࡤࡸ࡭ࡱࡪࡒࡶࡰࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷࠨ᜸"): os.environ.get(bstack1ll11_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡄࡘࡍࡑࡊ࡟ࡓࡗࡑࡣࡎࡊࡅࡏࡖࡌࡊࡎࡋࡒࠨ᜹")), bstack1ll11_opy_ (u"ࠥࡴࡷࡵࡪࡦࡥࡷࡒࡦࡳࡥࠣ᜺"): self.config.get(bstack1ll11_opy_ (u"ࠫࡵࡸ࡯࡫ࡧࡦࡸࡓࡧ࡭ࡦࠩ᜻"))}
            response = bstack11ll1llllll_opy_.bstack11ll11l1l1l_opy_(self.bstack11l1lllll11_opy_, data)
            if response.get(bstack1ll11_opy_ (u"ࠧࡹࡴࡢࡶࡸࡷࠧ᜼")) == 200:
                self.logger.debug(bstack1ll11_opy_ (u"ࠨࡓࡶࡥࡦࡩࡸࡹࡦࡶ࡮࡯ࡽࠥࡹࡥ࡯ࡶࠣࡪࡦ࡯࡬ࡦࡦࠣࡸࡪࡹࡴࡴ࠼ࠣࡿࢂࠨ᜽").format(data))
            else:
                self.logger.debug(bstack1ll11_opy_ (u"ࠢࡇࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡷࡪࡴࡤࠡࡨࡤ࡭ࡱ࡫ࡤࠡࡶࡨࡷࡹࡹ࠺ࠡࡽࢀࠦ᜾").format(response))
        except Exception as e:
            self.logger.debug(bstack1ll11_opy_ (u"ࠣࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤࡩࡻࡲࡪࡰࡪࠤࡸ࡫࡮ࡥ࡫ࡱ࡫ࠥ࡬ࡡࡪ࡮ࡨࡨࠥࡺࡥࡴࡶࡶ࠾ࠥࢁࡽࠣ᜿").format(e))
    def bstack11ll11ll1l1_opy_(self):
        if self.bstack11l1llll1l1_opy_:
            with self.lock:
                try:
                    with open(self.bstack11l1lllll1l_opy_, bstack1ll11_opy_ (u"ࠤࡵࠦᝀ")) as f:
                        bstack11ll111ll11_opy_ = set(line.strip() for line in f if line.strip())
                    failed_count = len(bstack11ll111ll11_opy_)
                except FileNotFoundError:
                    failed_count = 0
                self.logger.debug(bstack1ll11_opy_ (u"ࠥࡔࡴࡲ࡬ࡦࡦࠣࡪࡦ࡯࡬ࡦࡦࠣࡸࡪࡹࡴࡴࠢࡦࡳࡺࡴࡴࠡࠪ࡯ࡳࡨࡧ࡬ࠪ࠼ࠣࡿࢂࠨᝁ").format(failed_count))
                if failed_count >= self.bstack11l1lllllll_opy_:
                    self.logger.info(bstack1ll11_opy_ (u"࡙ࠦ࡮ࡲࡦࡵ࡫ࡳࡱࡪࠠࡤࡴࡲࡷࡸ࡫ࡤࠡࠪ࡯ࡳࡨࡧ࡬ࠪ࠼ࠣࡿࢂࠦ࠾࠾ࠢࡾࢁࠧᝂ").format(failed_count, self.bstack11l1lllllll_opy_))
                    self.bstack11ll111l1l1_opy_(failed_count)
                    self.bstack11ll11111l1_opy_ = True
            return
        try:
            response = bstack11ll1llllll_opy_.bstack11ll11ll1l1_opy_(bstack1ll11_opy_ (u"ࠧࢁࡽࡀࡤࡸ࡭ࡱࡪࡎࡢ࡯ࡨࡁࢀࢃࠦࡣࡷ࡬ࡰࡩࡘࡵ࡯ࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࡂࢁࡽࠧࡲࡵࡳ࡯࡫ࡣࡵࡐࡤࡱࡪࡃࡻࡾࠤᝃ").format(self.bstack11l1lllll11_opy_, self.config.get(bstack1ll11_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡓࡧ࡭ࡦࠩᝄ")), os.environ.get(bstack1ll11_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡂࡖࡋࡏࡈࡤࡘࡕࡏࡡࡌࡈࡊࡔࡔࡊࡈࡌࡉࡗ࠭ᝅ")), self.config.get(bstack1ll11_opy_ (u"ࠨࡲࡵࡳ࡯࡫ࡣࡵࡐࡤࡱࡪ࠭ᝆ"))))
            if response.get(bstack1ll11_opy_ (u"ࠤࡶࡸࡦࡺࡵࡴࠤᝇ")) == 200:
                failed_count = response.get(bstack1ll11_opy_ (u"ࠥࡪࡦ࡯࡬ࡦࡦࡗࡩࡸࡺࡳࡄࡱࡸࡲࡹࠨᝈ"), 0)
                self.logger.debug(bstack1ll11_opy_ (u"ࠦࡕࡵ࡬࡭ࡧࡧࠤ࡫ࡧࡩ࡭ࡧࡧࠤࡹ࡫ࡳࡵࡵࠣࡧࡴࡻ࡮ࡵ࠼ࠣࡿࢂࠨᝉ").format(failed_count))
                if failed_count >= self.bstack11l1lllllll_opy_:
                    self.logger.info(bstack1ll11_opy_ (u"࡚ࠧࡨࡳࡧࡶ࡬ࡴࡲࡤࠡࡥࡵࡳࡸࡹࡥࡥ࠼ࠣࡿࢂࠦ࠾࠾ࠢࡾࢁࠧᝊ").format(failed_count, self.bstack11l1lllllll_opy_))
                    self.bstack11ll111l1l1_opy_(failed_count)
                    self.bstack11ll11111l1_opy_ = True
            else:
                self.logger.error(bstack1ll11_opy_ (u"ࠨࡆࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡳࡳࡱࡲࠠࡧࡣ࡬ࡰࡪࡪࠠࡵࡧࡶࡸࡸࡀࠠࡼࡿࠥᝋ").format(response))
        except Exception as e:
            self.logger.error(bstack1ll11_opy_ (u"ࠢࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣࡨࡺࡸࡩ࡯ࡩࠣࡴࡴࡲ࡬ࡪࡰࡪ࠾ࠥࢁࡽࠣᝌ").format(e))
    def bstack11ll111l1l1_opy_(self, failed_count):
        with open(self.bstack11l1llll1ll_opy_, bstack1ll11_opy_ (u"ࠣࡹࠥᝍ")) as f:
            f.write(bstack1ll11_opy_ (u"ࠤࡗ࡬ࡷ࡫ࡳࡩࡱ࡯ࡨࠥࡩࡲࡰࡵࡶࡩࡩࠦࡡࡵࠢࡾࢁࡡࡴࠢᝎ").format(datetime.now()))
            f.write(bstack1ll11_opy_ (u"ࠥࡊࡦ࡯࡬ࡦࡦࠣࡸࡪࡹࡴࡴࠢࡦࡳࡺࡴࡴ࠻ࠢࡾࢁࡡࡴࠢᝏ").format(failed_count))
        self.logger.debug(bstack1ll11_opy_ (u"ࠦࡆࡨ࡯ࡳࡶࠣࡆࡺ࡯࡬ࡥࠢࡩ࡭ࡱ࡫ࠠࡤࡴࡨࡥࡹ࡫ࡤ࠻ࠢࡾࢁࠧᝐ").format(self.bstack11l1llll1ll_opy_))
    def bstack11ll1111l1l_opy_(self):
        def bstack11ll1111lll_opy_():
            while not self.bstack11ll11111l1_opy_:
                time.sleep(bstack11ll111l11l_opy_)
                self.bstack11ll1111ll1_opy_()
                self.bstack11ll11ll1l1_opy_()
        bstack11ll111111l_opy_ = threading.Thread(target=bstack11ll1111lll_opy_, daemon=True)
        bstack11ll111111l_opy_.start()