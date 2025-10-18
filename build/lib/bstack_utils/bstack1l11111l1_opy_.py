# coding: UTF-8
import sys
bstack11ll1l1_opy_ = sys.version_info [0] == 2
bstack11111ll_opy_ = 2048
bstack111lll1_opy_ = 7
def bstack1l1lll1_opy_ (bstack1lllll_opy_):
    global bstack111111l_opy_
    bstack1llll_opy_ = ord (bstack1lllll_opy_ [-1])
    bstack11lll1l_opy_ = bstack1lllll_opy_ [:-1]
    bstack1111_opy_ = bstack1llll_opy_ % len (bstack11lll1l_opy_)
    bstack11ll11l_opy_ = bstack11lll1l_opy_ [:bstack1111_opy_] + bstack11lll1l_opy_ [bstack1111_opy_:]
    if bstack11ll1l1_opy_:
        bstack1llll1_opy_ = unicode () .join ([unichr (ord (char) - bstack11111ll_opy_ - (bstack1l1l1ll_opy_ + bstack1llll_opy_) % bstack111lll1_opy_) for bstack1l1l1ll_opy_, char in enumerate (bstack11ll11l_opy_)])
    else:
        bstack1llll1_opy_ = str () .join ([chr (ord (char) - bstack11111ll_opy_ - (bstack1l1l1ll_opy_ + bstack1llll_opy_) % bstack111lll1_opy_) for bstack1l1l1ll_opy_, char in enumerate (bstack11ll11l_opy_)])
    return eval (bstack1llll1_opy_)
import threading
import tempfile
import os
import time
from datetime import datetime
from bstack_utils.bstack11ll1ll1l11_opy_ import bstack11ll1llll1l_opy_
from bstack_utils.constants import bstack11ll1llllll_opy_, bstack11ll111ll1_opy_
from bstack_utils.bstack11l111l1_opy_ import bstack1111llll_opy_
from bstack_utils import bstack111l11l1l_opy_
bstack11l1lll1lll_opy_ = 10
class bstack11l1lll1ll_opy_:
    def __init__(self, bstack11l11ll11_opy_, config, bstack11ll111l11l_opy_=0):
        self.bstack11l1llll11l_opy_ = set()
        self.lock = threading.Lock()
        self.bstack11ll1111l11_opy_ = bstack1l1lll1_opy_ (u"ࠥࡿࢂ࠵ࡴࡦࡵࡷࡳࡷࡩࡨࡦࡵࡷࡶࡦࡺࡩࡰࡰ࠲ࡥࡵ࡯࠯ࡷ࠳࠲ࡪࡦ࡯࡬ࡦࡦ࠰ࡸࡪࡹࡴࡴࠤᜥ").format(bstack11ll1llllll_opy_)
        self.bstack11ll1111ll1_opy_ = os.path.join(tempfile.gettempdir(), bstack1l1lll1_opy_ (u"ࠦࡦࡨ࡯ࡳࡶࡢࡦࡺ࡯࡬ࡥࡡࡾࢁࠧᜦ").format(os.environ.get(bstack1l1lll1_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡊࡘࡆࡤ࡛ࡕࡊࡆࠪᜧ"))))
        self.bstack11ll1111l1l_opy_ = os.path.join(tempfile.gettempdir(), bstack1l1lll1_opy_ (u"ࠨࡦࡢ࡫࡯ࡩࡩࡥࡴࡦࡵࡷࡷࡤࢁࡽ࠯ࡶࡻࡸࠧᜨ").format(os.environ.get(bstack1l1lll1_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡖࡗࡌࡈࠬᜩ"))))
        self.bstack11l1llll1l1_opy_ = 2
        self.bstack11l11ll11_opy_ = bstack11l11ll11_opy_
        self.config = config
        self.logger = bstack111l11l1l_opy_.get_logger(__name__, bstack11ll111ll1_opy_)
        self.bstack11ll111l11l_opy_ = bstack11ll111l11l_opy_
        self.bstack11l1lllllll_opy_ = False
        self.bstack11l1llll1ll_opy_ = not (
                            os.environ.get(bstack1l1lll1_opy_ (u"ࠣࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡃࡗࡌࡐࡉࡥࡒࡖࡐࡢࡍࡉࡋࡎࡕࡋࡉࡍࡊࡘࠢᜪ")) and
                            os.environ.get(bstack1l1lll1_opy_ (u"ࠤࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡐࡒࡈࡊࡥࡉࡏࡆࡈ࡜ࠧᜫ")) and
                            os.environ.get(bstack1l1lll1_opy_ (u"ࠥࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡓ࡙ࡇࡌࡠࡐࡒࡈࡊࡥࡃࡐࡗࡑࡘࠧᜬ"))
                        )
        if bstack1111llll_opy_.bstack11ll1111111_opy_(config):
            self.bstack11l1llll1l1_opy_ = bstack1111llll_opy_.bstack11ll11111l1_opy_(config, self.bstack11ll111l11l_opy_)
            self.bstack11l1lll1ll1_opy_()
    def bstack11l1llllll1_opy_(self):
        return bstack1l1lll1_opy_ (u"ࠦࢀࢃ࡟ࡼࡿࠥᜭ").format(self.config.get(bstack1l1lll1_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡒࡦࡳࡥࠨᜮ")), os.environ.get(bstack1l1lll1_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡈࡕࡊࡎࡇࡣࡗ࡛ࡎࡠࡋࡇࡉࡓ࡚ࡉࡇࡋࡈࡖࠬᜯ")))
    def bstack11l1lllll1l_opy_(self):
        try:
            if self.bstack11l1llll1ll_opy_:
                return
            with self.lock:
                try:
                    with open(self.bstack11ll1111l1l_opy_, bstack1l1lll1_opy_ (u"ࠢࡳࠤᜰ")) as f:
                        bstack11ll111111l_opy_ = set(line.strip() for line in f if line.strip())
                except FileNotFoundError:
                    bstack11ll111111l_opy_ = set()
                bstack11ll11111ll_opy_ = bstack11ll111111l_opy_ - self.bstack11l1llll11l_opy_
                if not bstack11ll11111ll_opy_:
                    return
                self.bstack11l1llll11l_opy_.update(bstack11ll11111ll_opy_)
                data = {bstack1l1lll1_opy_ (u"ࠣࡨࡤ࡭ࡱ࡫ࡤࡕࡧࡶࡸࡸࠨᜱ"): list(self.bstack11l1llll11l_opy_), bstack1l1lll1_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡏࡣࡰࡩࠧᜲ"): self.config.get(bstack1l1lll1_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡐࡤࡱࡪ࠭ᜳ")), bstack1l1lll1_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡕࡹࡳࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠤ᜴"): os.environ.get(bstack1l1lll1_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡇ࡛ࡉࡍࡆࡢࡖ࡚ࡔ࡟ࡊࡆࡈࡒ࡙ࡏࡆࡊࡇࡕࠫ᜵")), bstack1l1lll1_opy_ (u"ࠨࡰࡳࡱ࡭ࡩࡨࡺࡎࡢ࡯ࡨࠦ᜶"): self.config.get(bstack1l1lll1_opy_ (u"ࠧࡱࡴࡲ࡮ࡪࡩࡴࡏࡣࡰࡩࠬ᜷"))}
            response = bstack11ll1llll1l_opy_.bstack11ll11ll11l_opy_(self.bstack11ll1111l11_opy_, data)
            if response.get(bstack1l1lll1_opy_ (u"ࠣࡵࡷࡥࡹࡻࡳࠣ᜸")) == 200:
                self.logger.debug(bstack1l1lll1_opy_ (u"ࠤࡖࡹࡨࡩࡥࡴࡵࡩࡹࡱࡲࡹࠡࡵࡨࡲࡹࠦࡦࡢ࡫࡯ࡩࡩࠦࡴࡦࡵࡷࡷ࠿ࠦࡻࡾࠤ᜹").format(data))
            else:
                self.logger.debug(bstack1l1lll1_opy_ (u"ࠥࡊࡦ࡯࡬ࡦࡦࠣࡸࡴࠦࡳࡦࡰࡧࠤ࡫ࡧࡩ࡭ࡧࡧࠤࡹ࡫ࡳࡵࡵ࠽ࠤࢀࢃࠢ᜺").format(response))
        except Exception as e:
            self.logger.debug(bstack1l1lll1_opy_ (u"ࠦࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡥࡷࡵ࡭ࡳ࡭ࠠࡴࡧࡱࡨ࡮ࡴࡧࠡࡨࡤ࡭ࡱ࡫ࡤࠡࡶࡨࡷࡹࡹ࠺ࠡࡽࢀࠦ᜻").format(e))
    def bstack11ll11ll1l1_opy_(self):
        if self.bstack11l1llll1ll_opy_:
            with self.lock:
                try:
                    with open(self.bstack11ll1111l1l_opy_, bstack1l1lll1_opy_ (u"ࠧࡸࠢ᜼")) as f:
                        bstack11l1llll111_opy_ = set(line.strip() for line in f if line.strip())
                    failed_count = len(bstack11l1llll111_opy_)
                except FileNotFoundError:
                    failed_count = 0
                self.logger.debug(bstack1l1lll1_opy_ (u"ࠨࡐࡰ࡮࡯ࡩࡩࠦࡦࡢ࡫࡯ࡩࡩࠦࡴࡦࡵࡷࡷࠥࡩ࡯ࡶࡰࡷࠤ࠭ࡲ࡯ࡤࡣ࡯࠭࠿ࠦࡻࡾࠤ᜽").format(failed_count))
                if failed_count >= self.bstack11l1llll1l1_opy_:
                    self.logger.info(bstack1l1lll1_opy_ (u"ࠢࡕࡪࡵࡩࡸ࡮࡯࡭ࡦࠣࡧࡷࡵࡳࡴࡧࡧࠤ࠭ࡲ࡯ࡤࡣ࡯࠭࠿ࠦࡻࡾࠢࡁࡁࠥࢁࡽࠣ᜾").format(failed_count, self.bstack11l1llll1l1_opy_))
                    self.bstack11l1lllll11_opy_(failed_count)
                    self.bstack11l1lllllll_opy_ = True
            return
        try:
            response = bstack11ll1llll1l_opy_.bstack11ll11ll1l1_opy_(bstack1l1lll1_opy_ (u"ࠣࡽࢀࡃࡧࡻࡩ࡭ࡦࡑࡥࡲ࡫࠽ࡼࡿࠩࡦࡺ࡯࡬ࡥࡔࡸࡲࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲ࠾ࡽࢀࠪࡵࡸ࡯࡫ࡧࡦࡸࡓࡧ࡭ࡦ࠿ࡾࢁࠧ᜿").format(self.bstack11ll1111l11_opy_, self.config.get(bstack1l1lll1_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡏࡣࡰࡩࠬᝀ")), os.environ.get(bstack1l1lll1_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡅ࡙ࡎࡒࡄࡠࡔࡘࡒࡤࡏࡄࡆࡐࡗࡍࡋࡏࡅࡓࠩᝁ")), self.config.get(bstack1l1lll1_opy_ (u"ࠫࡵࡸ࡯࡫ࡧࡦࡸࡓࡧ࡭ࡦࠩᝂ"))))
            if response.get(bstack1l1lll1_opy_ (u"ࠧࡹࡴࡢࡶࡸࡷࠧᝃ")) == 200:
                failed_count = response.get(bstack1l1lll1_opy_ (u"ࠨࡦࡢ࡫࡯ࡩࡩ࡚ࡥࡴࡶࡶࡇࡴࡻ࡮ࡵࠤᝄ"), 0)
                self.logger.debug(bstack1l1lll1_opy_ (u"ࠢࡑࡱ࡯ࡰࡪࡪࠠࡧࡣ࡬ࡰࡪࡪࠠࡵࡧࡶࡸࡸࠦࡣࡰࡷࡱࡸ࠿ࠦࡻࡾࠤᝅ").format(failed_count))
                if failed_count >= self.bstack11l1llll1l1_opy_:
                    self.logger.info(bstack1l1lll1_opy_ (u"ࠣࡖ࡫ࡶࡪࡹࡨࡰ࡮ࡧࠤࡨࡸ࡯ࡴࡵࡨࡨ࠿ࠦࡻࡾࠢࡁࡁࠥࢁࡽࠣᝆ").format(failed_count, self.bstack11l1llll1l1_opy_))
                    self.bstack11l1lllll11_opy_(failed_count)
                    self.bstack11l1lllllll_opy_ = True
            else:
                self.logger.error(bstack1l1lll1_opy_ (u"ࠤࡉࡥ࡮ࡲࡥࡥࠢࡷࡳࠥࡶ࡯࡭࡮ࠣࡪࡦ࡯࡬ࡦࡦࠣࡸࡪࡹࡴࡴ࠼ࠣࡿࢂࠨᝇ").format(response))
        except Exception as e:
            self.logger.error(bstack1l1lll1_opy_ (u"ࠥࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡤࡶࡴ࡬ࡲ࡬ࠦࡰࡰ࡮࡯࡭ࡳ࡭࠺ࠡࡽࢀࠦᝈ").format(e))
    def bstack11l1lllll11_opy_(self, failed_count):
        with open(self.bstack11ll1111ll1_opy_, bstack1l1lll1_opy_ (u"ࠦࡼࠨᝉ")) as f:
            f.write(bstack1l1lll1_opy_ (u"࡚ࠧࡨࡳࡧࡶ࡬ࡴࡲࡤࠡࡥࡵࡳࡸࡹࡥࡥࠢࡤࡸࠥࢁࡽ࡝ࡰࠥᝊ").format(datetime.now()))
            f.write(bstack1l1lll1_opy_ (u"ࠨࡆࡢ࡫࡯ࡩࡩࠦࡴࡦࡵࡷࡷࠥࡩ࡯ࡶࡰࡷ࠾ࠥࢁࡽ࡝ࡰࠥᝋ").format(failed_count))
        self.logger.debug(bstack1l1lll1_opy_ (u"ࠢࡂࡤࡲࡶࡹࠦࡂࡶ࡫࡯ࡨࠥ࡬ࡩ࡭ࡧࠣࡧࡷ࡫ࡡࡵࡧࡧ࠾ࠥࢁࡽࠣᝌ").format(self.bstack11ll1111ll1_opy_))
    def bstack11l1lll1ll1_opy_(self):
        def bstack11ll1111lll_opy_():
            while not self.bstack11l1lllllll_opy_:
                time.sleep(bstack11l1lll1lll_opy_)
                self.bstack11l1lllll1l_opy_()
                self.bstack11ll11ll1l1_opy_()
        bstack11ll111l111_opy_ = threading.Thread(target=bstack11ll1111lll_opy_, daemon=True)
        bstack11ll111l111_opy_.start()