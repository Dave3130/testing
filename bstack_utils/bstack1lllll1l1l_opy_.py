# coding: UTF-8
import sys
bstack1l1lll_opy_ = sys.version_info [0] == 2
bstack1l1l1ll_opy_ = 2048
bstack1lllllll_opy_ = 7
def bstack1ll1l_opy_ (bstack1ll1l1l_opy_):
    global bstack11ll1l_opy_
    bstack111l111_opy_ = ord (bstack1ll1l1l_opy_ [-1])
    bstack1l111ll_opy_ = bstack1ll1l1l_opy_ [:-1]
    bstack1ll_opy_ = bstack111l111_opy_ % len (bstack1l111ll_opy_)
    bstack111l_opy_ = bstack1l111ll_opy_ [:bstack1ll_opy_] + bstack1l111ll_opy_ [bstack1ll_opy_:]
    if bstack1l1lll_opy_:
        bstack1lll1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack1l1l1ll_opy_ - (bstack1111lll_opy_ + bstack111l111_opy_) % bstack1lllllll_opy_) for bstack1111lll_opy_, char in enumerate (bstack111l_opy_)])
    else:
        bstack1lll1ll_opy_ = str () .join ([chr (ord (char) - bstack1l1l1ll_opy_ - (bstack1111lll_opy_ + bstack111l111_opy_) % bstack1lllllll_opy_) for bstack1111lll_opy_, char in enumerate (bstack111l_opy_)])
    return eval (bstack1lll1ll_opy_)
import threading
import tempfile
import os
import time
from datetime import datetime
from bstack_utils.bstack11ll1ll11l1_opy_ import bstack11ll1ll1ll1_opy_
from bstack_utils.constants import bstack11ll1ll1lll_opy_, bstack1llll1ll1l_opy_
from bstack_utils.bstack1111llll_opy_ import bstack11111l1l_opy_
from bstack_utils import bstack1ll1ll111_opy_
bstack11ll11111ll_opy_ = 10
class bstack11lll111l_opy_:
    def __init__(self, bstack1111l1l11l_opy_, config, bstack11l1llll1ll_opy_=0):
        self.bstack11ll1111lll_opy_ = set()
        self.lock = threading.Lock()
        self.bstack11l1lllll1l_opy_ = bstack1ll1l_opy_ (u"ࠤࡾࢁ࠴ࡺࡥࡴࡶࡲࡶࡨ࡮ࡥࡴࡶࡵࡥࡹ࡯࡯࡯࠱ࡤࡴ࡮࠵ࡶ࠲࠱ࡩࡥ࡮ࡲࡥࡥ࠯ࡷࡩࡸࡺࡳࠣᜤ").format(bstack11ll1ll1lll_opy_)
        self.bstack11ll111111l_opy_ = os.path.join(tempfile.gettempdir(), bstack1ll1l_opy_ (u"ࠥࡥࡧࡵࡲࡵࡡࡥࡹ࡮ࡲࡤࡠࡽࢀࠦᜥ").format(os.environ.get(bstack1ll1l_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡉࡗࡅࡣ࡚࡛ࡉࡅࠩᜦ"))))
        self.bstack11ll11111l1_opy_ = os.path.join(tempfile.gettempdir(), bstack1ll1l_opy_ (u"ࠧ࡬ࡡࡪ࡮ࡨࡨࡤࡺࡥࡴࡶࡶࡣࢀࢃ࠮ࡵࡺࡷࠦᜧ").format(os.environ.get(bstack1ll1l_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡕࡖࡋࡇࠫᜨ"))))
        self.bstack11ll111l1l1_opy_ = 2
        self.bstack1111l1l11l_opy_ = bstack1111l1l11l_opy_
        self.config = config
        self.logger = bstack1ll1ll111_opy_.get_logger(__name__, bstack1llll1ll1l_opy_)
        self.bstack11l1llll1ll_opy_ = bstack11l1llll1ll_opy_
        self.bstack11l1llllll1_opy_ = False
        self.bstack11l1llll111_opy_ = not (
                            os.environ.get(bstack1ll1l_opy_ (u"ࠢࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡂࡖࡋࡏࡈࡤࡘࡕࡏࡡࡌࡈࡊࡔࡔࡊࡈࡌࡉࡗࠨᜩ")) and
                            os.environ.get(bstack1ll1l_opy_ (u"ࠣࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡏࡑࡇࡉࡤࡏࡎࡅࡇ࡛ࠦᜪ")) and
                            os.environ.get(bstack1ll1l_opy_ (u"ࠤࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡒࡘࡆࡒ࡟ࡏࡑࡇࡉࡤࡉࡏࡖࡐࡗࠦᜫ"))
                        )
        if bstack11111l1l_opy_.bstack11ll111l11l_opy_(config):
            self.bstack11ll111l1l1_opy_ = bstack11111l1l_opy_.bstack11ll111l111_opy_(config, self.bstack11l1llll1ll_opy_)
            self.bstack11l1llll11l_opy_()
    def bstack11ll1111l11_opy_(self):
        return bstack1ll1l_opy_ (u"ࠥࡿࢂࡥࡻࡾࠤᜬ").format(self.config.get(bstack1ll1l_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡑࡥࡲ࡫ࠧᜭ")), os.environ.get(bstack1ll1l_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡇ࡛ࡉࡍࡆࡢࡖ࡚ࡔ࡟ࡊࡆࡈࡒ࡙ࡏࡆࡊࡇࡕࠫᜮ")))
    def bstack11l1llll1l1_opy_(self):
        try:
            if self.bstack11l1llll111_opy_:
                return
            with self.lock:
                try:
                    with open(self.bstack11ll11111l1_opy_, bstack1ll1l_opy_ (u"ࠨࡲࠣᜯ")) as f:
                        bstack11ll1111l1l_opy_ = set(line.strip() for line in f if line.strip())
                except FileNotFoundError:
                    bstack11ll1111l1l_opy_ = set()
                bstack11l1lll1lll_opy_ = bstack11ll1111l1l_opy_ - self.bstack11ll1111lll_opy_
                if not bstack11l1lll1lll_opy_:
                    return
                self.bstack11ll1111lll_opy_.update(bstack11l1lll1lll_opy_)
                data = {bstack1ll1l_opy_ (u"ࠢࡧࡣ࡬ࡰࡪࡪࡔࡦࡵࡷࡷࠧᜰ"): list(self.bstack11ll1111lll_opy_), bstack1ll1l_opy_ (u"ࠣࡤࡸ࡭ࡱࡪࡎࡢ࡯ࡨࠦᜱ"): self.config.get(bstack1ll1l_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡏࡣࡰࡩࠬᜲ")), bstack1ll1l_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡔࡸࡲࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠣᜳ"): os.environ.get(bstack1ll1l_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡆ࡚ࡏࡌࡅࡡࡕ࡙ࡓࡥࡉࡅࡇࡑࡘࡎࡌࡉࡆࡔ᜴ࠪ")), bstack1ll1l_opy_ (u"ࠧࡶࡲࡰ࡬ࡨࡧࡹࡔࡡ࡮ࡧࠥ᜵"): self.config.get(bstack1ll1l_opy_ (u"࠭ࡰࡳࡱ࡭ࡩࡨࡺࡎࡢ࡯ࡨࠫ᜶"))}
            response = bstack11ll1ll1ll1_opy_.bstack11ll11l11ll_opy_(self.bstack11l1lllll1l_opy_, data)
            if response.get(bstack1ll1l_opy_ (u"ࠢࡴࡶࡤࡸࡺࡹࠢ᜷")) == 200:
                self.logger.debug(bstack1ll1l_opy_ (u"ࠣࡕࡸࡧࡨ࡫ࡳࡴࡨࡸࡰࡱࡿࠠࡴࡧࡱࡸࠥ࡬ࡡࡪ࡮ࡨࡨࠥࡺࡥࡴࡶࡶ࠾ࠥࢁࡽࠣ᜸").format(data))
            else:
                self.logger.debug(bstack1ll1l_opy_ (u"ࠤࡉࡥ࡮ࡲࡥࡥࠢࡷࡳࠥࡹࡥ࡯ࡦࠣࡪࡦ࡯࡬ࡦࡦࠣࡸࡪࡹࡴࡴ࠼ࠣࡿࢂࠨ᜹").format(response))
        except Exception as e:
            self.logger.debug(bstack1ll1l_opy_ (u"ࠥࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡤࡶࡴ࡬ࡲ࡬ࠦࡳࡦࡰࡧ࡭ࡳ࡭ࠠࡧࡣ࡬ࡰࡪࡪࠠࡵࡧࡶࡸࡸࡀࠠࡼࡿࠥ᜺").format(e))
    def bstack11ll11ll111_opy_(self):
        if self.bstack11l1llll111_opy_:
            with self.lock:
                try:
                    with open(self.bstack11ll11111l1_opy_, bstack1ll1l_opy_ (u"ࠦࡷࠨ᜻")) as f:
                        bstack11l1lllllll_opy_ = set(line.strip() for line in f if line.strip())
                    failed_count = len(bstack11l1lllllll_opy_)
                except FileNotFoundError:
                    failed_count = 0
                self.logger.debug(bstack1ll1l_opy_ (u"ࠧࡖ࡯࡭࡮ࡨࡨࠥ࡬ࡡࡪ࡮ࡨࡨࠥࡺࡥࡴࡶࡶࠤࡨࡵࡵ࡯ࡶࠣࠬࡱࡵࡣࡢ࡮ࠬ࠾ࠥࢁࡽࠣ᜼").format(failed_count))
                if failed_count >= self.bstack11ll111l1l1_opy_:
                    self.logger.info(bstack1ll1l_opy_ (u"ࠨࡔࡩࡴࡨࡷ࡭ࡵ࡬ࡥࠢࡦࡶࡴࡹࡳࡦࡦࠣࠬࡱࡵࡣࡢ࡮ࠬ࠾ࠥࢁࡽࠡࡀࡀࠤࢀࢃࠢ᜽").format(failed_count, self.bstack11ll111l1l1_opy_))
                    self.bstack11ll1111ll1_opy_(failed_count)
                    self.bstack11l1llllll1_opy_ = True
            return
        try:
            response = bstack11ll1ll1ll1_opy_.bstack11ll11ll111_opy_(bstack1ll1l_opy_ (u"ࠢࡼࡿࡂࡦࡺ࡯࡬ࡥࡐࡤࡱࡪࡃࡻࡾࠨࡥࡹ࡮ࡲࡤࡓࡷࡱࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸ࠽ࡼࡿࠩࡴࡷࡵࡪࡦࡥࡷࡒࡦࡳࡥ࠾ࡽࢀࠦ᜾").format(self.bstack11l1lllll1l_opy_, self.config.get(bstack1ll1l_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡎࡢ࡯ࡨࠫ᜿")), os.environ.get(bstack1ll1l_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡄࡘࡍࡑࡊ࡟ࡓࡗࡑࡣࡎࡊࡅࡏࡖࡌࡊࡎࡋࡒࠨᝀ")), self.config.get(bstack1ll1l_opy_ (u"ࠪࡴࡷࡵࡪࡦࡥࡷࡒࡦࡳࡥࠨᝁ"))))
            if response.get(bstack1ll1l_opy_ (u"ࠦࡸࡺࡡࡵࡷࡶࠦᝂ")) == 200:
                failed_count = response.get(bstack1ll1l_opy_ (u"ࠧ࡬ࡡࡪ࡮ࡨࡨ࡙࡫ࡳࡵࡵࡆࡳࡺࡴࡴࠣᝃ"), 0)
                self.logger.debug(bstack1ll1l_opy_ (u"ࠨࡐࡰ࡮࡯ࡩࡩࠦࡦࡢ࡫࡯ࡩࡩࠦࡴࡦࡵࡷࡷࠥࡩ࡯ࡶࡰࡷ࠾ࠥࢁࡽࠣᝄ").format(failed_count))
                if failed_count >= self.bstack11ll111l1l1_opy_:
                    self.logger.info(bstack1ll1l_opy_ (u"ࠢࡕࡪࡵࡩࡸ࡮࡯࡭ࡦࠣࡧࡷࡵࡳࡴࡧࡧ࠾ࠥࢁࡽࠡࡀࡀࠤࢀࢃࠢᝅ").format(failed_count, self.bstack11ll111l1l1_opy_))
                    self.bstack11ll1111ll1_opy_(failed_count)
                    self.bstack11l1llllll1_opy_ = True
            else:
                self.logger.error(bstack1ll1l_opy_ (u"ࠣࡈࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤࡵࡵ࡬࡭ࠢࡩࡥ࡮ࡲࡥࡥࠢࡷࡩࡸࡺࡳ࠻ࠢࡾࢁࠧᝆ").format(response))
        except Exception as e:
            self.logger.error(bstack1ll1l_opy_ (u"ࠤࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥࡪࡵࡳ࡫ࡱ࡫ࠥࡶ࡯࡭࡮࡬ࡲ࡬ࡀࠠࡼࡿࠥᝇ").format(e))
    def bstack11ll1111ll1_opy_(self, failed_count):
        with open(self.bstack11ll111111l_opy_, bstack1ll1l_opy_ (u"ࠥࡻࠧᝈ")) as f:
            f.write(bstack1ll1l_opy_ (u"࡙ࠦ࡮ࡲࡦࡵ࡫ࡳࡱࡪࠠࡤࡴࡲࡷࡸ࡫ࡤࠡࡣࡷࠤࢀࢃ࡜࡯ࠤᝉ").format(datetime.now()))
            f.write(bstack1ll1l_opy_ (u"ࠧࡌࡡࡪ࡮ࡨࡨࠥࡺࡥࡴࡶࡶࠤࡨࡵࡵ࡯ࡶ࠽ࠤࢀࢃ࡜࡯ࠤᝊ").format(failed_count))
        self.logger.debug(bstack1ll1l_opy_ (u"ࠨࡁࡣࡱࡵࡸࠥࡈࡵࡪ࡮ࡧࠤ࡫࡯࡬ࡦࠢࡦࡶࡪࡧࡴࡦࡦ࠽ࠤࢀࢃࠢᝋ").format(self.bstack11ll111111l_opy_))
    def bstack11l1llll11l_opy_(self):
        def bstack11ll1111111_opy_():
            while not self.bstack11l1llllll1_opy_:
                time.sleep(bstack11ll11111ll_opy_)
                self.bstack11l1llll1l1_opy_()
                self.bstack11ll11ll111_opy_()
        bstack11l1lllll11_opy_ = threading.Thread(target=bstack11ll1111111_opy_, daemon=True)
        bstack11l1lllll11_opy_.start()