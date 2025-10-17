# coding: UTF-8
import sys
bstack1111l11_opy_ = sys.version_info [0] == 2
bstack11111l_opy_ = 2048
bstack1111111_opy_ = 7
def bstack11l111_opy_ (bstack1ll1l1_opy_):
    global bstack1llll1_opy_
    bstack1l1l1_opy_ = ord (bstack1ll1l1_opy_ [-1])
    bstack1lll1_opy_ = bstack1ll1l1_opy_ [:-1]
    bstack1l1l11_opy_ = bstack1l1l1_opy_ % len (bstack1lll1_opy_)
    bstack1l1l111_opy_ = bstack1lll1_opy_ [:bstack1l1l11_opy_] + bstack1lll1_opy_ [bstack1l1l11_opy_:]
    if bstack1111l11_opy_:
        bstack1111lll_opy_ = unicode () .join ([unichr (ord (char) - bstack11111l_opy_ - (bstack1llllll_opy_ + bstack1l1l1_opy_) % bstack1111111_opy_) for bstack1llllll_opy_, char in enumerate (bstack1l1l111_opy_)])
    else:
        bstack1111lll_opy_ = str () .join ([chr (ord (char) - bstack11111l_opy_ - (bstack1llllll_opy_ + bstack1l1l1_opy_) % bstack1111111_opy_) for bstack1llllll_opy_, char in enumerate (bstack1l1l111_opy_)])
    return eval (bstack1111lll_opy_)
import threading
import tempfile
import os
import time
from datetime import datetime
from bstack_utils.bstack11lll111lll_opy_ import bstack11lll111111_opy_
from bstack_utils.constants import bstack11lll111l11_opy_, bstack1llll11lll_opy_
from bstack_utils.bstack1lll1l1l1_opy_ import bstack1llllllll_opy_
from bstack_utils import bstack1lll11ll11_opy_
bstack11l1lll1lll_opy_ = 10
class bstack1111ll111l_opy_:
    def __init__(self, bstack11l1ll1ll1_opy_, config, bstack11ll1111l1l_opy_=0):
        self.bstack11l1lllll11_opy_ = set()
        self.lock = threading.Lock()
        self.bstack11ll1111lll_opy_ = bstack11l111_opy_ (u"ࠧࢁࡽ࠰ࡶࡨࡷࡹࡵࡲࡤࡪࡨࡷࡹࡸࡡࡵ࡫ࡲࡲ࠴ࡧࡰࡪ࠱ࡹ࠵࠴࡬ࡡࡪ࡮ࡨࡨ࠲ࡺࡥࡴࡶࡶࠦ᜙").format(bstack11lll111l11_opy_)
        self.bstack11ll1111ll1_opy_ = os.path.join(tempfile.gettempdir(), bstack11l111_opy_ (u"ࠨࡡࡣࡱࡵࡸࡤࡨࡵࡪ࡮ࡧࡣࢀࢃࠢ᜚").format(os.environ.get(bstack11l111_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡖࡗࡌࡈࠬ᜛"))))
        self.bstack11ll111111l_opy_ = os.path.join(tempfile.gettempdir(), bstack11l111_opy_ (u"ࠣࡨࡤ࡭ࡱ࡫ࡤࡠࡶࡨࡷࡹࡹ࡟ࡼࡿ࠱ࡸࡽࡺࠢ᜜").format(os.environ.get(bstack11l111_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡎࡕࡃࡡࡘ࡙ࡎࡊࠧ᜝"))))
        self.bstack11ll111l111_opy_ = 2
        self.bstack11l1ll1ll1_opy_ = bstack11l1ll1ll1_opy_
        self.config = config
        self.logger = bstack1lll11ll11_opy_.get_logger(__name__, bstack1llll11lll_opy_)
        self.bstack11ll1111l1l_opy_ = bstack11ll1111l1l_opy_
        self.bstack11ll11111l1_opy_ = False
        self.bstack11ll1111111_opy_ = not (
                            os.environ.get(bstack11l111_opy_ (u"ࠥࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡅ࡙ࡎࡒࡄࡠࡔࡘࡒࡤࡏࡄࡆࡐࡗࡍࡋࡏࡅࡓࠤ᜞")) and
                            os.environ.get(bstack11l111_opy_ (u"ࠦࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡒࡔࡊࡅࡠࡋࡑࡈࡊ࡞ࠢᜟ")) and
                            os.environ.get(bstack11l111_opy_ (u"ࠧࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡕࡔࡂࡎࡢࡒࡔࡊࡅࡠࡅࡒ࡙ࡓ࡚ࠢᜠ"))
                        )
        if bstack1llllllll_opy_.bstack11l1llll1ll_opy_(config):
            self.bstack11ll111l111_opy_ = bstack1llllllll_opy_.bstack11l1llll111_opy_(config, self.bstack11ll1111l1l_opy_)
            self.bstack11ll11111ll_opy_()
    def bstack11l1lllll1l_opy_(self):
        return bstack11l111_opy_ (u"ࠨࡻࡾࡡࡾࢁࠧᜡ").format(self.config.get(bstack11l111_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡔࡡ࡮ࡧࠪᜢ")), os.environ.get(bstack11l111_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡃࡗࡌࡐࡉࡥࡒࡖࡐࡢࡍࡉࡋࡎࡕࡋࡉࡍࡊࡘࠧᜣ")))
    def bstack11l1lll1l1l_opy_(self):
        try:
            if self.bstack11ll1111111_opy_:
                return
            with self.lock:
                try:
                    with open(self.bstack11ll111111l_opy_, bstack11l111_opy_ (u"ࠤࡵࠦᜤ")) as f:
                        bstack11l1llll1l1_opy_ = set(line.strip() for line in f if line.strip())
                except FileNotFoundError:
                    bstack11l1llll1l1_opy_ = set()
                bstack11l1llllll1_opy_ = bstack11l1llll1l1_opy_ - self.bstack11l1lllll11_opy_
                if not bstack11l1llllll1_opy_:
                    return
                self.bstack11l1lllll11_opy_.update(bstack11l1llllll1_opy_)
                data = {bstack11l111_opy_ (u"ࠥࡪࡦ࡯࡬ࡦࡦࡗࡩࡸࡺࡳࠣᜥ"): list(self.bstack11l1lllll11_opy_), bstack11l111_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡑࡥࡲ࡫ࠢᜦ"): self.config.get(bstack11l111_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡒࡦࡳࡥࠨᜧ")), bstack11l111_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡗࡻ࡮ࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠦᜨ"): os.environ.get(bstack11l111_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡂࡖࡋࡏࡈࡤࡘࡕࡏࡡࡌࡈࡊࡔࡔࡊࡈࡌࡉࡗ࠭ᜩ")), bstack11l111_opy_ (u"ࠣࡲࡵࡳ࡯࡫ࡣࡵࡐࡤࡱࡪࠨᜪ"): self.config.get(bstack11l111_opy_ (u"ࠩࡳࡶࡴࡰࡥࡤࡶࡑࡥࡲ࡫ࠧᜫ"))}
            response = bstack11lll111111_opy_.bstack11ll11ll11l_opy_(self.bstack11ll1111lll_opy_, data)
            if response.get(bstack11l111_opy_ (u"ࠥࡷࡹࡧࡴࡶࡵࠥᜬ")) == 200:
                self.logger.debug(bstack11l111_opy_ (u"ࠦࡘࡻࡣࡤࡧࡶࡷ࡫ࡻ࡬࡭ࡻࠣࡷࡪࡴࡴࠡࡨࡤ࡭ࡱ࡫ࡤࠡࡶࡨࡷࡹࡹ࠺ࠡࡽࢀࠦᜭ").format(data))
            else:
                self.logger.debug(bstack11l111_opy_ (u"ࠧࡌࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡࡵࡨࡲࡩࠦࡦࡢ࡫࡯ࡩࡩࠦࡴࡦࡵࡷࡷ࠿ࠦࡻࡾࠤᜮ").format(response))
        except Exception as e:
            self.logger.debug(bstack11l111_opy_ (u"ࠨࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢࡧࡹࡷ࡯࡮ࡨࠢࡶࡩࡳࡪࡩ࡯ࡩࠣࡪࡦ࡯࡬ࡦࡦࠣࡸࡪࡹࡴࡴ࠼ࠣࡿࢂࠨᜯ").format(e))
    def bstack11ll11ll1ll_opy_(self):
        if self.bstack11ll1111111_opy_:
            with self.lock:
                try:
                    with open(self.bstack11ll111111l_opy_, bstack11l111_opy_ (u"ࠢࡳࠤᜰ")) as f:
                        bstack11ll1111l11_opy_ = set(line.strip() for line in f if line.strip())
                    failed_count = len(bstack11ll1111l11_opy_)
                except FileNotFoundError:
                    failed_count = 0
                self.logger.debug(bstack11l111_opy_ (u"ࠣࡒࡲࡰࡱ࡫ࡤࠡࡨࡤ࡭ࡱ࡫ࡤࠡࡶࡨࡷࡹࡹࠠࡤࡱࡸࡲࡹࠦࠨ࡭ࡱࡦࡥࡱ࠯࠺ࠡࡽࢀࠦᜱ").format(failed_count))
                if failed_count >= self.bstack11ll111l111_opy_:
                    self.logger.info(bstack11l111_opy_ (u"ࠤࡗ࡬ࡷ࡫ࡳࡩࡱ࡯ࡨࠥࡩࡲࡰࡵࡶࡩࡩࠦࠨ࡭ࡱࡦࡥࡱ࠯࠺ࠡࡽࢀࠤࡃࡃࠠࡼࡿࠥᜲ").format(failed_count, self.bstack11ll111l111_opy_))
                    self.bstack11l1lllllll_opy_(failed_count)
                    self.bstack11ll11111l1_opy_ = True
            return
        try:
            response = bstack11lll111111_opy_.bstack11ll11ll1ll_opy_(bstack11l111_opy_ (u"ࠥࡿࢂࡅࡢࡶ࡫࡯ࡨࡓࡧ࡭ࡦ࠿ࡾࢁࠫࡨࡵࡪ࡮ࡧࡖࡺࡴࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࡀࡿࢂࠬࡰࡳࡱ࡭ࡩࡨࡺࡎࡢ࡯ࡨࡁࢀࢃࠢᜳ").format(self.bstack11ll1111lll_opy_, self.config.get(bstack11l111_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡑࡥࡲ࡫᜴ࠧ")), os.environ.get(bstack11l111_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡇ࡛ࡉࡍࡆࡢࡖ࡚ࡔ࡟ࡊࡆࡈࡒ࡙ࡏࡆࡊࡇࡕࠫ᜵")), self.config.get(bstack11l111_opy_ (u"࠭ࡰࡳࡱ࡭ࡩࡨࡺࡎࡢ࡯ࡨࠫ᜶"))))
            if response.get(bstack11l111_opy_ (u"ࠢࡴࡶࡤࡸࡺࡹࠢ᜷")) == 200:
                failed_count = response.get(bstack11l111_opy_ (u"ࠣࡨࡤ࡭ࡱ࡫ࡤࡕࡧࡶࡸࡸࡉ࡯ࡶࡰࡷࠦ᜸"), 0)
                self.logger.debug(bstack11l111_opy_ (u"ࠤࡓࡳࡱࡲࡥࡥࠢࡩࡥ࡮ࡲࡥࡥࠢࡷࡩࡸࡺࡳࠡࡥࡲࡹࡳࡺ࠺ࠡࡽࢀࠦ᜹").format(failed_count))
                if failed_count >= self.bstack11ll111l111_opy_:
                    self.logger.info(bstack11l111_opy_ (u"ࠥࡘ࡭ࡸࡥࡴࡪࡲࡰࡩࠦࡣࡳࡱࡶࡷࡪࡪ࠺ࠡࡽࢀࠤࡃࡃࠠࡼࡿࠥ᜺").format(failed_count, self.bstack11ll111l111_opy_))
                    self.bstack11l1lllllll_opy_(failed_count)
                    self.bstack11ll11111l1_opy_ = True
            else:
                self.logger.error(bstack11l111_opy_ (u"ࠦࡋࡧࡩ࡭ࡧࡧࠤࡹࡵࠠࡱࡱ࡯ࡰࠥ࡬ࡡࡪ࡮ࡨࡨࠥࡺࡥࡴࡶࡶ࠾ࠥࢁࡽࠣ᜻").format(response))
        except Exception as e:
            self.logger.error(bstack11l111_opy_ (u"ࠧࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡࡦࡸࡶ࡮ࡴࡧࠡࡲࡲࡰࡱ࡯࡮ࡨ࠼ࠣࡿࢂࠨ᜼").format(e))
    def bstack11l1lllllll_opy_(self, failed_count):
        with open(self.bstack11ll1111ll1_opy_, bstack11l111_opy_ (u"ࠨࡷࠣ᜽")) as f:
            f.write(bstack11l111_opy_ (u"ࠢࡕࡪࡵࡩࡸ࡮࡯࡭ࡦࠣࡧࡷࡵࡳࡴࡧࡧࠤࡦࡺࠠࡼࡿ࡟ࡲࠧ᜾").format(datetime.now()))
            f.write(bstack11l111_opy_ (u"ࠣࡈࡤ࡭ࡱ࡫ࡤࠡࡶࡨࡷࡹࡹࠠࡤࡱࡸࡲࡹࡀࠠࡼࡿ࡟ࡲࠧ᜿").format(failed_count))
        self.logger.debug(bstack11l111_opy_ (u"ࠤࡄࡦࡴࡸࡴࠡࡄࡸ࡭ࡱࡪࠠࡧ࡫࡯ࡩࠥࡩࡲࡦࡣࡷࡩࡩࡀࠠࡼࡿࠥᝀ").format(self.bstack11ll1111ll1_opy_))
    def bstack11ll11111ll_opy_(self):
        def bstack11l1llll11l_opy_():
            while not self.bstack11ll11111l1_opy_:
                time.sleep(bstack11l1lll1lll_opy_)
                self.bstack11l1lll1l1l_opy_()
                self.bstack11ll11ll1ll_opy_()
        bstack11l1lll1ll1_opy_ = threading.Thread(target=bstack11l1llll11l_opy_, daemon=True)
        bstack11l1lll1ll1_opy_.start()