# coding: UTF-8
import sys
bstack1lll1l_opy_ = sys.version_info [0] == 2
bstack111l11l_opy_ = 2048
bstack1l1llll_opy_ = 7
def bstack111111l_opy_ (bstack1ll1_opy_):
    global bstack11l1ll_opy_
    bstack11ll1l_opy_ = ord (bstack1ll1_opy_ [-1])
    bstack11ll_opy_ = bstack1ll1_opy_ [:-1]
    bstack1lllll1_opy_ = bstack11ll1l_opy_ % len (bstack11ll_opy_)
    bstack111l1l1_opy_ = bstack11ll_opy_ [:bstack1lllll1_opy_] + bstack11ll_opy_ [bstack1lllll1_opy_:]
    if bstack1lll1l_opy_:
        bstack1111_opy_ = unicode () .join ([unichr (ord (char) - bstack111l11l_opy_ - (bstack1l1l1l_opy_ + bstack11ll1l_opy_) % bstack1l1llll_opy_) for bstack1l1l1l_opy_, char in enumerate (bstack111l1l1_opy_)])
    else:
        bstack1111_opy_ = str () .join ([chr (ord (char) - bstack111l11l_opy_ - (bstack1l1l1l_opy_ + bstack11ll1l_opy_) % bstack1l1llll_opy_) for bstack1l1l1l_opy_, char in enumerate (bstack111l1l1_opy_)])
    return eval (bstack1111_opy_)
import threading
import tempfile
import os
import time
from datetime import datetime
from bstack_utils.bstack11ll1lllll1_opy_ import bstack11lll111111_opy_
from bstack_utils.constants import bstack11lll11111l_opy_, bstack11111ll1l_opy_
from bstack_utils.bstack1111l1l1_opy_ import bstack1lll1ll11_opy_
from bstack_utils import bstack11111ll111_opy_
bstack11l1lllll1l_opy_ = 10
class bstack11l11ll1ll_opy_:
    def __init__(self, bstack1l1l111l1_opy_, config, bstack11l1llll111_opy_=0):
        self.bstack11ll111l111_opy_ = set()
        self.lock = threading.Lock()
        self.bstack11ll11111l1_opy_ = bstack111111l_opy_ (u"ࠦࢀࢃ࠯ࡵࡧࡶࡸࡴࡸࡣࡩࡧࡶࡸࡷࡧࡴࡪࡱࡱ࠳ࡦࡶࡩ࠰ࡸ࠴࠳࡫ࡧࡩ࡭ࡧࡧ࠱ࡹ࡫ࡳࡵࡵࠥᜟ").format(bstack11lll11111l_opy_)
        self.bstack11ll1111l1l_opy_ = os.path.join(tempfile.gettempdir(), bstack111111l_opy_ (u"ࠧࡧࡢࡰࡴࡷࡣࡧࡻࡩ࡭ࡦࡢࡿࢂࠨᜠ").format(os.environ.get(bstack111111l_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡕࡖࡋࡇࠫᜡ"))))
        self.bstack11ll111111l_opy_ = os.path.join(tempfile.gettempdir(), bstack111111l_opy_ (u"ࠢࡧࡣ࡬ࡰࡪࡪ࡟ࡵࡧࡶࡸࡸࡥࡻࡾ࠰ࡷࡼࡹࠨᜢ").format(os.environ.get(bstack111111l_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡍ࡛ࡂࡠࡗࡘࡍࡉ࠭ᜣ"))))
        self.bstack11ll111l11l_opy_ = 2
        self.bstack1l1l111l1_opy_ = bstack1l1l111l1_opy_
        self.config = config
        self.logger = bstack11111ll111_opy_.get_logger(__name__, bstack11111ll1l_opy_)
        self.bstack11l1llll111_opy_ = bstack11l1llll111_opy_
        self.bstack11ll1111ll1_opy_ = False
        self.bstack11l1llll1ll_opy_ = not (
                            os.environ.get(bstack111111l_opy_ (u"ࠤࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡄࡘࡍࡑࡊ࡟ࡓࡗࡑࡣࡎࡊࡅࡏࡖࡌࡊࡎࡋࡒࠣᜤ")) and
                            os.environ.get(bstack111111l_opy_ (u"ࠥࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡑࡓࡉࡋ࡟ࡊࡐࡇࡉ࡝ࠨᜥ")) and
                            os.environ.get(bstack111111l_opy_ (u"ࠦࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡔ࡚ࡁࡍࡡࡑࡓࡉࡋ࡟ࡄࡑࡘࡒ࡙ࠨᜦ"))
                        )
        if bstack1lll1ll11_opy_.bstack11l1llll11l_opy_(config):
            self.bstack11ll111l11l_opy_ = bstack1lll1ll11_opy_.bstack11l1lllllll_opy_(config, self.bstack11l1llll111_opy_)
            self.bstack11ll1111111_opy_()
    def bstack11l1lllll11_opy_(self):
        return bstack111111l_opy_ (u"ࠧࢁࡽࡠࡽࢀࠦᜧ").format(self.config.get(bstack111111l_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡓࡧ࡭ࡦࠩᜨ")), os.environ.get(bstack111111l_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡂࡖࡋࡏࡈࡤࡘࡕࡏࡡࡌࡈࡊࡔࡔࡊࡈࡌࡉࡗ࠭ᜩ")))
    def bstack11l1llllll1_opy_(self):
        try:
            if self.bstack11l1llll1ll_opy_:
                return
            with self.lock:
                try:
                    with open(self.bstack11ll111111l_opy_, bstack111111l_opy_ (u"ࠣࡴࠥᜪ")) as f:
                        bstack11ll111l1l1_opy_ = set(line.strip() for line in f if line.strip())
                except FileNotFoundError:
                    bstack11ll111l1l1_opy_ = set()
                bstack11ll1111lll_opy_ = bstack11ll111l1l1_opy_ - self.bstack11ll111l111_opy_
                if not bstack11ll1111lll_opy_:
                    return
                self.bstack11ll111l111_opy_.update(bstack11ll1111lll_opy_)
                data = {bstack111111l_opy_ (u"ࠤࡩࡥ࡮ࡲࡥࡥࡖࡨࡷࡹࡹࠢᜫ"): list(self.bstack11ll111l111_opy_), bstack111111l_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡐࡤࡱࡪࠨᜬ"): self.config.get(bstack111111l_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡑࡥࡲ࡫ࠧᜭ")), bstack111111l_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡖࡺࡴࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠥᜮ"): os.environ.get(bstack111111l_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡈࡕࡊࡎࡇࡣࡗ࡛ࡎࡠࡋࡇࡉࡓ࡚ࡉࡇࡋࡈࡖࠬᜯ")), bstack111111l_opy_ (u"ࠢࡱࡴࡲ࡮ࡪࡩࡴࡏࡣࡰࡩࠧᜰ"): self.config.get(bstack111111l_opy_ (u"ࠨࡲࡵࡳ࡯࡫ࡣࡵࡐࡤࡱࡪ࠭ᜱ"))}
            response = bstack11lll111111_opy_.bstack11ll11ll1ll_opy_(self.bstack11ll11111l1_opy_, data)
            if response.get(bstack111111l_opy_ (u"ࠤࡶࡸࡦࡺࡵࡴࠤᜲ")) == 200:
                self.logger.debug(bstack111111l_opy_ (u"ࠥࡗࡺࡩࡣࡦࡵࡶࡪࡺࡲ࡬ࡺࠢࡶࡩࡳࡺࠠࡧࡣ࡬ࡰࡪࡪࠠࡵࡧࡶࡸࡸࡀࠠࡼࡿࠥᜳ").format(data))
            else:
                self.logger.debug(bstack111111l_opy_ (u"ࠦࡋࡧࡩ࡭ࡧࡧࠤࡹࡵࠠࡴࡧࡱࡨࠥ࡬ࡡࡪ࡮ࡨࡨࠥࡺࡥࡴࡶࡶ࠾ࠥࢁࡽ᜴ࠣ").format(response))
        except Exception as e:
            self.logger.debug(bstack111111l_opy_ (u"ࠧࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡࡦࡸࡶ࡮ࡴࡧࠡࡵࡨࡲࡩ࡯࡮ࡨࠢࡩࡥ࡮ࡲࡥࡥࠢࡷࡩࡸࡺࡳ࠻ࠢࡾࢁࠧ᜵").format(e))
    def bstack11ll11lll11_opy_(self):
        if self.bstack11l1llll1ll_opy_:
            with self.lock:
                try:
                    with open(self.bstack11ll111111l_opy_, bstack111111l_opy_ (u"ࠨࡲࠣ᜶")) as f:
                        bstack11l1lll1lll_opy_ = set(line.strip() for line in f if line.strip())
                    failed_count = len(bstack11l1lll1lll_opy_)
                except FileNotFoundError:
                    failed_count = 0
                self.logger.debug(bstack111111l_opy_ (u"ࠢࡑࡱ࡯ࡰࡪࡪࠠࡧࡣ࡬ࡰࡪࡪࠠࡵࡧࡶࡸࡸࠦࡣࡰࡷࡱࡸࠥ࠮࡬ࡰࡥࡤࡰ࠮ࡀࠠࡼࡿࠥ᜷").format(failed_count))
                if failed_count >= self.bstack11ll111l11l_opy_:
                    self.logger.info(bstack111111l_opy_ (u"ࠣࡖ࡫ࡶࡪࡹࡨࡰ࡮ࡧࠤࡨࡸ࡯ࡴࡵࡨࡨࠥ࠮࡬ࡰࡥࡤࡰ࠮ࡀࠠࡼࡿࠣࡂࡂࠦࡻࡾࠤ᜸").format(failed_count, self.bstack11ll111l11l_opy_))
                    self.bstack11ll11111ll_opy_(failed_count)
                    self.bstack11ll1111ll1_opy_ = True
            return
        try:
            response = bstack11lll111111_opy_.bstack11ll11lll11_opy_(bstack111111l_opy_ (u"ࠤࡾࢁࡄࡨࡵࡪ࡮ࡧࡒࡦࡳࡥ࠾ࡽࢀࠪࡧࡻࡩ࡭ࡦࡕࡹࡳࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳ࠿ࡾࢁࠫࡶࡲࡰ࡬ࡨࡧࡹࡔࡡ࡮ࡧࡀࡿࢂࠨ᜹").format(self.bstack11ll11111l1_opy_, self.config.get(bstack111111l_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡐࡤࡱࡪ࠭᜺")), os.environ.get(bstack111111l_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡆ࡚ࡏࡌࡅࡡࡕ࡙ࡓࡥࡉࡅࡇࡑࡘࡎࡌࡉࡆࡔࠪ᜻")), self.config.get(bstack111111l_opy_ (u"ࠬࡶࡲࡰ࡬ࡨࡧࡹࡔࡡ࡮ࡧࠪ᜼"))))
            if response.get(bstack111111l_opy_ (u"ࠨࡳࡵࡣࡷࡹࡸࠨ᜽")) == 200:
                failed_count = response.get(bstack111111l_opy_ (u"ࠢࡧࡣ࡬ࡰࡪࡪࡔࡦࡵࡷࡷࡈࡵࡵ࡯ࡶࠥ᜾"), 0)
                self.logger.debug(bstack111111l_opy_ (u"ࠣࡒࡲࡰࡱ࡫ࡤࠡࡨࡤ࡭ࡱ࡫ࡤࠡࡶࡨࡷࡹࡹࠠࡤࡱࡸࡲࡹࡀࠠࡼࡿࠥ᜿").format(failed_count))
                if failed_count >= self.bstack11ll111l11l_opy_:
                    self.logger.info(bstack111111l_opy_ (u"ࠤࡗ࡬ࡷ࡫ࡳࡩࡱ࡯ࡨࠥࡩࡲࡰࡵࡶࡩࡩࡀࠠࡼࡿࠣࡂࡂࠦࡻࡾࠤᝀ").format(failed_count, self.bstack11ll111l11l_opy_))
                    self.bstack11ll11111ll_opy_(failed_count)
                    self.bstack11ll1111ll1_opy_ = True
            else:
                self.logger.error(bstack111111l_opy_ (u"ࠥࡊࡦ࡯࡬ࡦࡦࠣࡸࡴࠦࡰࡰ࡮࡯ࠤ࡫ࡧࡩ࡭ࡧࡧࠤࡹ࡫ࡳࡵࡵ࠽ࠤࢀࢃࠢᝁ").format(response))
        except Exception as e:
            self.logger.error(bstack111111l_opy_ (u"ࠦࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡥࡷࡵ࡭ࡳ࡭ࠠࡱࡱ࡯ࡰ࡮ࡴࡧ࠻ࠢࡾࢁࠧᝂ").format(e))
    def bstack11ll11111ll_opy_(self, failed_count):
        with open(self.bstack11ll1111l1l_opy_, bstack111111l_opy_ (u"ࠧࡽࠢᝃ")) as f:
            f.write(bstack111111l_opy_ (u"ࠨࡔࡩࡴࡨࡷ࡭ࡵ࡬ࡥࠢࡦࡶࡴࡹࡳࡦࡦࠣࡥࡹࠦࡻࡾ࡞ࡱࠦᝄ").format(datetime.now()))
            f.write(bstack111111l_opy_ (u"ࠢࡇࡣ࡬ࡰࡪࡪࠠࡵࡧࡶࡸࡸࠦࡣࡰࡷࡱࡸ࠿ࠦࡻࡾ࡞ࡱࠦᝅ").format(failed_count))
        self.logger.debug(bstack111111l_opy_ (u"ࠣࡃࡥࡳࡷࡺࠠࡃࡷ࡬ࡰࡩࠦࡦࡪ࡮ࡨࠤࡨࡸࡥࡢࡶࡨࡨ࠿ࠦࡻࡾࠤᝆ").format(self.bstack11ll1111l1l_opy_))
    def bstack11ll1111111_opy_(self):
        def bstack11ll1111l11_opy_():
            while not self.bstack11ll1111ll1_opy_:
                time.sleep(bstack11l1lllll1l_opy_)
                self.bstack11l1llllll1_opy_()
                self.bstack11ll11lll11_opy_()
        bstack11l1llll1l1_opy_ = threading.Thread(target=bstack11ll1111l11_opy_, daemon=True)
        bstack11l1llll1l1_opy_.start()