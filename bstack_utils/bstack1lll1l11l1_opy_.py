# coding: UTF-8
import sys
bstack1ll1lll_opy_ = sys.version_info [0] == 2
bstack1l1ll_opy_ = 2048
bstack11l1l1_opy_ = 7
def bstack111l1l_opy_ (bstack1l_opy_):
    global bstack11111ll_opy_
    bstack1lll11l_opy_ = ord (bstack1l_opy_ [-1])
    bstack111ll1_opy_ = bstack1l_opy_ [:-1]
    bstack1ll11l_opy_ = bstack1lll11l_opy_ % len (bstack111ll1_opy_)
    bstack11l111_opy_ = bstack111ll1_opy_ [:bstack1ll11l_opy_] + bstack111ll1_opy_ [bstack1ll11l_opy_:]
    if bstack1ll1lll_opy_:
        bstack1l11l11_opy_ = unicode () .join ([unichr (ord (char) - bstack1l1ll_opy_ - (bstack11llll_opy_ + bstack1lll11l_opy_) % bstack11l1l1_opy_) for bstack11llll_opy_, char in enumerate (bstack11l111_opy_)])
    else:
        bstack1l11l11_opy_ = str () .join ([chr (ord (char) - bstack1l1ll_opy_ - (bstack11llll_opy_ + bstack1lll11l_opy_) % bstack11l1l1_opy_) for bstack11llll_opy_, char in enumerate (bstack11l111_opy_)])
    return eval (bstack1l11l11_opy_)
import threading
import tempfile
import os
import time
from datetime import datetime
from bstack_utils.bstack11ll1l1ll1l_opy_ import bstack11lll111111_opy_
from bstack_utils.constants import bstack11ll1l1l11l_opy_, bstack111l111ll1_opy_
from bstack_utils.bstack1lll1llll_opy_ import bstack1llll1lll_opy_
from bstack_utils import bstack1l11l1lll_opy_
bstack11l1ll1ll1l_opy_ = 10
class bstack11lll1lll1_opy_:
    def __init__(self, bstack1l1lll11l1_opy_, config, bstack11l1lll1l11_opy_=0):
        self.bstack11l1ll1lll1_opy_ = set()
        self.lock = threading.Lock()
        self.bstack11l1ll1llll_opy_ = bstack111l1l_opy_ (u"ࠤࡾࢁ࠴ࡺࡥࡴࡶࡲࡶࡨ࡮ࡥࡴࡶࡵࡥࡹ࡯࡯࡯࠱ࡤࡴ࡮࠵ࡶ࠲࠱ࡩࡥ࡮ࡲࡥࡥ࠯ࡷࡩࡸࡺࡳࠣᝇ").format(bstack11ll1l1l11l_opy_)
        self.bstack11l1llll111_opy_ = os.path.join(tempfile.gettempdir(), bstack111l1l_opy_ (u"ࠥࡥࡧࡵࡲࡵࡡࡥࡹ࡮ࡲࡤࡠࡽࢀࠦᝈ").format(os.environ.get(bstack111l1l_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡉࡗࡅࡣ࡚࡛ࡉࡅࠩᝉ"))))
        self.bstack11l1lllll11_opy_ = os.path.join(tempfile.gettempdir(), bstack111l1l_opy_ (u"ࠧ࡬ࡡࡪ࡮ࡨࡨࡤࡺࡥࡴࡶࡶࡣࢀࢃ࠮ࡵࡺࡷࠦᝊ").format(os.environ.get(bstack111l1l_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡕࡖࡋࡇࠫᝋ"))))
        self.bstack11l1lll111l_opy_ = 2
        self.bstack1l1lll11l1_opy_ = bstack1l1lll11l1_opy_
        self.config = config
        self.logger = bstack1l11l1lll_opy_.get_logger(__name__, bstack111l111ll1_opy_)
        self.bstack11l1lll1l11_opy_ = bstack11l1lll1l11_opy_
        self.bstack11l1lll1ll1_opy_ = False
        self.bstack11l1ll1ll11_opy_ = not (
                            os.environ.get(bstack111l1l_opy_ (u"ࠢࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡂࡖࡋࡏࡈࡤࡘࡕࡏࡡࡌࡈࡊࡔࡔࡊࡈࡌࡉࡗࠨᝌ")) and
                            os.environ.get(bstack111l1l_opy_ (u"ࠣࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡏࡑࡇࡉࡤࡏࡎࡅࡇ࡛ࠦᝍ")) and
                            os.environ.get(bstack111l1l_opy_ (u"ࠤࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡒࡘࡆࡒ࡟ࡏࡑࡇࡉࡤࡉࡏࡖࡐࡗࠦᝎ"))
                        )
        if bstack1llll1lll_opy_.bstack11l1llll1ll_opy_(config):
            self.bstack11l1lll111l_opy_ = bstack1llll1lll_opy_.bstack11l1llll11l_opy_(config, self.bstack11l1lll1l11_opy_)
            self.bstack11l1lll1111_opy_()
    def bstack11l1llllll1_opy_(self):
        return bstack111l1l_opy_ (u"ࠥࡿࢂࡥࡻࡾࠤᝏ").format(self.config.get(bstack111l1l_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡑࡥࡲ࡫ࠧᝐ")), os.environ.get(bstack111l1l_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡇ࡛ࡉࡍࡆࡢࡖ࡚ࡔ࡟ࡊࡆࡈࡒ࡙ࡏࡆࡊࡇࡕࠫᝑ")))
    def bstack11l1lllll1l_opy_(self):
        try:
            if self.bstack11l1ll1ll11_opy_:
                return
            with self.lock:
                try:
                    with open(self.bstack11l1lllll11_opy_, bstack111l1l_opy_ (u"ࠨࡲࠣᝒ")) as f:
                        bstack11l1lll11ll_opy_ = set(line.strip() for line in f if line.strip())
                except FileNotFoundError:
                    bstack11l1lll11ll_opy_ = set()
                bstack11l1lll1l1l_opy_ = bstack11l1lll11ll_opy_ - self.bstack11l1ll1lll1_opy_
                if not bstack11l1lll1l1l_opy_:
                    return
                self.bstack11l1ll1lll1_opy_.update(bstack11l1lll1l1l_opy_)
                data = {bstack111l1l_opy_ (u"ࠢࡧࡣ࡬ࡰࡪࡪࡔࡦࡵࡷࡷࠧᝓ"): list(self.bstack11l1ll1lll1_opy_), bstack111l1l_opy_ (u"ࠣࡤࡸ࡭ࡱࡪࡎࡢ࡯ࡨࠦ᝔"): self.config.get(bstack111l1l_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡏࡣࡰࡩࠬ᝕")), bstack111l1l_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡔࡸࡲࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠣ᝖"): os.environ.get(bstack111l1l_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡆ࡚ࡏࡌࡅࡡࡕ࡙ࡓࡥࡉࡅࡇࡑࡘࡎࡌࡉࡆࡔࠪ᝗")), bstack111l1l_opy_ (u"ࠧࡶࡲࡰ࡬ࡨࡧࡹࡔࡡ࡮ࡧࠥ᝘"): self.config.get(bstack111l1l_opy_ (u"࠭ࡰࡳࡱ࡭ࡩࡨࡺࡎࡢ࡯ࡨࠫ᝙"))}
            response = bstack11lll111111_opy_.bstack11ll1111lll_opy_(self.bstack11l1ll1llll_opy_, data)
            if response.get(bstack111l1l_opy_ (u"ࠢࡴࡶࡤࡸࡺࡹࠢ᝚")) == 200:
                self.logger.debug(bstack111l1l_opy_ (u"ࠣࡕࡸࡧࡨ࡫ࡳࡴࡨࡸࡰࡱࡿࠠࡴࡧࡱࡸࠥ࡬ࡡࡪ࡮ࡨࡨࠥࡺࡥࡴࡶࡶ࠾ࠥࢁࡽࠣ᝛").format(data))
            else:
                self.logger.debug(bstack111l1l_opy_ (u"ࠤࡉࡥ࡮ࡲࡥࡥࠢࡷࡳࠥࡹࡥ࡯ࡦࠣࡪࡦ࡯࡬ࡦࡦࠣࡸࡪࡹࡴࡴ࠼ࠣࡿࢂࠨ᝜").format(response))
        except Exception as e:
            self.logger.debug(bstack111l1l_opy_ (u"ࠥࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡤࡶࡴ࡬ࡲ࡬ࠦࡳࡦࡰࡧ࡭ࡳ࡭ࠠࡧࡣ࡬ࡰࡪࡪࠠࡵࡧࡶࡸࡸࡀࠠࡼࡿࠥ᝝").format(e))
    def bstack11ll111l11l_opy_(self):
        if self.bstack11l1ll1ll11_opy_:
            with self.lock:
                try:
                    with open(self.bstack11l1lllll11_opy_, bstack111l1l_opy_ (u"ࠦࡷࠨ᝞")) as f:
                        bstack11l1lll11l1_opy_ = set(line.strip() for line in f if line.strip())
                    failed_count = len(bstack11l1lll11l1_opy_)
                except FileNotFoundError:
                    failed_count = 0
                self.logger.debug(bstack111l1l_opy_ (u"ࠧࡖ࡯࡭࡮ࡨࡨࠥ࡬ࡡࡪ࡮ࡨࡨࠥࡺࡥࡴࡶࡶࠤࡨࡵࡵ࡯ࡶࠣࠬࡱࡵࡣࡢ࡮ࠬ࠾ࠥࢁࡽࠣ᝟").format(failed_count))
                if failed_count >= self.bstack11l1lll111l_opy_:
                    self.logger.info(bstack111l1l_opy_ (u"ࠨࡔࡩࡴࡨࡷ࡭ࡵ࡬ࡥࠢࡦࡶࡴࡹࡳࡦࡦࠣࠬࡱࡵࡣࡢ࡮ࠬ࠾ࠥࢁࡽࠡࡀࡀࠤࢀࢃࠢᝠ").format(failed_count, self.bstack11l1lll111l_opy_))
                    self.bstack11l1lll1lll_opy_(failed_count)
                    self.bstack11l1lll1ll1_opy_ = True
            return
        try:
            response = bstack11lll111111_opy_.bstack11ll111l11l_opy_(bstack111l1l_opy_ (u"ࠢࡼࡿࡂࡦࡺ࡯࡬ࡥࡐࡤࡱࡪࡃࡻࡾࠨࡥࡹ࡮ࡲࡤࡓࡷࡱࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸ࠽ࡼࡿࠩࡴࡷࡵࡪࡦࡥࡷࡒࡦࡳࡥ࠾ࡽࢀࠦᝡ").format(self.bstack11l1ll1llll_opy_, self.config.get(bstack111l1l_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡎࡢ࡯ࡨࠫᝢ")), os.environ.get(bstack111l1l_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡄࡘࡍࡑࡊ࡟ࡓࡗࡑࡣࡎࡊࡅࡏࡖࡌࡊࡎࡋࡒࠨᝣ")), self.config.get(bstack111l1l_opy_ (u"ࠪࡴࡷࡵࡪࡦࡥࡷࡒࡦࡳࡥࠨᝤ"))))
            if response.get(bstack111l1l_opy_ (u"ࠦࡸࡺࡡࡵࡷࡶࠦᝥ")) == 200:
                failed_count = response.get(bstack111l1l_opy_ (u"ࠧ࡬ࡡࡪ࡮ࡨࡨ࡙࡫ࡳࡵࡵࡆࡳࡺࡴࡴࠣᝦ"), 0)
                self.logger.debug(bstack111l1l_opy_ (u"ࠨࡐࡰ࡮࡯ࡩࡩࠦࡦࡢ࡫࡯ࡩࡩࠦࡴࡦࡵࡷࡷࠥࡩ࡯ࡶࡰࡷ࠾ࠥࢁࡽࠣᝧ").format(failed_count))
                if failed_count >= self.bstack11l1lll111l_opy_:
                    self.logger.info(bstack111l1l_opy_ (u"ࠢࡕࡪࡵࡩࡸ࡮࡯࡭ࡦࠣࡧࡷࡵࡳࡴࡧࡧ࠾ࠥࢁࡽࠡࡀࡀࠤࢀࢃࠢᝨ").format(failed_count, self.bstack11l1lll111l_opy_))
                    self.bstack11l1lll1lll_opy_(failed_count)
                    self.bstack11l1lll1ll1_opy_ = True
            else:
                self.logger.error(bstack111l1l_opy_ (u"ࠣࡈࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤࡵࡵ࡬࡭ࠢࡩࡥ࡮ࡲࡥࡥࠢࡷࡩࡸࡺࡳ࠻ࠢࡾࢁࠧᝩ").format(response))
        except Exception as e:
            self.logger.error(bstack111l1l_opy_ (u"ࠤࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥࡪࡵࡳ࡫ࡱ࡫ࠥࡶ࡯࡭࡮࡬ࡲ࡬ࡀࠠࡼࡿࠥᝪ").format(e))
    def bstack11l1lll1lll_opy_(self, failed_count):
        with open(self.bstack11l1llll111_opy_, bstack111l1l_opy_ (u"ࠥࡻࠧᝫ")) as f:
            f.write(bstack111l1l_opy_ (u"࡙ࠦ࡮ࡲࡦࡵ࡫ࡳࡱࡪࠠࡤࡴࡲࡷࡸ࡫ࡤࠡࡣࡷࠤࢀࢃ࡜࡯ࠤᝬ").format(datetime.now()))
            f.write(bstack111l1l_opy_ (u"ࠧࡌࡡࡪ࡮ࡨࡨࠥࡺࡥࡴࡶࡶࠤࡨࡵࡵ࡯ࡶ࠽ࠤࢀࢃ࡜࡯ࠤ᝭").format(failed_count))
        self.logger.debug(bstack111l1l_opy_ (u"ࠨࡁࡣࡱࡵࡸࠥࡈࡵࡪ࡮ࡧࠤ࡫࡯࡬ࡦࠢࡦࡶࡪࡧࡴࡦࡦ࠽ࠤࢀࢃࠢᝮ").format(self.bstack11l1llll111_opy_))
    def bstack11l1lll1111_opy_(self):
        def bstack11l1llll1l1_opy_():
            while not self.bstack11l1lll1ll1_opy_:
                time.sleep(bstack11l1ll1ll1l_opy_)
                self.bstack11l1lllll1l_opy_()
                self.bstack11ll111l11l_opy_()
        bstack11l1lllllll_opy_ = threading.Thread(target=bstack11l1llll1l1_opy_, daemon=True)
        bstack11l1lllllll_opy_.start()