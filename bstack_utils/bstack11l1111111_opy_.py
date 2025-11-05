# coding: UTF-8
import sys
bstack1111l1_opy_ = sys.version_info [0] == 2
bstack1l1ll11_opy_ = 2048
bstack11l11l_opy_ = 7
def bstack11111_opy_ (bstack11lll_opy_):
    global bstack111l1l1_opy_
    bstack1l1l1_opy_ = ord (bstack11lll_opy_ [-1])
    bstack1l111ll_opy_ = bstack11lll_opy_ [:-1]
    bstack1l1l11_opy_ = bstack1l1l1_opy_ % len (bstack1l111ll_opy_)
    bstack1l11l11_opy_ = bstack1l111ll_opy_ [:bstack1l1l11_opy_] + bstack1l111ll_opy_ [bstack1l1l11_opy_:]
    if bstack1111l1_opy_:
        bstack1llll11_opy_ = unicode () .join ([unichr (ord (char) - bstack1l1ll11_opy_ - (bstack1111ll1_opy_ + bstack1l1l1_opy_) % bstack11l11l_opy_) for bstack1111ll1_opy_, char in enumerate (bstack1l11l11_opy_)])
    else:
        bstack1llll11_opy_ = str () .join ([chr (ord (char) - bstack1l1ll11_opy_ - (bstack1111ll1_opy_ + bstack1l1l1_opy_) % bstack11l11l_opy_) for bstack1111ll1_opy_, char in enumerate (bstack1l11l11_opy_)])
    return eval (bstack1llll11_opy_)
import threading
import tempfile
import os
import time
from datetime import datetime
from bstack_utils.bstack11ll1ll111l_opy_ import bstack11ll1l1l111_opy_
from bstack_utils.constants import bstack11ll1ll11ll_opy_, bstack1lllll1l11_opy_
from bstack_utils.bstack1lll1ll11_opy_ import bstack111l11ll_opy_
from bstack_utils import bstack111111l11l_opy_
bstack11l1ll1l1ll_opy_ = 10
class bstack111ll1lll_opy_:
    def __init__(self, bstack111ll1ll1l_opy_, config, bstack11l1lll1lll_opy_=0):
        self.bstack11l1ll1l111_opy_ = set()
        self.lock = threading.Lock()
        self.bstack11l1ll11lll_opy_ = bstack11111_opy_ (u"ࠢࡼࡿ࠲ࡸࡪࡹࡴࡰࡴࡦ࡬ࡪࡹࡴࡳࡣࡷ࡭ࡴࡴ࠯ࡢࡲ࡬࠳ࡻ࠷࠯ࡧࡣ࡬ࡰࡪࡪ࠭ࡵࡧࡶࡸࡸࠨᝨ").format(bstack11ll1ll11ll_opy_)
        self.bstack11l1lll1l11_opy_ = os.path.join(tempfile.gettempdir(), bstack11111_opy_ (u"ࠣࡣࡥࡳࡷࡺ࡟ࡣࡷ࡬ࡰࡩࡥࡻࡾࠤᝩ").format(os.environ.get(bstack11111_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡎࡕࡃࡡࡘ࡙ࡎࡊࠧᝪ"))))
        self.bstack11l1lll1l1l_opy_ = os.path.join(tempfile.gettempdir(), bstack11111_opy_ (u"ࠥࡪࡦ࡯࡬ࡦࡦࡢࡸࡪࡹࡴࡴࡡࡾࢁ࠳ࡺࡸࡵࠤᝫ").format(os.environ.get(bstack11111_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡉࡗࡅࡣ࡚࡛ࡉࡅࠩᝬ"))))
        self.bstack11l1lll1111_opy_ = 2
        self.bstack111ll1ll1l_opy_ = bstack111ll1ll1l_opy_
        self.config = config
        self.logger = bstack111111l11l_opy_.get_logger(__name__, bstack1lllll1l11_opy_)
        self.bstack11l1lll1lll_opy_ = bstack11l1lll1lll_opy_
        self.bstack11l1lll11l1_opy_ = False
        self.bstack11l1lll11ll_opy_ = not (
                            os.environ.get(bstack11111_opy_ (u"ࠧࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡇ࡛ࡉࡍࡆࡢࡖ࡚ࡔ࡟ࡊࡆࡈࡒ࡙ࡏࡆࡊࡇࡕࠦ᝭")) and
                            os.environ.get(bstack11111_opy_ (u"ࠨࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡔࡏࡅࡇࡢࡍࡓࡊࡅ࡙ࠤᝮ")) and
                            os.environ.get(bstack11111_opy_ (u"ࠢࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡐࡖࡄࡐࡤࡔࡏࡅࡇࡢࡇࡔ࡛ࡎࡕࠤᝯ"))
                        )
        if bstack111l11ll_opy_.bstack11l1ll1ll11_opy_(config):
            self.bstack11l1lll1111_opy_ = bstack111l11ll_opy_.bstack11l1ll1lll1_opy_(config, self.bstack11l1lll1lll_opy_)
            self.bstack11l1ll1l11l_opy_()
    def bstack11l1ll1llll_opy_(self):
        return bstack11111_opy_ (u"ࠣࡽࢀࡣࢀࢃࠢᝰ").format(self.config.get(bstack11111_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡏࡣࡰࡩࠬ᝱")), os.environ.get(bstack11111_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡅ࡙ࡎࡒࡄࡠࡔࡘࡒࡤࡏࡄࡆࡐࡗࡍࡋࡏࡅࡓࠩᝲ")))
    def bstack11l1llll111_opy_(self):
        try:
            if self.bstack11l1lll11ll_opy_:
                return
            with self.lock:
                try:
                    with open(self.bstack11l1lll1l1l_opy_, bstack11111_opy_ (u"ࠦࡷࠨᝳ")) as f:
                        bstack11l1ll11l1l_opy_ = set(line.strip() for line in f if line.strip())
                except FileNotFoundError:
                    bstack11l1ll11l1l_opy_ = set()
                bstack11l1lll1ll1_opy_ = bstack11l1ll11l1l_opy_ - self.bstack11l1ll1l111_opy_
                if not bstack11l1lll1ll1_opy_:
                    return
                self.bstack11l1ll1l111_opy_.update(bstack11l1lll1ll1_opy_)
                data = {bstack11111_opy_ (u"ࠧ࡬ࡡࡪ࡮ࡨࡨ࡙࡫ࡳࡵࡵࠥ᝴"): list(self.bstack11l1ll1l111_opy_), bstack11111_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡓࡧ࡭ࡦࠤ᝵"): self.config.get(bstack11111_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡔࡡ࡮ࡧࠪ᝶")), bstack11111_opy_ (u"ࠣࡤࡸ࡭ࡱࡪࡒࡶࡰࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷࠨ᝷"): os.environ.get(bstack11111_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡄࡘࡍࡑࡊ࡟ࡓࡗࡑࡣࡎࡊࡅࡏࡖࡌࡊࡎࡋࡒࠨ᝸")), bstack11111_opy_ (u"ࠥࡴࡷࡵࡪࡦࡥࡷࡒࡦࡳࡥࠣ᝹"): self.config.get(bstack11111_opy_ (u"ࠫࡵࡸ࡯࡫ࡧࡦࡸࡓࡧ࡭ࡦࠩ᝺"))}
            response = bstack11ll1l1l111_opy_.bstack11ll1111ll1_opy_(self.bstack11l1ll11lll_opy_, data)
            if response.get(bstack11111_opy_ (u"ࠧࡹࡴࡢࡶࡸࡷࠧ᝻")) == 200:
                self.logger.debug(bstack11111_opy_ (u"ࠨࡓࡶࡥࡦࡩࡸࡹࡦࡶ࡮࡯ࡽࠥࡹࡥ࡯ࡶࠣࡪࡦ࡯࡬ࡦࡦࠣࡸࡪࡹࡴࡴ࠼ࠣࡿࢂࠨ᝼").format(data))
            else:
                self.logger.debug(bstack11111_opy_ (u"ࠢࡇࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡷࡪࡴࡤࠡࡨࡤ࡭ࡱ࡫ࡤࠡࡶࡨࡷࡹࡹ࠺ࠡࡽࢀࠦ᝽").format(response))
        except Exception as e:
            self.logger.debug(bstack11111_opy_ (u"ࠣࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤࡩࡻࡲࡪࡰࡪࠤࡸ࡫࡮ࡥ࡫ࡱ࡫ࠥ࡬ࡡࡪ࡮ࡨࡨࠥࡺࡥࡴࡶࡶ࠾ࠥࢁࡽࠣ᝾").format(e))
    def bstack11ll11111ll_opy_(self):
        if self.bstack11l1lll11ll_opy_:
            with self.lock:
                try:
                    with open(self.bstack11l1lll1l1l_opy_, bstack11111_opy_ (u"ࠤࡵࠦ᝿")) as f:
                        bstack11l1lll111l_opy_ = set(line.strip() for line in f if line.strip())
                    failed_count = len(bstack11l1lll111l_opy_)
                except FileNotFoundError:
                    failed_count = 0
                self.logger.debug(bstack11111_opy_ (u"ࠥࡔࡴࡲ࡬ࡦࡦࠣࡪࡦ࡯࡬ࡦࡦࠣࡸࡪࡹࡴࡴࠢࡦࡳࡺࡴࡴࠡࠪ࡯ࡳࡨࡧ࡬ࠪ࠼ࠣࡿࢂࠨក").format(failed_count))
                if failed_count >= self.bstack11l1lll1111_opy_:
                    self.logger.info(bstack11111_opy_ (u"࡙ࠦ࡮ࡲࡦࡵ࡫ࡳࡱࡪࠠࡤࡴࡲࡷࡸ࡫ࡤࠡࠪ࡯ࡳࡨࡧ࡬ࠪ࠼ࠣࡿࢂࠦ࠾࠾ࠢࡾࢁࠧខ").format(failed_count, self.bstack11l1lll1111_opy_))
                    self.bstack11l1ll1ll1l_opy_(failed_count)
                    self.bstack11l1lll11l1_opy_ = True
            return
        try:
            response = bstack11ll1l1l111_opy_.bstack11ll11111ll_opy_(bstack11111_opy_ (u"ࠧࢁࡽࡀࡤࡸ࡭ࡱࡪࡎࡢ࡯ࡨࡁࢀࢃࠦࡣࡷ࡬ࡰࡩࡘࡵ࡯ࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࡂࢁࡽࠧࡲࡵࡳ࡯࡫ࡣࡵࡐࡤࡱࡪࡃࡻࡾࠤគ").format(self.bstack11l1ll11lll_opy_, self.config.get(bstack11111_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡓࡧ࡭ࡦࠩឃ")), os.environ.get(bstack11111_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡂࡖࡋࡏࡈࡤࡘࡕࡏࡡࡌࡈࡊࡔࡔࡊࡈࡌࡉࡗ࠭ង")), self.config.get(bstack11111_opy_ (u"ࠨࡲࡵࡳ࡯࡫ࡣࡵࡐࡤࡱࡪ࠭ច"))))
            if response.get(bstack11111_opy_ (u"ࠤࡶࡸࡦࡺࡵࡴࠤឆ")) == 200:
                failed_count = response.get(bstack11111_opy_ (u"ࠥࡪࡦ࡯࡬ࡦࡦࡗࡩࡸࡺࡳࡄࡱࡸࡲࡹࠨជ"), 0)
                self.logger.debug(bstack11111_opy_ (u"ࠦࡕࡵ࡬࡭ࡧࡧࠤ࡫ࡧࡩ࡭ࡧࡧࠤࡹ࡫ࡳࡵࡵࠣࡧࡴࡻ࡮ࡵ࠼ࠣࡿࢂࠨឈ").format(failed_count))
                if failed_count >= self.bstack11l1lll1111_opy_:
                    self.logger.info(bstack11111_opy_ (u"࡚ࠧࡨࡳࡧࡶ࡬ࡴࡲࡤࠡࡥࡵࡳࡸࡹࡥࡥ࠼ࠣࡿࢂࠦ࠾࠾ࠢࡾࢁࠧញ").format(failed_count, self.bstack11l1lll1111_opy_))
                    self.bstack11l1ll1ll1l_opy_(failed_count)
                    self.bstack11l1lll11l1_opy_ = True
            else:
                self.logger.error(bstack11111_opy_ (u"ࠨࡆࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡳࡳࡱࡲࠠࡧࡣ࡬ࡰࡪࡪࠠࡵࡧࡶࡸࡸࡀࠠࡼࡿࠥដ").format(response))
        except Exception as e:
            self.logger.error(bstack11111_opy_ (u"ࠢࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣࡨࡺࡸࡩ࡯ࡩࠣࡴࡴࡲ࡬ࡪࡰࡪ࠾ࠥࢁࡽࠣឋ").format(e))
    def bstack11l1ll1ll1l_opy_(self, failed_count):
        with open(self.bstack11l1lll1l11_opy_, bstack11111_opy_ (u"ࠣࡹࠥឌ")) as f:
            f.write(bstack11111_opy_ (u"ࠤࡗ࡬ࡷ࡫ࡳࡩࡱ࡯ࡨࠥࡩࡲࡰࡵࡶࡩࡩࠦࡡࡵࠢࡾࢁࡡࡴࠢឍ").format(datetime.now()))
            f.write(bstack11111_opy_ (u"ࠥࡊࡦ࡯࡬ࡦࡦࠣࡸࡪࡹࡴࡴࠢࡦࡳࡺࡴࡴ࠻ࠢࡾࢁࡡࡴࠢណ").format(failed_count))
        self.logger.debug(bstack11111_opy_ (u"ࠦࡆࡨ࡯ࡳࡶࠣࡆࡺ࡯࡬ࡥࠢࡩ࡭ࡱ࡫ࠠࡤࡴࡨࡥࡹ࡫ࡤ࠻ࠢࡾࢁࠧត").format(self.bstack11l1lll1l11_opy_))
    def bstack11l1ll1l11l_opy_(self):
        def bstack11l1ll11ll1_opy_():
            while not self.bstack11l1lll11l1_opy_:
                time.sleep(bstack11l1ll1l1ll_opy_)
                self.bstack11l1llll111_opy_()
                self.bstack11ll11111ll_opy_()
        bstack11l1ll1l1l1_opy_ = threading.Thread(target=bstack11l1ll11ll1_opy_, daemon=True)
        bstack11l1ll1l1l1_opy_.start()