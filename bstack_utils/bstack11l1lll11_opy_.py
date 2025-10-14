# coding: UTF-8
import sys
bstack1_opy_ = sys.version_info [0] == 2
bstack11l1ll1_opy_ = 2048
bstack1l1l1ll_opy_ = 7
def bstack11l1l11_opy_ (bstack111l1ll_opy_):
    global bstack1l1lll1_opy_
    bstack1l1l11_opy_ = ord (bstack111l1ll_opy_ [-1])
    bstack111l1l1_opy_ = bstack111l1ll_opy_ [:-1]
    bstack111ll_opy_ = bstack1l1l11_opy_ % len (bstack111l1l1_opy_)
    bstack11l11l1_opy_ = bstack111l1l1_opy_ [:bstack111ll_opy_] + bstack111l1l1_opy_ [bstack111ll_opy_:]
    if bstack1_opy_:
        bstack1111l1l_opy_ = unicode () .join ([unichr (ord (char) - bstack11l1ll1_opy_ - (bstack1l111ll_opy_ + bstack1l1l11_opy_) % bstack1l1l1ll_opy_) for bstack1l111ll_opy_, char in enumerate (bstack11l11l1_opy_)])
    else:
        bstack1111l1l_opy_ = str () .join ([chr (ord (char) - bstack11l1ll1_opy_ - (bstack1l111ll_opy_ + bstack1l1l11_opy_) % bstack1l1l1ll_opy_) for bstack1l111ll_opy_, char in enumerate (bstack11l11l1_opy_)])
    return eval (bstack1111l1l_opy_)
import threading
import tempfile
import os
import time
from datetime import datetime
from bstack_utils.bstack11lll111l1l_opy_ import bstack11ll1lllll1_opy_
from bstack_utils.constants import bstack11ll1llllll_opy_, bstack1l11lllll1_opy_
from bstack_utils.bstack1llll11l1_opy_ import bstack11l1l111_opy_
from bstack_utils import bstack1ll1111ll_opy_
bstack11ll1111l1l_opy_ = 10
class bstack11ll11lll_opy_:
    def __init__(self, bstack1111ll11ll_opy_, config, bstack11ll111111l_opy_=0):
        self.bstack11l1lllll1l_opy_ = set()
        self.lock = threading.Lock()
        self.bstack11ll1111lll_opy_ = bstack11l1l11_opy_ (u"ࠢࡼࡿ࠲ࡸࡪࡹࡴࡰࡴࡦ࡬ࡪࡹࡴࡳࡣࡷ࡭ࡴࡴ࠯ࡢࡲ࡬࠳ࡻ࠷࠯ࡧࡣ࡬ࡰࡪࡪ࠭ࡵࡧࡶࡸࡸࠨᜢ").format(bstack11ll1llllll_opy_)
        self.bstack11l1llll11l_opy_ = os.path.join(tempfile.gettempdir(), bstack11l1l11_opy_ (u"ࠣࡣࡥࡳࡷࡺ࡟ࡣࡷ࡬ࡰࡩࡥࡻࡾࠤᜣ").format(os.environ.get(bstack11l1l11_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡎࡕࡃࡡࡘ࡙ࡎࡊࠧᜤ"))))
        self.bstack11ll1111l11_opy_ = os.path.join(tempfile.gettempdir(), bstack11l1l11_opy_ (u"ࠥࡪࡦ࡯࡬ࡦࡦࡢࡸࡪࡹࡴࡴࡡࡾࢁ࠳ࡺࡸࡵࠤᜥ").format(os.environ.get(bstack11l1l11_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡉࡗࡅࡣ࡚࡛ࡉࡅࠩᜦ"))))
        self.bstack11ll1111111_opy_ = 2
        self.bstack1111ll11ll_opy_ = bstack1111ll11ll_opy_
        self.config = config
        self.logger = bstack1ll1111ll_opy_.get_logger(__name__, bstack1l11lllll1_opy_)
        self.bstack11ll111111l_opy_ = bstack11ll111111l_opy_
        self.bstack11l1llll1ll_opy_ = False
        self.bstack11ll111l11l_opy_ = not (
                            os.environ.get(bstack11l1l11_opy_ (u"ࠧࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡇ࡛ࡉࡍࡆࡢࡖ࡚ࡔ࡟ࡊࡆࡈࡒ࡙ࡏࡆࡊࡇࡕࠦᜧ")) and
                            os.environ.get(bstack11l1l11_opy_ (u"ࠨࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡔࡏࡅࡇࡢࡍࡓࡊࡅ࡙ࠤᜨ")) and
                            os.environ.get(bstack11l1l11_opy_ (u"ࠢࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡐࡖࡄࡐࡤࡔࡏࡅࡇࡢࡇࡔ࡛ࡎࡕࠤᜩ"))
                        )
        if bstack11l1l111_opy_.bstack11ll11111l1_opy_(config):
            self.bstack11ll1111111_opy_ = bstack11l1l111_opy_.bstack11l1llll111_opy_(config, self.bstack11ll111111l_opy_)
            self.bstack11ll111l1l1_opy_()
    def bstack11ll1111ll1_opy_(self):
        return bstack11l1l11_opy_ (u"ࠣࡽࢀࡣࢀࢃࠢᜪ").format(self.config.get(bstack11l1l11_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡏࡣࡰࡩࠬᜫ")), os.environ.get(bstack11l1l11_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡅ࡙ࡎࡒࡄࡠࡔࡘࡒࡤࡏࡄࡆࡐࡗࡍࡋࡏࡅࡓࠩᜬ")))
    def bstack11l1lllllll_opy_(self):
        try:
            if self.bstack11ll111l11l_opy_:
                return
            with self.lock:
                try:
                    with open(self.bstack11ll1111l11_opy_, bstack11l1l11_opy_ (u"ࠦࡷࠨᜭ")) as f:
                        bstack11ll11111ll_opy_ = set(line.strip() for line in f if line.strip())
                except FileNotFoundError:
                    bstack11ll11111ll_opy_ = set()
                bstack11l1lllll11_opy_ = bstack11ll11111ll_opy_ - self.bstack11l1lllll1l_opy_
                if not bstack11l1lllll11_opy_:
                    return
                self.bstack11l1lllll1l_opy_.update(bstack11l1lllll11_opy_)
                data = {bstack11l1l11_opy_ (u"ࠧ࡬ࡡࡪ࡮ࡨࡨ࡙࡫ࡳࡵࡵࠥᜮ"): list(self.bstack11l1lllll1l_opy_), bstack11l1l11_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡓࡧ࡭ࡦࠤᜯ"): self.config.get(bstack11l1l11_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡔࡡ࡮ࡧࠪᜰ")), bstack11l1l11_opy_ (u"ࠣࡤࡸ࡭ࡱࡪࡒࡶࡰࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷࠨᜱ"): os.environ.get(bstack11l1l11_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡄࡘࡍࡑࡊ࡟ࡓࡗࡑࡣࡎࡊࡅࡏࡖࡌࡊࡎࡋࡒࠨᜲ")), bstack11l1l11_opy_ (u"ࠥࡴࡷࡵࡪࡦࡥࡷࡒࡦࡳࡥࠣᜳ"): self.config.get(bstack11l1l11_opy_ (u"ࠫࡵࡸ࡯࡫ࡧࡦࡸࡓࡧ࡭ࡦ᜴ࠩ"))}
            response = bstack11ll1lllll1_opy_.bstack11ll11l11ll_opy_(self.bstack11ll1111lll_opy_, data)
            if response.get(bstack11l1l11_opy_ (u"ࠧࡹࡴࡢࡶࡸࡷࠧ᜵")) == 200:
                self.logger.debug(bstack11l1l11_opy_ (u"ࠨࡓࡶࡥࡦࡩࡸࡹࡦࡶ࡮࡯ࡽࠥࡹࡥ࡯ࡶࠣࡪࡦ࡯࡬ࡦࡦࠣࡸࡪࡹࡴࡴ࠼ࠣࡿࢂࠨ᜶").format(data))
            else:
                self.logger.debug(bstack11l1l11_opy_ (u"ࠢࡇࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡷࡪࡴࡤࠡࡨࡤ࡭ࡱ࡫ࡤࠡࡶࡨࡷࡹࡹ࠺ࠡࡽࢀࠦ᜷").format(response))
        except Exception as e:
            self.logger.debug(bstack11l1l11_opy_ (u"ࠣࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤࡩࡻࡲࡪࡰࡪࠤࡸ࡫࡮ࡥ࡫ࡱ࡫ࠥ࡬ࡡࡪ࡮ࡨࡨࠥࡺࡥࡴࡶࡶ࠾ࠥࢁࡽࠣ᜸").format(e))
    def bstack11ll11lll11_opy_(self):
        if self.bstack11ll111l11l_opy_:
            with self.lock:
                try:
                    with open(self.bstack11ll1111l11_opy_, bstack11l1l11_opy_ (u"ࠤࡵࠦ᜹")) as f:
                        bstack11ll111l111_opy_ = set(line.strip() for line in f if line.strip())
                    failed_count = len(bstack11ll111l111_opy_)
                except FileNotFoundError:
                    failed_count = 0
                self.logger.debug(bstack11l1l11_opy_ (u"ࠥࡔࡴࡲ࡬ࡦࡦࠣࡪࡦ࡯࡬ࡦࡦࠣࡸࡪࡹࡴࡴࠢࡦࡳࡺࡴࡴࠡࠪ࡯ࡳࡨࡧ࡬ࠪ࠼ࠣࡿࢂࠨ᜺").format(failed_count))
                if failed_count >= self.bstack11ll1111111_opy_:
                    self.logger.info(bstack11l1l11_opy_ (u"࡙ࠦ࡮ࡲࡦࡵ࡫ࡳࡱࡪࠠࡤࡴࡲࡷࡸ࡫ࡤࠡࠪ࡯ࡳࡨࡧ࡬ࠪ࠼ࠣࡿࢂࠦ࠾࠾ࠢࡾࢁࠧ᜻").format(failed_count, self.bstack11ll1111111_opy_))
                    self.bstack11l1lll1lll_opy_(failed_count)
                    self.bstack11l1llll1ll_opy_ = True
            return
        try:
            response = bstack11ll1lllll1_opy_.bstack11ll11lll11_opy_(bstack11l1l11_opy_ (u"ࠧࢁࡽࡀࡤࡸ࡭ࡱࡪࡎࡢ࡯ࡨࡁࢀࢃࠦࡣࡷ࡬ࡰࡩࡘࡵ࡯ࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࡂࢁࡽࠧࡲࡵࡳ࡯࡫ࡣࡵࡐࡤࡱࡪࡃࡻࡾࠤ᜼").format(self.bstack11ll1111lll_opy_, self.config.get(bstack11l1l11_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡓࡧ࡭ࡦࠩ᜽")), os.environ.get(bstack11l1l11_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡂࡖࡋࡏࡈࡤࡘࡕࡏࡡࡌࡈࡊࡔࡔࡊࡈࡌࡉࡗ࠭᜾")), self.config.get(bstack11l1l11_opy_ (u"ࠨࡲࡵࡳ࡯࡫ࡣࡵࡐࡤࡱࡪ࠭᜿"))))
            if response.get(bstack11l1l11_opy_ (u"ࠤࡶࡸࡦࡺࡵࡴࠤᝀ")) == 200:
                failed_count = response.get(bstack11l1l11_opy_ (u"ࠥࡪࡦ࡯࡬ࡦࡦࡗࡩࡸࡺࡳࡄࡱࡸࡲࡹࠨᝁ"), 0)
                self.logger.debug(bstack11l1l11_opy_ (u"ࠦࡕࡵ࡬࡭ࡧࡧࠤ࡫ࡧࡩ࡭ࡧࡧࠤࡹ࡫ࡳࡵࡵࠣࡧࡴࡻ࡮ࡵ࠼ࠣࡿࢂࠨᝂ").format(failed_count))
                if failed_count >= self.bstack11ll1111111_opy_:
                    self.logger.info(bstack11l1l11_opy_ (u"࡚ࠧࡨࡳࡧࡶ࡬ࡴࡲࡤࠡࡥࡵࡳࡸࡹࡥࡥ࠼ࠣࡿࢂࠦ࠾࠾ࠢࡾࢁࠧᝃ").format(failed_count, self.bstack11ll1111111_opy_))
                    self.bstack11l1lll1lll_opy_(failed_count)
                    self.bstack11l1llll1ll_opy_ = True
            else:
                self.logger.error(bstack11l1l11_opy_ (u"ࠨࡆࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡳࡳࡱࡲࠠࡧࡣ࡬ࡰࡪࡪࠠࡵࡧࡶࡸࡸࡀࠠࡼࡿࠥᝄ").format(response))
        except Exception as e:
            self.logger.error(bstack11l1l11_opy_ (u"ࠢࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣࡨࡺࡸࡩ࡯ࡩࠣࡴࡴࡲ࡬ࡪࡰࡪ࠾ࠥࢁࡽࠣᝅ").format(e))
    def bstack11l1lll1lll_opy_(self, failed_count):
        with open(self.bstack11l1llll11l_opy_, bstack11l1l11_opy_ (u"ࠣࡹࠥᝆ")) as f:
            f.write(bstack11l1l11_opy_ (u"ࠤࡗ࡬ࡷ࡫ࡳࡩࡱ࡯ࡨࠥࡩࡲࡰࡵࡶࡩࡩࠦࡡࡵࠢࡾࢁࡡࡴࠢᝇ").format(datetime.now()))
            f.write(bstack11l1l11_opy_ (u"ࠥࡊࡦ࡯࡬ࡦࡦࠣࡸࡪࡹࡴࡴࠢࡦࡳࡺࡴࡴ࠻ࠢࡾࢁࡡࡴࠢᝈ").format(failed_count))
        self.logger.debug(bstack11l1l11_opy_ (u"ࠦࡆࡨ࡯ࡳࡶࠣࡆࡺ࡯࡬ࡥࠢࡩ࡭ࡱ࡫ࠠࡤࡴࡨࡥࡹ࡫ࡤ࠻ࠢࡾࢁࠧᝉ").format(self.bstack11l1llll11l_opy_))
    def bstack11ll111l1l1_opy_(self):
        def bstack11l1llll1l1_opy_():
            while not self.bstack11l1llll1ll_opy_:
                time.sleep(bstack11ll1111l1l_opy_)
                self.bstack11l1lllllll_opy_()
                self.bstack11ll11lll11_opy_()
        bstack11l1llllll1_opy_ = threading.Thread(target=bstack11l1llll1l1_opy_, daemon=True)
        bstack11l1llllll1_opy_.start()