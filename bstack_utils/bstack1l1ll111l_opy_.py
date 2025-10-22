# coding: UTF-8
import sys
bstack1l11l_opy_ = sys.version_info [0] == 2
bstack1111_opy_ = 2048
bstack1lll1_opy_ = 7
def bstack1lllll1l_opy_ (bstack1ll1l11_opy_):
    global bstack11l1ll_opy_
    bstack111lll_opy_ = ord (bstack1ll1l11_opy_ [-1])
    bstack1l111l1_opy_ = bstack1ll1l11_opy_ [:-1]
    bstack1111l_opy_ = bstack111lll_opy_ % len (bstack1l111l1_opy_)
    bstack1111ll_opy_ = bstack1l111l1_opy_ [:bstack1111l_opy_] + bstack1l111l1_opy_ [bstack1111l_opy_:]
    if bstack1l11l_opy_:
        bstack1l1l1_opy_ = unicode () .join ([unichr (ord (char) - bstack1111_opy_ - (bstack1ll1111_opy_ + bstack111lll_opy_) % bstack1lll1_opy_) for bstack1ll1111_opy_, char in enumerate (bstack1111ll_opy_)])
    else:
        bstack1l1l1_opy_ = str () .join ([chr (ord (char) - bstack1111_opy_ - (bstack1ll1111_opy_ + bstack111lll_opy_) % bstack1lll1_opy_) for bstack1ll1111_opy_, char in enumerate (bstack1111ll_opy_)])
    return eval (bstack1l1l1_opy_)
import threading
import tempfile
import os
import time
from datetime import datetime
from bstack_utils.bstack11ll1ll1lll_opy_ import bstack11ll1l1llll_opy_
from bstack_utils.constants import bstack11ll1lll11l_opy_, bstack1l11llll1_opy_
from bstack_utils.bstack111l1l1l_opy_ import bstack111l11ll_opy_
from bstack_utils import bstack11llll111l_opy_
bstack11l1lll1ll1_opy_ = 10
class bstack1l111l111_opy_:
    def __init__(self, bstack111l1ll1ll_opy_, config, bstack11l1lllll11_opy_=0):
        self.bstack11l1lll1lll_opy_ = set()
        self.lock = threading.Lock()
        self.bstack11l1lll1l1l_opy_ = bstack1lllll1l_opy_ (u"ࠧࢁࡽ࠰ࡶࡨࡷࡹࡵࡲࡤࡪࡨࡷࡹࡸࡡࡵ࡫ࡲࡲ࠴ࡧࡰࡪ࠱ࡹ࠵࠴࡬ࡡࡪ࡮ࡨࡨ࠲ࡺࡥࡴࡶࡶࠦᝊ").format(bstack11ll1lll11l_opy_)
        self.bstack11l1lllll1l_opy_ = os.path.join(tempfile.gettempdir(), bstack1lllll1l_opy_ (u"ࠨࡡࡣࡱࡵࡸࡤࡨࡵࡪ࡮ࡧࡣࢀࢃࠢᝋ").format(os.environ.get(bstack1lllll1l_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡖࡗࡌࡈࠬᝌ"))))
        self.bstack11l1ll1llll_opy_ = os.path.join(tempfile.gettempdir(), bstack1lllll1l_opy_ (u"ࠣࡨࡤ࡭ࡱ࡫ࡤࡠࡶࡨࡷࡹࡹ࡟ࡼࡿ࠱ࡸࡽࡺࠢᝍ").format(os.environ.get(bstack1lllll1l_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡎࡕࡃࡡࡘ࡙ࡎࡊࠧᝎ"))))
        self.bstack11ll1111111_opy_ = 2
        self.bstack111l1ll1ll_opy_ = bstack111l1ll1ll_opy_
        self.config = config
        self.logger = bstack11llll111l_opy_.get_logger(__name__, bstack1l11llll1_opy_)
        self.bstack11l1lllll11_opy_ = bstack11l1lllll11_opy_
        self.bstack11l1llll1ll_opy_ = False
        self.bstack11l1llll11l_opy_ = not (
                            os.environ.get(bstack1lllll1l_opy_ (u"ࠥࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡅ࡙ࡎࡒࡄࡠࡔࡘࡒࡤࡏࡄࡆࡐࡗࡍࡋࡏࡅࡓࠤᝏ")) and
                            os.environ.get(bstack1lllll1l_opy_ (u"ࠦࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡒࡔࡊࡅࡠࡋࡑࡈࡊ࡞ࠢᝐ")) and
                            os.environ.get(bstack1lllll1l_opy_ (u"ࠧࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡕࡔࡂࡎࡢࡒࡔࡊࡅࡠࡅࡒ࡙ࡓ࡚ࠢᝑ"))
                        )
        if bstack111l11ll_opy_.bstack11l1ll1lll1_opy_(config):
            self.bstack11ll1111111_opy_ = bstack111l11ll_opy_.bstack11l1llllll1_opy_(config, self.bstack11l1lllll11_opy_)
            self.bstack11l1lll1111_opy_()
    def bstack11l1llll1l1_opy_(self):
        return bstack1lllll1l_opy_ (u"ࠨࡻࡾࡡࡾࢁࠧᝒ").format(self.config.get(bstack1lllll1l_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡔࡡ࡮ࡧࠪᝓ")), os.environ.get(bstack1lllll1l_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡃࡗࡌࡐࡉࡥࡒࡖࡐࡢࡍࡉࡋࡎࡕࡋࡉࡍࡊࡘࠧ᝔")))
    def bstack11l1lllllll_opy_(self):
        try:
            if self.bstack11l1llll11l_opy_:
                return
            with self.lock:
                try:
                    with open(self.bstack11l1ll1llll_opy_, bstack1lllll1l_opy_ (u"ࠤࡵࠦ᝕")) as f:
                        bstack11ll111111l_opy_ = set(line.strip() for line in f if line.strip())
                except FileNotFoundError:
                    bstack11ll111111l_opy_ = set()
                bstack11l1llll111_opy_ = bstack11ll111111l_opy_ - self.bstack11l1lll1lll_opy_
                if not bstack11l1llll111_opy_:
                    return
                self.bstack11l1lll1lll_opy_.update(bstack11l1llll111_opy_)
                data = {bstack1lllll1l_opy_ (u"ࠥࡪࡦ࡯࡬ࡦࡦࡗࡩࡸࡺࡳࠣ᝖"): list(self.bstack11l1lll1lll_opy_), bstack1lllll1l_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡑࡥࡲ࡫ࠢ᝗"): self.config.get(bstack1lllll1l_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡒࡦࡳࡥࠨ᝘")), bstack1lllll1l_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡗࡻ࡮ࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠦ᝙"): os.environ.get(bstack1lllll1l_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡂࡖࡋࡏࡈࡤࡘࡕࡏࡡࡌࡈࡊࡔࡔࡊࡈࡌࡉࡗ࠭᝚")), bstack1lllll1l_opy_ (u"ࠣࡲࡵࡳ࡯࡫ࡣࡵࡐࡤࡱࡪࠨ᝛"): self.config.get(bstack1lllll1l_opy_ (u"ࠩࡳࡶࡴࡰࡥࡤࡶࡑࡥࡲ࡫ࠧ᝜"))}
            response = bstack11ll1l1llll_opy_.bstack11ll111l11l_opy_(self.bstack11l1lll1l1l_opy_, data)
            if response.get(bstack1lllll1l_opy_ (u"ࠥࡷࡹࡧࡴࡶࡵࠥ᝝")) == 200:
                self.logger.debug(bstack1lllll1l_opy_ (u"ࠦࡘࡻࡣࡤࡧࡶࡷ࡫ࡻ࡬࡭ࡻࠣࡷࡪࡴࡴࠡࡨࡤ࡭ࡱ࡫ࡤࠡࡶࡨࡷࡹࡹ࠺ࠡࡽࢀࠦ᝞").format(data))
            else:
                self.logger.debug(bstack1lllll1l_opy_ (u"ࠧࡌࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡࡵࡨࡲࡩࠦࡦࡢ࡫࡯ࡩࡩࠦࡴࡦࡵࡷࡷ࠿ࠦࡻࡾࠤ᝟").format(response))
        except Exception as e:
            self.logger.debug(bstack1lllll1l_opy_ (u"ࠨࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢࡧࡹࡷ࡯࡮ࡨࠢࡶࡩࡳࡪࡩ࡯ࡩࠣࡪࡦ࡯࡬ࡦࡦࠣࡸࡪࡹࡴࡴ࠼ࠣࡿࢂࠨᝠ").format(e))
    def bstack11ll111ll11_opy_(self):
        if self.bstack11l1llll11l_opy_:
            with self.lock:
                try:
                    with open(self.bstack11l1ll1llll_opy_, bstack1lllll1l_opy_ (u"ࠢࡳࠤᝡ")) as f:
                        bstack11l1lll11ll_opy_ = set(line.strip() for line in f if line.strip())
                    failed_count = len(bstack11l1lll11ll_opy_)
                except FileNotFoundError:
                    failed_count = 0
                self.logger.debug(bstack1lllll1l_opy_ (u"ࠣࡒࡲࡰࡱ࡫ࡤࠡࡨࡤ࡭ࡱ࡫ࡤࠡࡶࡨࡷࡹࡹࠠࡤࡱࡸࡲࡹࠦࠨ࡭ࡱࡦࡥࡱ࠯࠺ࠡࡽࢀࠦᝢ").format(failed_count))
                if failed_count >= self.bstack11ll1111111_opy_:
                    self.logger.info(bstack1lllll1l_opy_ (u"ࠤࡗ࡬ࡷ࡫ࡳࡩࡱ࡯ࡨࠥࡩࡲࡰࡵࡶࡩࡩࠦࠨ࡭ࡱࡦࡥࡱ࠯࠺ࠡࡽࢀࠤࡃࡃࠠࡼࡿࠥᝣ").format(failed_count, self.bstack11ll1111111_opy_))
                    self.bstack11l1lll111l_opy_(failed_count)
                    self.bstack11l1llll1ll_opy_ = True
            return
        try:
            response = bstack11ll1l1llll_opy_.bstack11ll111ll11_opy_(bstack1lllll1l_opy_ (u"ࠥࡿࢂࡅࡢࡶ࡫࡯ࡨࡓࡧ࡭ࡦ࠿ࡾࢁࠫࡨࡵࡪ࡮ࡧࡖࡺࡴࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࡀࡿࢂࠬࡰࡳࡱ࡭ࡩࡨࡺࡎࡢ࡯ࡨࡁࢀࢃࠢᝤ").format(self.bstack11l1lll1l1l_opy_, self.config.get(bstack1lllll1l_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡑࡥࡲ࡫ࠧᝥ")), os.environ.get(bstack1lllll1l_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡇ࡛ࡉࡍࡆࡢࡖ࡚ࡔ࡟ࡊࡆࡈࡒ࡙ࡏࡆࡊࡇࡕࠫᝦ")), self.config.get(bstack1lllll1l_opy_ (u"࠭ࡰࡳࡱ࡭ࡩࡨࡺࡎࡢ࡯ࡨࠫᝧ"))))
            if response.get(bstack1lllll1l_opy_ (u"ࠢࡴࡶࡤࡸࡺࡹࠢᝨ")) == 200:
                failed_count = response.get(bstack1lllll1l_opy_ (u"ࠣࡨࡤ࡭ࡱ࡫ࡤࡕࡧࡶࡸࡸࡉ࡯ࡶࡰࡷࠦᝩ"), 0)
                self.logger.debug(bstack1lllll1l_opy_ (u"ࠤࡓࡳࡱࡲࡥࡥࠢࡩࡥ࡮ࡲࡥࡥࠢࡷࡩࡸࡺࡳࠡࡥࡲࡹࡳࡺ࠺ࠡࡽࢀࠦᝪ").format(failed_count))
                if failed_count >= self.bstack11ll1111111_opy_:
                    self.logger.info(bstack1lllll1l_opy_ (u"ࠥࡘ࡭ࡸࡥࡴࡪࡲࡰࡩࠦࡣࡳࡱࡶࡷࡪࡪ࠺ࠡࡽࢀࠤࡃࡃࠠࡼࡿࠥᝫ").format(failed_count, self.bstack11ll1111111_opy_))
                    self.bstack11l1lll111l_opy_(failed_count)
                    self.bstack11l1llll1ll_opy_ = True
            else:
                self.logger.error(bstack1lllll1l_opy_ (u"ࠦࡋࡧࡩ࡭ࡧࡧࠤࡹࡵࠠࡱࡱ࡯ࡰࠥ࡬ࡡࡪ࡮ࡨࡨࠥࡺࡥࡴࡶࡶ࠾ࠥࢁࡽࠣᝬ").format(response))
        except Exception as e:
            self.logger.error(bstack1lllll1l_opy_ (u"ࠧࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡࡦࡸࡶ࡮ࡴࡧࠡࡲࡲࡰࡱ࡯࡮ࡨ࠼ࠣࡿࢂࠨ᝭").format(e))
    def bstack11l1lll111l_opy_(self, failed_count):
        with open(self.bstack11l1lllll1l_opy_, bstack1lllll1l_opy_ (u"ࠨࡷࠣᝮ")) as f:
            f.write(bstack1lllll1l_opy_ (u"ࠢࡕࡪࡵࡩࡸ࡮࡯࡭ࡦࠣࡧࡷࡵࡳࡴࡧࡧࠤࡦࡺࠠࡼࡿ࡟ࡲࠧᝯ").format(datetime.now()))
            f.write(bstack1lllll1l_opy_ (u"ࠣࡈࡤ࡭ࡱ࡫ࡤࠡࡶࡨࡷࡹࡹࠠࡤࡱࡸࡲࡹࡀࠠࡼࡿ࡟ࡲࠧᝰ").format(failed_count))
        self.logger.debug(bstack1lllll1l_opy_ (u"ࠤࡄࡦࡴࡸࡴࠡࡄࡸ࡭ࡱࡪࠠࡧ࡫࡯ࡩࠥࡩࡲࡦࡣࡷࡩࡩࡀࠠࡼࡿࠥ᝱").format(self.bstack11l1lllll1l_opy_))
    def bstack11l1lll1111_opy_(self):
        def bstack11l1lll11l1_opy_():
            while not self.bstack11l1llll1ll_opy_:
                time.sleep(bstack11l1lll1ll1_opy_)
                self.bstack11l1lllllll_opy_()
                self.bstack11ll111ll11_opy_()
        bstack11l1lll1l11_opy_ = threading.Thread(target=bstack11l1lll11l1_opy_, daemon=True)
        bstack11l1lll1l11_opy_.start()