# coding: UTF-8
import sys
bstack111ll1_opy_ = sys.version_info [0] == 2
bstack1l11l1_opy_ = 2048
bstack11111l_opy_ = 7
def bstack1ll1ll1_opy_ (bstack11lll1l_opy_):
    global bstack1ll11l1_opy_
    bstack1l1ll_opy_ = ord (bstack11lll1l_opy_ [-1])
    bstack1ll1l1l_opy_ = bstack11lll1l_opy_ [:-1]
    bstack1l1l1ll_opy_ = bstack1l1ll_opy_ % len (bstack1ll1l1l_opy_)
    bstack11ll1ll_opy_ = bstack1ll1l1l_opy_ [:bstack1l1l1ll_opy_] + bstack1ll1l1l_opy_ [bstack1l1l1ll_opy_:]
    if bstack111ll1_opy_:
        bstack111ll_opy_ = unicode () .join ([unichr (ord (char) - bstack1l11l1_opy_ - (bstack111111l_opy_ + bstack1l1ll_opy_) % bstack11111l_opy_) for bstack111111l_opy_, char in enumerate (bstack11ll1ll_opy_)])
    else:
        bstack111ll_opy_ = str () .join ([chr (ord (char) - bstack1l11l1_opy_ - (bstack111111l_opy_ + bstack1l1ll_opy_) % bstack11111l_opy_) for bstack111111l_opy_, char in enumerate (bstack11ll1ll_opy_)])
    return eval (bstack111ll_opy_)
import threading
import tempfile
import os
import time
from datetime import datetime
from bstack_utils.bstack11lll11ll1l_opy_ import bstack11lll11ll11_opy_
from bstack_utils.constants import bstack11lll1111l1_opy_, bstack11ll1lll1l_opy_
from bstack_utils.bstack111l1lll_opy_ import bstack1llll111l_opy_
from bstack_utils import bstack1l1l1ll111_opy_
bstack11ll1111111_opy_ = 10
class bstack1ll11l1ll_opy_:
    def __init__(self, bstack11l1lll1l1_opy_, config, bstack11ll1111l1l_opy_=0):
        self.bstack11l1lllll11_opy_ = set()
        self.lock = threading.Lock()
        self.bstack11l1llll1ll_opy_ = bstack1ll1ll1_opy_ (u"ࠥࡿࢂ࠵ࡴࡦࡵࡷࡳࡷࡩࡨࡦࡵࡷࡶࡦࡺࡩࡰࡰ࠲ࡥࡵ࡯࠯ࡷ࠳࠲ࡪࡦ࡯࡬ࡦࡦ࠰ࡸࡪࡹࡴࡴࠤᜬ").format(bstack11lll1111l1_opy_)
        self.bstack11ll111l11l_opy_ = os.path.join(tempfile.gettempdir(), bstack1ll1ll1_opy_ (u"ࠦࡦࡨ࡯ࡳࡶࡢࡦࡺ࡯࡬ࡥࡡࡾࢁࠧᜭ").format(os.environ.get(bstack1ll1ll1_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡊࡘࡆࡤ࡛ࡕࡊࡆࠪᜮ"))))
        self.bstack11ll1111lll_opy_ = os.path.join(tempfile.gettempdir(), bstack1ll1ll1_opy_ (u"ࠨࡦࡢ࡫࡯ࡩࡩࡥࡴࡦࡵࡷࡷࡤࢁࡽ࠯ࡶࡻࡸࠧᜯ").format(os.environ.get(bstack1ll1ll1_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡖࡗࡌࡈࠬᜰ"))))
        self.bstack11ll111111l_opy_ = 2
        self.bstack11l1lll1l1_opy_ = bstack11l1lll1l1_opy_
        self.config = config
        self.logger = bstack1l1l1ll111_opy_.get_logger(__name__, bstack11ll1lll1l_opy_)
        self.bstack11ll1111l1l_opy_ = bstack11ll1111l1l_opy_
        self.bstack11ll1111l11_opy_ = False
        self.bstack11l1llllll1_opy_ = not (
                            os.environ.get(bstack1ll1ll1_opy_ (u"ࠣࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡃࡗࡌࡐࡉࡥࡒࡖࡐࡢࡍࡉࡋࡎࡕࡋࡉࡍࡊࡘࠢᜱ")) and
                            os.environ.get(bstack1ll1ll1_opy_ (u"ࠤࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡐࡒࡈࡊࡥࡉࡏࡆࡈ࡜ࠧᜲ")) and
                            os.environ.get(bstack1ll1ll1_opy_ (u"ࠥࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡓ࡙ࡇࡌࡠࡐࡒࡈࡊࡥࡃࡐࡗࡑࡘࠧᜳ"))
                        )
        if bstack1llll111l_opy_.bstack11ll111l111_opy_(config):
            self.bstack11ll111111l_opy_ = bstack1llll111l_opy_.bstack11l1lllll1l_opy_(config, self.bstack11ll1111l1l_opy_)
            self.bstack11ll11111ll_opy_()
    def bstack11ll1111ll1_opy_(self):
        return bstack1ll1ll1_opy_ (u"ࠦࢀࢃ࡟ࡼࡿ᜴ࠥ").format(self.config.get(bstack1ll1ll1_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡒࡦࡳࡥࠨ᜵")), os.environ.get(bstack1ll1ll1_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡈࡕࡊࡎࡇࡣࡗ࡛ࡎࡠࡋࡇࡉࡓ࡚ࡉࡇࡋࡈࡖࠬ᜶")))
    def bstack11ll111l1l1_opy_(self):
        try:
            if self.bstack11l1llllll1_opy_:
                return
            with self.lock:
                try:
                    with open(self.bstack11ll1111lll_opy_, bstack1ll1ll1_opy_ (u"ࠢࡳࠤ᜷")) as f:
                        bstack11l1llll11l_opy_ = set(line.strip() for line in f if line.strip())
                except FileNotFoundError:
                    bstack11l1llll11l_opy_ = set()
                bstack11l1lllllll_opy_ = bstack11l1llll11l_opy_ - self.bstack11l1lllll11_opy_
                if not bstack11l1lllllll_opy_:
                    return
                self.bstack11l1lllll11_opy_.update(bstack11l1lllllll_opy_)
                data = {bstack1ll1ll1_opy_ (u"ࠣࡨࡤ࡭ࡱ࡫ࡤࡕࡧࡶࡸࡸࠨ᜸"): list(self.bstack11l1lllll11_opy_), bstack1ll1ll1_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡏࡣࡰࡩࠧ᜹"): self.config.get(bstack1ll1ll1_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡐࡤࡱࡪ࠭᜺")), bstack1ll1ll1_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡕࡹࡳࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠤ᜻"): os.environ.get(bstack1ll1ll1_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡇ࡛ࡉࡍࡆࡢࡖ࡚ࡔ࡟ࡊࡆࡈࡒ࡙ࡏࡆࡊࡇࡕࠫ᜼")), bstack1ll1ll1_opy_ (u"ࠨࡰࡳࡱ࡭ࡩࡨࡺࡎࡢ࡯ࡨࠦ᜽"): self.config.get(bstack1ll1ll1_opy_ (u"ࠧࡱࡴࡲ࡮ࡪࡩࡴࡏࡣࡰࡩࠬ᜾"))}
            response = bstack11lll11ll11_opy_.bstack11ll11l1lll_opy_(self.bstack11l1llll1ll_opy_, data)
            if response.get(bstack1ll1ll1_opy_ (u"ࠣࡵࡷࡥࡹࡻࡳࠣ᜿")) == 200:
                self.logger.debug(bstack1ll1ll1_opy_ (u"ࠤࡖࡹࡨࡩࡥࡴࡵࡩࡹࡱࡲࡹࠡࡵࡨࡲࡹࠦࡦࡢ࡫࡯ࡩࡩࠦࡴࡦࡵࡷࡷ࠿ࠦࡻࡾࠤᝀ").format(data))
            else:
                self.logger.debug(bstack1ll1ll1_opy_ (u"ࠥࡊࡦ࡯࡬ࡦࡦࠣࡸࡴࠦࡳࡦࡰࡧࠤ࡫ࡧࡩ࡭ࡧࡧࠤࡹ࡫ࡳࡵࡵ࠽ࠤࢀࢃࠢᝁ").format(response))
        except Exception as e:
            self.logger.debug(bstack1ll1ll1_opy_ (u"ࠦࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡥࡷࡵ࡭ࡳ࡭ࠠࡴࡧࡱࡨ࡮ࡴࡧࠡࡨࡤ࡭ࡱ࡫ࡤࠡࡶࡨࡷࡹࡹ࠺ࠡࡽࢀࠦᝂ").format(e))
    def bstack11ll11lll11_opy_(self):
        if self.bstack11l1llllll1_opy_:
            with self.lock:
                try:
                    with open(self.bstack11ll1111lll_opy_, bstack1ll1ll1_opy_ (u"ࠧࡸࠢᝃ")) as f:
                        bstack11ll111ll11_opy_ = set(line.strip() for line in f if line.strip())
                    failed_count = len(bstack11ll111ll11_opy_)
                except FileNotFoundError:
                    failed_count = 0
                self.logger.debug(bstack1ll1ll1_opy_ (u"ࠨࡐࡰ࡮࡯ࡩࡩࠦࡦࡢ࡫࡯ࡩࡩࠦࡴࡦࡵࡷࡷࠥࡩ࡯ࡶࡰࡷࠤ࠭ࡲ࡯ࡤࡣ࡯࠭࠿ࠦࡻࡾࠤᝄ").format(failed_count))
                if failed_count >= self.bstack11ll111111l_opy_:
                    self.logger.info(bstack1ll1ll1_opy_ (u"ࠢࡕࡪࡵࡩࡸ࡮࡯࡭ࡦࠣࡧࡷࡵࡳࡴࡧࡧࠤ࠭ࡲ࡯ࡤࡣ࡯࠭࠿ࠦࡻࡾࠢࡁࡁࠥࢁࡽࠣᝅ").format(failed_count, self.bstack11ll111111l_opy_))
                    self.bstack11l1llll1l1_opy_(failed_count)
                    self.bstack11ll1111l11_opy_ = True
            return
        try:
            response = bstack11lll11ll11_opy_.bstack11ll11lll11_opy_(bstack1ll1ll1_opy_ (u"ࠣࡽࢀࡃࡧࡻࡩ࡭ࡦࡑࡥࡲ࡫࠽ࡼࡿࠩࡦࡺ࡯࡬ࡥࡔࡸࡲࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲ࠾ࡽࢀࠪࡵࡸ࡯࡫ࡧࡦࡸࡓࡧ࡭ࡦ࠿ࡾࢁࠧᝆ").format(self.bstack11l1llll1ll_opy_, self.config.get(bstack1ll1ll1_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡏࡣࡰࡩࠬᝇ")), os.environ.get(bstack1ll1ll1_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡅ࡙ࡎࡒࡄࡠࡔࡘࡒࡤࡏࡄࡆࡐࡗࡍࡋࡏࡅࡓࠩᝈ")), self.config.get(bstack1ll1ll1_opy_ (u"ࠫࡵࡸ࡯࡫ࡧࡦࡸࡓࡧ࡭ࡦࠩᝉ"))))
            if response.get(bstack1ll1ll1_opy_ (u"ࠧࡹࡴࡢࡶࡸࡷࠧᝊ")) == 200:
                failed_count = response.get(bstack1ll1ll1_opy_ (u"ࠨࡦࡢ࡫࡯ࡩࡩ࡚ࡥࡴࡶࡶࡇࡴࡻ࡮ࡵࠤᝋ"), 0)
                self.logger.debug(bstack1ll1ll1_opy_ (u"ࠢࡑࡱ࡯ࡰࡪࡪࠠࡧࡣ࡬ࡰࡪࡪࠠࡵࡧࡶࡸࡸࠦࡣࡰࡷࡱࡸ࠿ࠦࡻࡾࠤᝌ").format(failed_count))
                if failed_count >= self.bstack11ll111111l_opy_:
                    self.logger.info(bstack1ll1ll1_opy_ (u"ࠣࡖ࡫ࡶࡪࡹࡨࡰ࡮ࡧࠤࡨࡸ࡯ࡴࡵࡨࡨ࠿ࠦࡻࡾࠢࡁࡁࠥࢁࡽࠣᝍ").format(failed_count, self.bstack11ll111111l_opy_))
                    self.bstack11l1llll1l1_opy_(failed_count)
                    self.bstack11ll1111l11_opy_ = True
            else:
                self.logger.error(bstack1ll1ll1_opy_ (u"ࠤࡉࡥ࡮ࡲࡥࡥࠢࡷࡳࠥࡶ࡯࡭࡮ࠣࡪࡦ࡯࡬ࡦࡦࠣࡸࡪࡹࡴࡴ࠼ࠣࡿࢂࠨᝎ").format(response))
        except Exception as e:
            self.logger.error(bstack1ll1ll1_opy_ (u"ࠥࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡤࡶࡴ࡬ࡲ࡬ࠦࡰࡰ࡮࡯࡭ࡳ࡭࠺ࠡࡽࢀࠦᝏ").format(e))
    def bstack11l1llll1l1_opy_(self, failed_count):
        with open(self.bstack11ll111l11l_opy_, bstack1ll1ll1_opy_ (u"ࠦࡼࠨᝐ")) as f:
            f.write(bstack1ll1ll1_opy_ (u"࡚ࠧࡨࡳࡧࡶ࡬ࡴࡲࡤࠡࡥࡵࡳࡸࡹࡥࡥࠢࡤࡸࠥࢁࡽ࡝ࡰࠥᝑ").format(datetime.now()))
            f.write(bstack1ll1ll1_opy_ (u"ࠨࡆࡢ࡫࡯ࡩࡩࠦࡴࡦࡵࡷࡷࠥࡩ࡯ࡶࡰࡷ࠾ࠥࢁࡽ࡝ࡰࠥᝒ").format(failed_count))
        self.logger.debug(bstack1ll1ll1_opy_ (u"ࠢࡂࡤࡲࡶࡹࠦࡂࡶ࡫࡯ࡨࠥ࡬ࡩ࡭ࡧࠣࡧࡷ࡫ࡡࡵࡧࡧ࠾ࠥࢁࡽࠣᝓ").format(self.bstack11ll111l11l_opy_))
    def bstack11ll11111ll_opy_(self):
        def bstack11ll111l1ll_opy_():
            while not self.bstack11ll1111l11_opy_:
                time.sleep(bstack11ll1111111_opy_)
                self.bstack11ll111l1l1_opy_()
                self.bstack11ll11lll11_opy_()
        bstack11ll11111l1_opy_ = threading.Thread(target=bstack11ll111l1ll_opy_, daemon=True)
        bstack11ll11111l1_opy_.start()