# coding: UTF-8
import sys
bstack1llll11_opy_ = sys.version_info [0] == 2
bstack1l1l11_opy_ = 2048
bstack11111ll_opy_ = 7
def bstack11ll_opy_ (bstack1111l1l_opy_):
    global bstack1lll_opy_
    bstack1ll11_opy_ = ord (bstack1111l1l_opy_ [-1])
    bstack1111l1_opy_ = bstack1111l1l_opy_ [:-1]
    bstack111l1_opy_ = bstack1ll11_opy_ % len (bstack1111l1_opy_)
    bstack11l11ll_opy_ = bstack1111l1_opy_ [:bstack111l1_opy_] + bstack1111l1_opy_ [bstack111l1_opy_:]
    if bstack1llll11_opy_:
        bstack11l1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack1l1l11_opy_ - (bstack11l1l11_opy_ + bstack1ll11_opy_) % bstack11111ll_opy_) for bstack11l1l11_opy_, char in enumerate (bstack11l11ll_opy_)])
    else:
        bstack11l1ll_opy_ = str () .join ([chr (ord (char) - bstack1l1l11_opy_ - (bstack11l1l11_opy_ + bstack1ll11_opy_) % bstack11111ll_opy_) for bstack11l1l11_opy_, char in enumerate (bstack11l11ll_opy_)])
    return eval (bstack11l1ll_opy_)
import threading
import tempfile
import os
import time
from datetime import datetime
from bstack_utils.bstack11ll1ll11ll_opy_ import bstack11ll1l1l111_opy_
from bstack_utils.constants import bstack11ll1lll11l_opy_, bstack111l1ll111_opy_
from bstack_utils.bstack11111lll_opy_ import bstack111ll1ll_opy_
from bstack_utils import bstack11l1l1l1ll_opy_
bstack11l1llll1ll_opy_ = 10
class bstack11l11l11ll_opy_:
    def __init__(self, bstack1l11ll1l1l_opy_, config, bstack11l1lll1111_opy_=0):
        self.bstack11l1ll1lll1_opy_ = set()
        self.lock = threading.Lock()
        self.bstack11l1ll1llll_opy_ = bstack11ll_opy_ (u"ࠤࡾࢁ࠴ࡺࡥࡴࡶࡲࡶࡨ࡮ࡥࡴࡶࡵࡥࡹ࡯࡯࡯࠱ࡤࡴ࡮࠵ࡶ࠲࠱ࡩࡥ࡮ࡲࡥࡥ࠯ࡷࡩࡸࡺࡳࠣᝎ").format(bstack11ll1lll11l_opy_)
        self.bstack11l1lll1ll1_opy_ = os.path.join(tempfile.gettempdir(), bstack11ll_opy_ (u"ࠥࡥࡧࡵࡲࡵࡡࡥࡹ࡮ࡲࡤࡠࡽࢀࠦᝏ").format(os.environ.get(bstack11ll_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡉࡗࡅࡣ࡚࡛ࡉࡅࠩᝐ"))))
        self.bstack11l1ll1ll1l_opy_ = os.path.join(tempfile.gettempdir(), bstack11ll_opy_ (u"ࠧ࡬ࡡࡪ࡮ࡨࡨࡤࡺࡥࡴࡶࡶࡣࢀࢃ࠮ࡵࡺࡷࠦᝑ").format(os.environ.get(bstack11ll_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡕࡖࡋࡇࠫᝒ"))))
        self.bstack11l1llllll1_opy_ = 2
        self.bstack1l11ll1l1l_opy_ = bstack1l11ll1l1l_opy_
        self.config = config
        self.logger = bstack11l1l1l1ll_opy_.get_logger(__name__, bstack111l1ll111_opy_)
        self.bstack11l1lll1111_opy_ = bstack11l1lll1111_opy_
        self.bstack11l1lll1l1l_opy_ = False
        self.bstack11l1lll11l1_opy_ = not (
                            os.environ.get(bstack11ll_opy_ (u"ࠢࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡂࡖࡋࡏࡈࡤࡘࡕࡏࡡࡌࡈࡊࡔࡔࡊࡈࡌࡉࡗࠨᝓ")) and
                            os.environ.get(bstack11ll_opy_ (u"ࠣࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡏࡑࡇࡉࡤࡏࡎࡅࡇ࡛ࠦ᝔")) and
                            os.environ.get(bstack11ll_opy_ (u"ࠤࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡒࡘࡆࡒ࡟ࡏࡑࡇࡉࡤࡉࡏࡖࡐࡗࠦ᝕"))
                        )
        if bstack111ll1ll_opy_.bstack11ll1111111_opy_(config):
            self.bstack11l1llllll1_opy_ = bstack111ll1ll_opy_.bstack11l1lll1lll_opy_(config, self.bstack11l1lll1111_opy_)
            self.bstack11l1llll11l_opy_()
    def bstack11l1lllllll_opy_(self):
        return bstack11ll_opy_ (u"ࠥࡿࢂࡥࡻࡾࠤ᝖").format(self.config.get(bstack11ll_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡑࡥࡲ࡫ࠧ᝗")), os.environ.get(bstack11ll_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡇ࡛ࡉࡍࡆࡢࡖ࡚ࡔ࡟ࡊࡆࡈࡒ࡙ࡏࡆࡊࡇࡕࠫ᝘")))
    def bstack11l1lll11ll_opy_(self):
        try:
            if self.bstack11l1lll11l1_opy_:
                return
            with self.lock:
                try:
                    with open(self.bstack11l1ll1ll1l_opy_, bstack11ll_opy_ (u"ࠨࡲࠣ᝙")) as f:
                        bstack11l1llll111_opy_ = set(line.strip() for line in f if line.strip())
                except FileNotFoundError:
                    bstack11l1llll111_opy_ = set()
                bstack11l1lll1l11_opy_ = bstack11l1llll111_opy_ - self.bstack11l1ll1lll1_opy_
                if not bstack11l1lll1l11_opy_:
                    return
                self.bstack11l1ll1lll1_opy_.update(bstack11l1lll1l11_opy_)
                data = {bstack11ll_opy_ (u"ࠢࡧࡣ࡬ࡰࡪࡪࡔࡦࡵࡷࡷࠧ᝚"): list(self.bstack11l1ll1lll1_opy_), bstack11ll_opy_ (u"ࠣࡤࡸ࡭ࡱࡪࡎࡢ࡯ࡨࠦ᝛"): self.config.get(bstack11ll_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡏࡣࡰࡩࠬ᝜")), bstack11ll_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡔࡸࡲࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠣ᝝"): os.environ.get(bstack11ll_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡆ࡚ࡏࡌࡅࡡࡕ࡙ࡓࡥࡉࡅࡇࡑࡘࡎࡌࡉࡆࡔࠪ᝞")), bstack11ll_opy_ (u"ࠧࡶࡲࡰ࡬ࡨࡧࡹࡔࡡ࡮ࡧࠥ᝟"): self.config.get(bstack11ll_opy_ (u"࠭ࡰࡳࡱ࡭ࡩࡨࡺࡎࡢ࡯ࡨࠫᝠ"))}
            response = bstack11ll1l1l111_opy_.bstack11ll11l11l1_opy_(self.bstack11l1ll1llll_opy_, data)
            if response.get(bstack11ll_opy_ (u"ࠢࡴࡶࡤࡸࡺࡹࠢᝡ")) == 200:
                self.logger.debug(bstack11ll_opy_ (u"ࠣࡕࡸࡧࡨ࡫ࡳࡴࡨࡸࡰࡱࡿࠠࡴࡧࡱࡸࠥ࡬ࡡࡪ࡮ࡨࡨࠥࡺࡥࡴࡶࡶ࠾ࠥࢁࡽࠣᝢ").format(data))
            else:
                self.logger.debug(bstack11ll_opy_ (u"ࠤࡉࡥ࡮ࡲࡥࡥࠢࡷࡳࠥࡹࡥ࡯ࡦࠣࡪࡦ࡯࡬ࡦࡦࠣࡸࡪࡹࡴࡴ࠼ࠣࡿࢂࠨᝣ").format(response))
        except Exception as e:
            self.logger.debug(bstack11ll_opy_ (u"ࠥࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡤࡶࡴ࡬ࡲ࡬ࠦࡳࡦࡰࡧ࡭ࡳ࡭ࠠࡧࡣ࡬ࡰࡪࡪࠠࡵࡧࡶࡸࡸࡀࠠࡼࡿࠥᝤ").format(e))
    def bstack11ll111l1ll_opy_(self):
        if self.bstack11l1lll11l1_opy_:
            with self.lock:
                try:
                    with open(self.bstack11l1ll1ll1l_opy_, bstack11ll_opy_ (u"ࠦࡷࠨᝥ")) as f:
                        bstack11l1lllll11_opy_ = set(line.strip() for line in f if line.strip())
                    failed_count = len(bstack11l1lllll11_opy_)
                except FileNotFoundError:
                    failed_count = 0
                self.logger.debug(bstack11ll_opy_ (u"ࠧࡖ࡯࡭࡮ࡨࡨࠥ࡬ࡡࡪ࡮ࡨࡨࠥࡺࡥࡴࡶࡶࠤࡨࡵࡵ࡯ࡶࠣࠬࡱࡵࡣࡢ࡮ࠬ࠾ࠥࢁࡽࠣᝦ").format(failed_count))
                if failed_count >= self.bstack11l1llllll1_opy_:
                    self.logger.info(bstack11ll_opy_ (u"ࠨࡔࡩࡴࡨࡷ࡭ࡵ࡬ࡥࠢࡦࡶࡴࡹࡳࡦࡦࠣࠬࡱࡵࡣࡢ࡮ࠬ࠾ࠥࢁࡽࠡࡀࡀࠤࢀࢃࠢᝧ").format(failed_count, self.bstack11l1llllll1_opy_))
                    self.bstack11l1lll111l_opy_(failed_count)
                    self.bstack11l1lll1l1l_opy_ = True
            return
        try:
            response = bstack11ll1l1l111_opy_.bstack11ll111l1ll_opy_(bstack11ll_opy_ (u"ࠢࡼࡿࡂࡦࡺ࡯࡬ࡥࡐࡤࡱࡪࡃࡻࡾࠨࡥࡹ࡮ࡲࡤࡓࡷࡱࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸ࠽ࡼࡿࠩࡴࡷࡵࡪࡦࡥࡷࡒࡦࡳࡥ࠾ࡽࢀࠦᝨ").format(self.bstack11l1ll1llll_opy_, self.config.get(bstack11ll_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡎࡢ࡯ࡨࠫᝩ")), os.environ.get(bstack11ll_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡄࡘࡍࡑࡊ࡟ࡓࡗࡑࡣࡎࡊࡅࡏࡖࡌࡊࡎࡋࡒࠨᝪ")), self.config.get(bstack11ll_opy_ (u"ࠪࡴࡷࡵࡪࡦࡥࡷࡒࡦࡳࡥࠨᝫ"))))
            if response.get(bstack11ll_opy_ (u"ࠦࡸࡺࡡࡵࡷࡶࠦᝬ")) == 200:
                failed_count = response.get(bstack11ll_opy_ (u"ࠧ࡬ࡡࡪ࡮ࡨࡨ࡙࡫ࡳࡵࡵࡆࡳࡺࡴࡴࠣ᝭"), 0)
                self.logger.debug(bstack11ll_opy_ (u"ࠨࡐࡰ࡮࡯ࡩࡩࠦࡦࡢ࡫࡯ࡩࡩࠦࡴࡦࡵࡷࡷࠥࡩ࡯ࡶࡰࡷ࠾ࠥࢁࡽࠣᝮ").format(failed_count))
                if failed_count >= self.bstack11l1llllll1_opy_:
                    self.logger.info(bstack11ll_opy_ (u"ࠢࡕࡪࡵࡩࡸ࡮࡯࡭ࡦࠣࡧࡷࡵࡳࡴࡧࡧ࠾ࠥࢁࡽࠡࡀࡀࠤࢀࢃࠢᝯ").format(failed_count, self.bstack11l1llllll1_opy_))
                    self.bstack11l1lll111l_opy_(failed_count)
                    self.bstack11l1lll1l1l_opy_ = True
            else:
                self.logger.error(bstack11ll_opy_ (u"ࠣࡈࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤࡵࡵ࡬࡭ࠢࡩࡥ࡮ࡲࡥࡥࠢࡷࡩࡸࡺࡳ࠻ࠢࡾࢁࠧᝰ").format(response))
        except Exception as e:
            self.logger.error(bstack11ll_opy_ (u"ࠤࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥࡪࡵࡳ࡫ࡱ࡫ࠥࡶ࡯࡭࡮࡬ࡲ࡬ࡀࠠࡼࡿࠥ᝱").format(e))
    def bstack11l1lll111l_opy_(self, failed_count):
        with open(self.bstack11l1lll1ll1_opy_, bstack11ll_opy_ (u"ࠥࡻࠧᝲ")) as f:
            f.write(bstack11ll_opy_ (u"࡙ࠦ࡮ࡲࡦࡵ࡫ࡳࡱࡪࠠࡤࡴࡲࡷࡸ࡫ࡤࠡࡣࡷࠤࢀࢃ࡜࡯ࠤᝳ").format(datetime.now()))
            f.write(bstack11ll_opy_ (u"ࠧࡌࡡࡪ࡮ࡨࡨࠥࡺࡥࡴࡶࡶࠤࡨࡵࡵ࡯ࡶ࠽ࠤࢀࢃ࡜࡯ࠤ᝴").format(failed_count))
        self.logger.debug(bstack11ll_opy_ (u"ࠨࡁࡣࡱࡵࡸࠥࡈࡵࡪ࡮ࡧࠤ࡫࡯࡬ࡦࠢࡦࡶࡪࡧࡴࡦࡦ࠽ࠤࢀࢃࠢ᝵").format(self.bstack11l1lll1ll1_opy_))
    def bstack11l1llll11l_opy_(self):
        def bstack11l1llll1l1_opy_():
            while not self.bstack11l1lll1l1l_opy_:
                time.sleep(bstack11l1llll1ll_opy_)
                self.bstack11l1lll11ll_opy_()
                self.bstack11ll111l1ll_opy_()
        bstack11l1lllll1l_opy_ = threading.Thread(target=bstack11l1llll1l1_opy_, daemon=True)
        bstack11l1lllll1l_opy_.start()