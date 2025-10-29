# coding: UTF-8
import sys
bstack1l1l111_opy_ = sys.version_info [0] == 2
bstack11l1ll_opy_ = 2048
bstack1llll11_opy_ = 7
def bstack11ll1l_opy_ (bstack1llllll1_opy_):
    global bstack1ll11_opy_
    bstack11ll111_opy_ = ord (bstack1llllll1_opy_ [-1])
    bstack1lll111_opy_ = bstack1llllll1_opy_ [:-1]
    bstack11l11l_opy_ = bstack11ll111_opy_ % len (bstack1lll111_opy_)
    bstack1l1ll11_opy_ = bstack1lll111_opy_ [:bstack11l11l_opy_] + bstack1lll111_opy_ [bstack11l11l_opy_:]
    if bstack1l1l111_opy_:
        bstack11111l1_opy_ = unicode () .join ([unichr (ord (char) - bstack11l1ll_opy_ - (bstack1l11111_opy_ + bstack11ll111_opy_) % bstack1llll11_opy_) for bstack1l11111_opy_, char in enumerate (bstack1l1ll11_opy_)])
    else:
        bstack11111l1_opy_ = str () .join ([chr (ord (char) - bstack11l1ll_opy_ - (bstack1l11111_opy_ + bstack11ll111_opy_) % bstack1llll11_opy_) for bstack1l11111_opy_, char in enumerate (bstack1l1ll11_opy_)])
    return eval (bstack11111l1_opy_)
import threading
import tempfile
import os
import time
from datetime import datetime
from bstack_utils.bstack11ll1l1lll1_opy_ import bstack11ll1l1ll11_opy_
from bstack_utils.constants import bstack11ll1ll1111_opy_, bstack1l1l11l11_opy_
from bstack_utils.bstack111l1111_opy_ import bstack1llllll11_opy_
from bstack_utils import bstack1l11111111_opy_
bstack11l1lll1l11_opy_ = 10
class bstack11l11111ll_opy_:
    def __init__(self, bstack1ll1l1ll1_opy_, config, bstack11l1lllll1l_opy_=0):
        self.bstack11l1ll1l1l1_opy_ = set()
        self.lock = threading.Lock()
        self.bstack11l1ll1lll1_opy_ = bstack11ll1l_opy_ (u"ࠨࡻࡾ࠱ࡷࡩࡸࡺ࡯ࡳࡥ࡫ࡩࡸࡺࡲࡢࡶ࡬ࡳࡳ࠵ࡡࡱ࡫࠲ࡺ࠶࠵ࡦࡢ࡫࡯ࡩࡩ࠳ࡴࡦࡵࡷࡷࠧ᝙").format(bstack11ll1ll1111_opy_)
        self.bstack11l1ll1ll11_opy_ = os.path.join(tempfile.gettempdir(), bstack11ll1l_opy_ (u"ࠢࡢࡤࡲࡶࡹࡥࡢࡶ࡫࡯ࡨࡤࢁࡽࠣ᝚").format(os.environ.get(bstack11ll1l_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡍ࡛ࡂࡠࡗࡘࡍࡉ࠭᝛"))))
        self.bstack11l1lll11ll_opy_ = os.path.join(tempfile.gettempdir(), bstack11ll1l_opy_ (u"ࠤࡩࡥ࡮ࡲࡥࡥࡡࡷࡩࡸࡺࡳࡠࡽࢀ࠲ࡹࡾࡴࠣ᝜").format(os.environ.get(bstack11ll1l_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚ࡈࡖࡄࡢ࡙࡚ࡏࡄࠨ᝝"))))
        self.bstack11l1lll1111_opy_ = 2
        self.bstack1ll1l1ll1_opy_ = bstack1ll1l1ll1_opy_
        self.config = config
        self.logger = bstack1l11111111_opy_.get_logger(__name__, bstack1l1l11l11_opy_)
        self.bstack11l1lllll1l_opy_ = bstack11l1lllll1l_opy_
        self.bstack11l1lll111l_opy_ = False
        self.bstack11l1lll11l1_opy_ = not (
                            os.environ.get(bstack11ll1l_opy_ (u"ࠦࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡆ࡚ࡏࡌࡅࡡࡕ࡙ࡓࡥࡉࡅࡇࡑࡘࡎࡌࡉࡆࡔࠥ᝞")) and
                            os.environ.get(bstack11ll1l_opy_ (u"ࠧࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡓࡕࡄࡆࡡࡌࡒࡉࡋࡘࠣ᝟")) and
                            os.environ.get(bstack11ll1l_opy_ (u"ࠨࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡏࡕࡃࡏࡣࡓࡕࡄࡆࡡࡆࡓ࡚ࡔࡔࠣᝠ"))
                        )
        if bstack1llllll11_opy_.bstack11l1llll1l1_opy_(config):
            self.bstack11l1lll1111_opy_ = bstack1llllll11_opy_.bstack11l1llll1ll_opy_(config, self.bstack11l1lllll1l_opy_)
            self.bstack11l1ll1ll1l_opy_()
    def bstack11l1llll111_opy_(self):
        return bstack11ll1l_opy_ (u"ࠢࡼࡿࡢࡿࢂࠨᝡ").format(self.config.get(bstack11ll1l_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡎࡢ࡯ࡨࠫᝢ")), os.environ.get(bstack11ll1l_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡄࡘࡍࡑࡊ࡟ࡓࡗࡑࡣࡎࡊࡅࡏࡖࡌࡊࡎࡋࡒࠨᝣ")))
    def bstack11l1llll11l_opy_(self):
        try:
            if self.bstack11l1lll11l1_opy_:
                return
            with self.lock:
                try:
                    with open(self.bstack11l1lll11ll_opy_, bstack11ll1l_opy_ (u"ࠥࡶࠧᝤ")) as f:
                        bstack11l1lll1ll1_opy_ = set(line.strip() for line in f if line.strip())
                except FileNotFoundError:
                    bstack11l1lll1ll1_opy_ = set()
                bstack11l1lll1l1l_opy_ = bstack11l1lll1ll1_opy_ - self.bstack11l1ll1l1l1_opy_
                if not bstack11l1lll1l1l_opy_:
                    return
                self.bstack11l1ll1l1l1_opy_.update(bstack11l1lll1l1l_opy_)
                data = {bstack11ll1l_opy_ (u"ࠦ࡫ࡧࡩ࡭ࡧࡧࡘࡪࡹࡴࡴࠤᝥ"): list(self.bstack11l1ll1l1l1_opy_), bstack11ll1l_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡒࡦࡳࡥࠣᝦ"): self.config.get(bstack11ll1l_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡓࡧ࡭ࡦࠩᝧ")), bstack11ll1l_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡘࡵ࡯ࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠧᝨ"): os.environ.get(bstack11ll1l_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡃࡗࡌࡐࡉࡥࡒࡖࡐࡢࡍࡉࡋࡎࡕࡋࡉࡍࡊࡘࠧᝩ")), bstack11ll1l_opy_ (u"ࠤࡳࡶࡴࡰࡥࡤࡶࡑࡥࡲ࡫ࠢᝪ"): self.config.get(bstack11ll1l_opy_ (u"ࠪࡴࡷࡵࡪࡦࡥࡷࡒࡦࡳࡥࠨᝫ"))}
            response = bstack11ll1l1ll11_opy_.bstack11ll1111ll1_opy_(self.bstack11l1ll1lll1_opy_, data)
            if response.get(bstack11ll1l_opy_ (u"ࠦࡸࡺࡡࡵࡷࡶࠦᝬ")) == 200:
                self.logger.debug(bstack11ll1l_opy_ (u"࡙ࠧࡵࡤࡥࡨࡷࡸ࡬ࡵ࡭࡮ࡼࠤࡸ࡫࡮ࡵࠢࡩࡥ࡮ࡲࡥࡥࠢࡷࡩࡸࡺࡳ࠻ࠢࡾࢁࠧ᝭").format(data))
            else:
                self.logger.debug(bstack11ll1l_opy_ (u"ࠨࡆࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡶࡩࡳࡪࠠࡧࡣ࡬ࡰࡪࡪࠠࡵࡧࡶࡸࡸࡀࠠࡼࡿࠥᝮ").format(response))
        except Exception as e:
            self.logger.debug(bstack11ll1l_opy_ (u"ࠢࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣࡨࡺࡸࡩ࡯ࡩࠣࡷࡪࡴࡤࡪࡰࡪࠤ࡫ࡧࡩ࡭ࡧࡧࠤࡹ࡫ࡳࡵࡵ࠽ࠤࢀࢃࠢᝯ").format(e))
    def bstack11ll111llll_opy_(self):
        if self.bstack11l1lll11l1_opy_:
            with self.lock:
                try:
                    with open(self.bstack11l1lll11ll_opy_, bstack11ll1l_opy_ (u"ࠣࡴࠥᝰ")) as f:
                        bstack11l1ll1l1ll_opy_ = set(line.strip() for line in f if line.strip())
                    failed_count = len(bstack11l1ll1l1ll_opy_)
                except FileNotFoundError:
                    failed_count = 0
                self.logger.debug(bstack11ll1l_opy_ (u"ࠤࡓࡳࡱࡲࡥࡥࠢࡩࡥ࡮ࡲࡥࡥࠢࡷࡩࡸࡺࡳࠡࡥࡲࡹࡳࡺࠠࠩ࡮ࡲࡧࡦࡲࠩ࠻ࠢࡾࢁࠧ᝱").format(failed_count))
                if failed_count >= self.bstack11l1lll1111_opy_:
                    self.logger.info(bstack11ll1l_opy_ (u"ࠥࡘ࡭ࡸࡥࡴࡪࡲࡰࡩࠦࡣࡳࡱࡶࡷࡪࡪࠠࠩ࡮ࡲࡧࡦࡲࠩ࠻ࠢࡾࢁࠥࡄ࠽ࠡࡽࢀࠦᝲ").format(failed_count, self.bstack11l1lll1111_opy_))
                    self.bstack11l1ll1llll_opy_(failed_count)
                    self.bstack11l1lll111l_opy_ = True
            return
        try:
            response = bstack11ll1l1ll11_opy_.bstack11ll111llll_opy_(bstack11ll1l_opy_ (u"ࠦࢀࢃ࠿ࡣࡷ࡬ࡰࡩࡔࡡ࡮ࡧࡀࡿࢂࠬࡢࡶ࡫࡯ࡨࡗࡻ࡮ࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࡁࢀࢃࠦࡱࡴࡲ࡮ࡪࡩࡴࡏࡣࡰࡩࡂࢁࡽࠣᝳ").format(self.bstack11l1ll1lll1_opy_, self.config.get(bstack11ll1l_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡒࡦࡳࡥࠨ᝴")), os.environ.get(bstack11ll1l_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡈࡕࡊࡎࡇࡣࡗ࡛ࡎࡠࡋࡇࡉࡓ࡚ࡉࡇࡋࡈࡖࠬ᝵")), self.config.get(bstack11ll1l_opy_ (u"ࠧࡱࡴࡲ࡮ࡪࡩࡴࡏࡣࡰࡩࠬ᝶"))))
            if response.get(bstack11ll1l_opy_ (u"ࠣࡵࡷࡥࡹࡻࡳࠣ᝷")) == 200:
                failed_count = response.get(bstack11ll1l_opy_ (u"ࠤࡩࡥ࡮ࡲࡥࡥࡖࡨࡷࡹࡹࡃࡰࡷࡱࡸࠧ᝸"), 0)
                self.logger.debug(bstack11ll1l_opy_ (u"ࠥࡔࡴࡲ࡬ࡦࡦࠣࡪࡦ࡯࡬ࡦࡦࠣࡸࡪࡹࡴࡴࠢࡦࡳࡺࡴࡴ࠻ࠢࡾࢁࠧ᝹").format(failed_count))
                if failed_count >= self.bstack11l1lll1111_opy_:
                    self.logger.info(bstack11ll1l_opy_ (u"࡙ࠦ࡮ࡲࡦࡵ࡫ࡳࡱࡪࠠࡤࡴࡲࡷࡸ࡫ࡤ࠻ࠢࡾࢁࠥࡄ࠽ࠡࡽࢀࠦ᝺").format(failed_count, self.bstack11l1lll1111_opy_))
                    self.bstack11l1ll1llll_opy_(failed_count)
                    self.bstack11l1lll111l_opy_ = True
            else:
                self.logger.error(bstack11ll1l_opy_ (u"ࠧࡌࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡࡲࡲࡰࡱࠦࡦࡢ࡫࡯ࡩࡩࠦࡴࡦࡵࡷࡷ࠿ࠦࡻࡾࠤ᝻").format(response))
        except Exception as e:
            self.logger.error(bstack11ll1l_opy_ (u"ࠨࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢࡧࡹࡷ࡯࡮ࡨࠢࡳࡳࡱࡲࡩ࡯ࡩ࠽ࠤࢀࢃࠢ᝼").format(e))
    def bstack11l1ll1llll_opy_(self, failed_count):
        with open(self.bstack11l1ll1ll11_opy_, bstack11ll1l_opy_ (u"ࠢࡸࠤ᝽")) as f:
            f.write(bstack11ll1l_opy_ (u"ࠣࡖ࡫ࡶࡪࡹࡨࡰ࡮ࡧࠤࡨࡸ࡯ࡴࡵࡨࡨࠥࡧࡴࠡࡽࢀࡠࡳࠨ᝾").format(datetime.now()))
            f.write(bstack11ll1l_opy_ (u"ࠤࡉࡥ࡮ࡲࡥࡥࠢࡷࡩࡸࡺࡳࠡࡥࡲࡹࡳࡺ࠺ࠡࡽࢀࡠࡳࠨ᝿").format(failed_count))
        self.logger.debug(bstack11ll1l_opy_ (u"ࠥࡅࡧࡵࡲࡵࠢࡅࡹ࡮ࡲࡤࠡࡨ࡬ࡰࡪࠦࡣࡳࡧࡤࡸࡪࡪ࠺ࠡࡽࢀࠦក").format(self.bstack11l1ll1ll11_opy_))
    def bstack11l1ll1ll1l_opy_(self):
        def bstack11l1lllll11_opy_():
            while not self.bstack11l1lll111l_opy_:
                time.sleep(bstack11l1lll1l11_opy_)
                self.bstack11l1llll11l_opy_()
                self.bstack11ll111llll_opy_()
        bstack11l1lll1lll_opy_ = threading.Thread(target=bstack11l1lllll11_opy_, daemon=True)
        bstack11l1lll1lll_opy_.start()