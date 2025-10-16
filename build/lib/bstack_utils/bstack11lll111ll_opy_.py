# coding: UTF-8
import sys
bstack11l1_opy_ = sys.version_info [0] == 2
bstack1l1l1ll_opy_ = 2048
bstack1llllll1_opy_ = 7
def bstack1l_opy_ (bstack11l1lll_opy_):
    global bstack1ll1ll1_opy_
    bstack1ll1l_opy_ = ord (bstack11l1lll_opy_ [-1])
    bstack1lll11_opy_ = bstack11l1lll_opy_ [:-1]
    bstack111l111_opy_ = bstack1ll1l_opy_ % len (bstack1lll11_opy_)
    bstack1ll11l_opy_ = bstack1lll11_opy_ [:bstack111l111_opy_] + bstack1lll11_opy_ [bstack111l111_opy_:]
    if bstack11l1_opy_:
        bstack1l1ll1l_opy_ = unicode () .join ([unichr (ord (char) - bstack1l1l1ll_opy_ - (bstack111l11_opy_ + bstack1ll1l_opy_) % bstack1llllll1_opy_) for bstack111l11_opy_, char in enumerate (bstack1ll11l_opy_)])
    else:
        bstack1l1ll1l_opy_ = str () .join ([chr (ord (char) - bstack1l1l1ll_opy_ - (bstack111l11_opy_ + bstack1ll1l_opy_) % bstack1llllll1_opy_) for bstack111l11_opy_, char in enumerate (bstack1ll11l_opy_)])
    return eval (bstack1l1ll1l_opy_)
import threading
import tempfile
import os
import time
from datetime import datetime
from bstack_utils.bstack11lll111l1l_opy_ import bstack11ll1lll111_opy_
from bstack_utils.constants import bstack11lll1111ll_opy_, bstack1lll1lll11_opy_
from bstack_utils.bstack1111l11l_opy_ import bstack11111l1l_opy_
from bstack_utils import bstack111ll1l1l_opy_
bstack11l1llll1l1_opy_ = 10
class bstack11111llll1_opy_:
    def __init__(self, bstack1111lll11l_opy_, config, bstack11ll111ll11_opy_=0):
        self.bstack11ll111l1ll_opy_ = set()
        self.lock = threading.Lock()
        self.bstack11ll111l1l1_opy_ = bstack1l_opy_ (u"ࠥࡿࢂ࠵ࡴࡦࡵࡷࡳࡷࡩࡨࡦࡵࡷࡶࡦࡺࡩࡰࡰ࠲ࡥࡵ࡯࠯ࡷ࠳࠲ࡪࡦ࡯࡬ࡦࡦ࠰ࡸࡪࡹࡴࡴࠤᜬ").format(bstack11lll1111ll_opy_)
        self.bstack11ll1111ll1_opy_ = os.path.join(tempfile.gettempdir(), bstack1l_opy_ (u"ࠦࡦࡨ࡯ࡳࡶࡢࡦࡺ࡯࡬ࡥࡡࡾࢁࠧᜭ").format(os.environ.get(bstack1l_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡊࡘࡆࡤ࡛ࡕࡊࡆࠪᜮ"))))
        self.bstack11ll11111ll_opy_ = os.path.join(tempfile.gettempdir(), bstack1l_opy_ (u"ࠨࡦࡢ࡫࡯ࡩࡩࡥࡴࡦࡵࡷࡷࡤࢁࡽ࠯ࡶࡻࡸࠧᜯ").format(os.environ.get(bstack1l_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡖࡗࡌࡈࠬᜰ"))))
        self.bstack11ll1111l11_opy_ = 2
        self.bstack1111lll11l_opy_ = bstack1111lll11l_opy_
        self.config = config
        self.logger = bstack111ll1l1l_opy_.get_logger(__name__, bstack1lll1lll11_opy_)
        self.bstack11ll111ll11_opy_ = bstack11ll111ll11_opy_
        self.bstack11l1llllll1_opy_ = False
        self.bstack11ll111111l_opy_ = not (
                            os.environ.get(bstack1l_opy_ (u"ࠣࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡃࡗࡌࡐࡉࡥࡒࡖࡐࡢࡍࡉࡋࡎࡕࡋࡉࡍࡊࡘࠢᜱ")) and
                            os.environ.get(bstack1l_opy_ (u"ࠤࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡐࡒࡈࡊࡥࡉࡏࡆࡈ࡜ࠧᜲ")) and
                            os.environ.get(bstack1l_opy_ (u"ࠥࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡓ࡙ࡇࡌࡠࡐࡒࡈࡊࡥࡃࡐࡗࡑࡘࠧᜳ"))
                        )
        if bstack11111l1l_opy_.bstack11ll111l111_opy_(config):
            self.bstack11ll1111l11_opy_ = bstack11111l1l_opy_.bstack11ll1111lll_opy_(config, self.bstack11ll111ll11_opy_)
            self.bstack11l1lllll1l_opy_()
    def bstack11l1llll1ll_opy_(self):
        return bstack1l_opy_ (u"ࠦࢀࢃ࡟ࡼࡿ᜴ࠥ").format(self.config.get(bstack1l_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡒࡦࡳࡥࠨ᜵")), os.environ.get(bstack1l_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡈࡕࡊࡎࡇࡣࡗ࡛ࡎࡠࡋࡇࡉࡓ࡚ࡉࡇࡋࡈࡖࠬ᜶")))
    def bstack11ll1111l1l_opy_(self):
        try:
            if self.bstack11ll111111l_opy_:
                return
            with self.lock:
                try:
                    with open(self.bstack11ll11111ll_opy_, bstack1l_opy_ (u"ࠢࡳࠤ᜷")) as f:
                        bstack11l1lllllll_opy_ = set(line.strip() for line in f if line.strip())
                except FileNotFoundError:
                    bstack11l1lllllll_opy_ = set()
                bstack11l1lllll11_opy_ = bstack11l1lllllll_opy_ - self.bstack11ll111l1ll_opy_
                if not bstack11l1lllll11_opy_:
                    return
                self.bstack11ll111l1ll_opy_.update(bstack11l1lllll11_opy_)
                data = {bstack1l_opy_ (u"ࠣࡨࡤ࡭ࡱ࡫ࡤࡕࡧࡶࡸࡸࠨ᜸"): list(self.bstack11ll111l1ll_opy_), bstack1l_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡏࡣࡰࡩࠧ᜹"): self.config.get(bstack1l_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡐࡤࡱࡪ࠭᜺")), bstack1l_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡕࡹࡳࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠤ᜻"): os.environ.get(bstack1l_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡇ࡛ࡉࡍࡆࡢࡖ࡚ࡔ࡟ࡊࡆࡈࡒ࡙ࡏࡆࡊࡇࡕࠫ᜼")), bstack1l_opy_ (u"ࠨࡰࡳࡱ࡭ࡩࡨࡺࡎࡢ࡯ࡨࠦ᜽"): self.config.get(bstack1l_opy_ (u"ࠧࡱࡴࡲ࡮ࡪࡩࡴࡏࡣࡰࡩࠬ᜾"))}
            response = bstack11ll1lll111_opy_.bstack11ll11lllll_opy_(self.bstack11ll111l1l1_opy_, data)
            if response.get(bstack1l_opy_ (u"ࠣࡵࡷࡥࡹࡻࡳࠣ᜿")) == 200:
                self.logger.debug(bstack1l_opy_ (u"ࠤࡖࡹࡨࡩࡥࡴࡵࡩࡹࡱࡲࡹࠡࡵࡨࡲࡹࠦࡦࡢ࡫࡯ࡩࡩࠦࡴࡦࡵࡷࡷ࠿ࠦࡻࡾࠤᝀ").format(data))
            else:
                self.logger.debug(bstack1l_opy_ (u"ࠥࡊࡦ࡯࡬ࡦࡦࠣࡸࡴࠦࡳࡦࡰࡧࠤ࡫ࡧࡩ࡭ࡧࡧࠤࡹ࡫ࡳࡵࡵ࠽ࠤࢀࢃࠢᝁ").format(response))
        except Exception as e:
            self.logger.debug(bstack1l_opy_ (u"ࠦࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡥࡷࡵ࡭ࡳ࡭ࠠࡴࡧࡱࡨ࡮ࡴࡧࠡࡨࡤ࡭ࡱ࡫ࡤࠡࡶࡨࡷࡹࡹ࠺ࠡࡽࢀࠦᝂ").format(e))
    def bstack11ll11l1l1l_opy_(self):
        if self.bstack11ll111111l_opy_:
            with self.lock:
                try:
                    with open(self.bstack11ll11111ll_opy_, bstack1l_opy_ (u"ࠧࡸࠢᝃ")) as f:
                        bstack11ll11111l1_opy_ = set(line.strip() for line in f if line.strip())
                    failed_count = len(bstack11ll11111l1_opy_)
                except FileNotFoundError:
                    failed_count = 0
                self.logger.debug(bstack1l_opy_ (u"ࠨࡐࡰ࡮࡯ࡩࡩࠦࡦࡢ࡫࡯ࡩࡩࠦࡴࡦࡵࡷࡷࠥࡩ࡯ࡶࡰࡷࠤ࠭ࡲ࡯ࡤࡣ࡯࠭࠿ࠦࡻࡾࠤᝄ").format(failed_count))
                if failed_count >= self.bstack11ll1111l11_opy_:
                    self.logger.info(bstack1l_opy_ (u"ࠢࡕࡪࡵࡩࡸ࡮࡯࡭ࡦࠣࡧࡷࡵࡳࡴࡧࡧࠤ࠭ࡲ࡯ࡤࡣ࡯࠭࠿ࠦࡻࡾࠢࡁࡁࠥࢁࡽࠣᝅ").format(failed_count, self.bstack11ll1111l11_opy_))
                    self.bstack11l1llll11l_opy_(failed_count)
                    self.bstack11l1llllll1_opy_ = True
            return
        try:
            response = bstack11ll1lll111_opy_.bstack11ll11l1l1l_opy_(bstack1l_opy_ (u"ࠣࡽࢀࡃࡧࡻࡩ࡭ࡦࡑࡥࡲ࡫࠽ࡼࡿࠩࡦࡺ࡯࡬ࡥࡔࡸࡲࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲ࠾ࡽࢀࠪࡵࡸ࡯࡫ࡧࡦࡸࡓࡧ࡭ࡦ࠿ࡾࢁࠧᝆ").format(self.bstack11ll111l1l1_opy_, self.config.get(bstack1l_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡏࡣࡰࡩࠬᝇ")), os.environ.get(bstack1l_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡅ࡙ࡎࡒࡄࡠࡔࡘࡒࡤࡏࡄࡆࡐࡗࡍࡋࡏࡅࡓࠩᝈ")), self.config.get(bstack1l_opy_ (u"ࠫࡵࡸ࡯࡫ࡧࡦࡸࡓࡧ࡭ࡦࠩᝉ"))))
            if response.get(bstack1l_opy_ (u"ࠧࡹࡴࡢࡶࡸࡷࠧᝊ")) == 200:
                failed_count = response.get(bstack1l_opy_ (u"ࠨࡦࡢ࡫࡯ࡩࡩ࡚ࡥࡴࡶࡶࡇࡴࡻ࡮ࡵࠤᝋ"), 0)
                self.logger.debug(bstack1l_opy_ (u"ࠢࡑࡱ࡯ࡰࡪࡪࠠࡧࡣ࡬ࡰࡪࡪࠠࡵࡧࡶࡸࡸࠦࡣࡰࡷࡱࡸ࠿ࠦࡻࡾࠤᝌ").format(failed_count))
                if failed_count >= self.bstack11ll1111l11_opy_:
                    self.logger.info(bstack1l_opy_ (u"ࠣࡖ࡫ࡶࡪࡹࡨࡰ࡮ࡧࠤࡨࡸ࡯ࡴࡵࡨࡨ࠿ࠦࡻࡾࠢࡁࡁࠥࢁࡽࠣᝍ").format(failed_count, self.bstack11ll1111l11_opy_))
                    self.bstack11l1llll11l_opy_(failed_count)
                    self.bstack11l1llllll1_opy_ = True
            else:
                self.logger.error(bstack1l_opy_ (u"ࠤࡉࡥ࡮ࡲࡥࡥࠢࡷࡳࠥࡶ࡯࡭࡮ࠣࡪࡦ࡯࡬ࡦࡦࠣࡸࡪࡹࡴࡴ࠼ࠣࡿࢂࠨᝎ").format(response))
        except Exception as e:
            self.logger.error(bstack1l_opy_ (u"ࠥࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡤࡶࡴ࡬ࡲ࡬ࠦࡰࡰ࡮࡯࡭ࡳ࡭࠺ࠡࡽࢀࠦᝏ").format(e))
    def bstack11l1llll11l_opy_(self, failed_count):
        with open(self.bstack11ll1111ll1_opy_, bstack1l_opy_ (u"ࠦࡼࠨᝐ")) as f:
            f.write(bstack1l_opy_ (u"࡚ࠧࡨࡳࡧࡶ࡬ࡴࡲࡤࠡࡥࡵࡳࡸࡹࡥࡥࠢࡤࡸࠥࢁࡽ࡝ࡰࠥᝑ").format(datetime.now()))
            f.write(bstack1l_opy_ (u"ࠨࡆࡢ࡫࡯ࡩࡩࠦࡴࡦࡵࡷࡷࠥࡩ࡯ࡶࡰࡷ࠾ࠥࢁࡽ࡝ࡰࠥᝒ").format(failed_count))
        self.logger.debug(bstack1l_opy_ (u"ࠢࡂࡤࡲࡶࡹࠦࡂࡶ࡫࡯ࡨࠥ࡬ࡩ࡭ࡧࠣࡧࡷ࡫ࡡࡵࡧࡧ࠾ࠥࢁࡽࠣᝓ").format(self.bstack11ll1111ll1_opy_))
    def bstack11l1lllll1l_opy_(self):
        def bstack11ll1111111_opy_():
            while not self.bstack11l1llllll1_opy_:
                time.sleep(bstack11l1llll1l1_opy_)
                self.bstack11ll1111l1l_opy_()
                self.bstack11ll11l1l1l_opy_()
        bstack11ll111l11l_opy_ = threading.Thread(target=bstack11ll1111111_opy_, daemon=True)
        bstack11ll111l11l_opy_.start()