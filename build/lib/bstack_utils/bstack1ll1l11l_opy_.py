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
import json
import logging
import os
import datetime
import threading
from bstack_utils.constants import EVENTS, STAGE
from bstack_utils.helper import bstack111l1111l1l_opy_, bstack111l11ll1ll_opy_, bstack1l1l1l1l1l_opy_, error_handler, bstack111l1l11l11_opy_, bstack111l1lll1ll_opy_, bstack1111l1ll111_opy_, bstack1ll1llll_opy_, bstack1l1l1l1l_opy_
from bstack_utils.measure import measure
from bstack_utils.bstack11l11l1l111_opy_ import bstack111ll111l11_opy_
import bstack_utils.bstack1111ll1111_opy_ as bstack1l1l1l1111_opy_
from bstack_utils.bstack11llllll_opy_ import bstack1l11lll1_opy_
import bstack_utils.accessibility as bstack1lll1ll1l_opy_
from bstack_utils.bstack1l11111ll_opy_ import bstack1l11111ll_opy_
from bstack_utils.bstack1l1l111l_opy_ import bstack1ll1l1l1_opy_
from bstack_utils.constants import bstack1lll1l1lll_opy_
bstack1llll1l11l11_opy_ = bstack1l1lll1_opy_ (u"ࠧࡩࡶࡷࡴࡸࡀ࠯࠰ࡥࡲࡰࡱ࡫ࡣࡵࡱࡵ࠱ࡴࡨࡳࡦࡴࡹࡥࡧ࡯࡬ࡪࡶࡼ࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡧࡴࡳࠧ⃺")
logger = logging.getLogger(__name__)
class bstack1l11ll1l_opy_:
    bstack11l11l1l111_opy_ = None
    bs_config = None
    bstack11llllll1l_opy_ = None
    @classmethod
    @error_handler(class_method=True)
    @measure(event_name=EVENTS.bstack11l1l11ll11_opy_, stage=STAGE.bstack1111llll1l_opy_)
    def launch(cls, bs_config, bstack11llllll1l_opy_):
        cls.bs_config = bs_config
        cls.bstack11llllll1l_opy_ = bstack11llllll1l_opy_
        try:
            cls.bstack1llll1l1l111_opy_()
            bstack1llll1lll1l1_opy_ = bstack111l1111l1l_opy_(bs_config)
            bstack1lllll11l1l1_opy_ = bstack111l11ll1ll_opy_(bs_config)
            data = bstack1l1l1l1111_opy_.bstack1llll1l11lll_opy_(bs_config, bstack11llllll1l_opy_)
            config = {
                bstack1l1lll1_opy_ (u"ࠨࡣࡸࡸ࡭࠭⃻"): (bstack1llll1lll1l1_opy_, bstack1lllll11l1l1_opy_),
                bstack1l1lll1_opy_ (u"ࠩ࡫ࡩࡦࡪࡥࡳࡵࠪ⃼"): cls.default_headers()
            }
            response = bstack1l1l1l1l1l_opy_(bstack1l1lll1_opy_ (u"ࠪࡔࡔ࡙ࡔࠨ⃽"), cls.request_url(bstack1l1lll1_opy_ (u"ࠫࡦࡶࡩ࠰ࡸ࠵࠳ࡧࡻࡩ࡭ࡦࡶࠫ⃾")), data, config)
            if response.status_code != 200:
                bstack11ll11111l_opy_ = response.json()
                if bstack11ll11111l_opy_[bstack1l1lll1_opy_ (u"ࠬࡹࡵࡤࡥࡨࡷࡸ࠭⃿")] == False:
                    cls.bstack1llll11ll1ll_opy_(bstack11ll11111l_opy_)
                    return
                cls.bstack1llll1l111l1_opy_(bstack11ll11111l_opy_[bstack1l1lll1_opy_ (u"࠭࡯ࡣࡵࡨࡶࡻࡧࡢࡪ࡮࡬ࡸࡾ࠭℀")])
                cls.bstack1llll11ll111_opy_(bstack11ll11111l_opy_[bstack1l1lll1_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠧ℁")])
                return None
            bstack1llll1l1l1l1_opy_ = cls.bstack1llll1l1ll11_opy_(response)
            return bstack1llll1l1l1l1_opy_, response.json()
        except Exception as error:
            logger.error(bstack1l1lll1_opy_ (u"ࠣࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤࡼ࡮ࡩ࡭ࡧࠣࡧࡷ࡫ࡡࡵ࡫ࡱ࡫ࠥࡨࡵࡪ࡮ࡧࠤ࡫ࡵࡲࠡࡖࡨࡷࡹࡎࡵࡣ࠼ࠣࡿࢂࠨℂ").format(str(error)))
            return None
    @classmethod
    @error_handler(class_method=True)
    def stop(cls, bstack1llll1l1111l_opy_=None):
        if not bstack1l11lll1_opy_.on() and not bstack1lll1ll1l_opy_.on():
            return
        if os.environ.get(bstack1l1lll1_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡎࡕࡃࡡࡍ࡛࡙࠭℃")) == bstack1l1lll1_opy_ (u"ࠥࡲࡺࡲ࡬ࠣ℄") or os.environ.get(bstack1l1lll1_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡉࡗࡅࡣ࡚࡛ࡉࡅࠩ℅")) == bstack1l1lll1_opy_ (u"ࠧࡴࡵ࡭࡮ࠥ℆"):
            logger.error(bstack1l1lll1_opy_ (u"࠭ࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥࡹࡴࡰࡲࠣࡦࡺ࡯࡬ࡥࠢࡵࡩࡶࡻࡥࡴࡶࠣࡸࡴࠦࡔࡦࡵࡷࡌࡺࡨ࠺ࠡࡏ࡬ࡷࡸ࡯࡮ࡨࠢࡤࡹࡹ࡮ࡥ࡯ࡶ࡬ࡧࡦࡺࡩࡰࡰࠣࡸࡴࡱࡥ࡯ࠩℇ"))
            return {
                bstack1l1lll1_opy_ (u"ࠧࡴࡶࡤࡸࡺࡹࠧ℈"): bstack1l1lll1_opy_ (u"ࠨࡧࡵࡶࡴࡸࠧ℉"),
                bstack1l1lll1_opy_ (u"ࠩࡰࡩࡸࡹࡡࡨࡧࠪℊ"): bstack1l1lll1_opy_ (u"ࠪࡘࡴࡱࡥ࡯࠱ࡥࡹ࡮ࡲࡤࡊࡆࠣ࡭ࡸࠦࡵ࡯ࡦࡨࡪ࡮ࡴࡥࡥ࠮ࠣࡦࡺ࡯࡬ࡥࠢࡦࡶࡪࡧࡴࡪࡱࡱࠤࡲ࡯ࡧࡩࡶࠣ࡬ࡦࡼࡥࠡࡨࡤ࡭ࡱ࡫ࡤࠨℋ")
            }
        try:
            cls.bstack11l11l1l111_opy_.shutdown()
            data = {
                bstack1l1lll1_opy_ (u"ࠫ࡫࡯࡮ࡪࡵ࡫ࡩࡩࡥࡡࡵࠩℌ"): bstack1ll1llll_opy_()
            }
            if not bstack1llll1l1111l_opy_ is None:
                data[bstack1l1lll1_opy_ (u"ࠬ࡬ࡩ࡯࡫ࡶ࡬ࡪࡪ࡟࡮ࡧࡷࡥࡩࡧࡴࡢࠩℍ")] = [{
                    bstack1l1lll1_opy_ (u"࠭ࡲࡦࡣࡶࡳࡳ࠭ℎ"): bstack1l1lll1_opy_ (u"ࠧࡶࡵࡨࡶࡤࡱࡩ࡭࡮ࡨࡨࠬℏ"),
                    bstack1l1lll1_opy_ (u"ࠨࡵ࡬࡫ࡳࡧ࡬ࠨℐ"): bstack1llll1l1111l_opy_
                }]
            config = {
                bstack1l1lll1_opy_ (u"ࠩ࡫ࡩࡦࡪࡥࡳࡵࠪℑ"): cls.default_headers()
            }
            bstack11ll11l1l11_opy_ = bstack1l1lll1_opy_ (u"ࠪࡥࡵ࡯࠯ࡷ࠳࠲ࡦࡺ࡯࡬ࡥࡵ࠲ࡿࢂ࠵ࡳࡵࡱࡳࠫℒ").format(os.environ[bstack1l1lll1_opy_ (u"ࠦࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡉࡗࡅࡣ࡚࡛ࡉࡅࠤℓ")])
            bstack1llll1l11ll1_opy_ = cls.request_url(bstack11ll11l1l11_opy_)
            response = bstack1l1l1l1l1l_opy_(bstack1l1lll1_opy_ (u"ࠬࡖࡕࡕࠩ℔"), bstack1llll1l11ll1_opy_, data, config)
            if not response.ok:
                raise Exception(bstack1l1lll1_opy_ (u"ࠨࡓࡵࡱࡳࠤࡷ࡫ࡱࡶࡧࡶࡸࠥࡴ࡯ࡵࠢࡲ࡯ࠧℕ"))
        except Exception as error:
            logger.error(bstack1l1lll1_opy_ (u"ࠢࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣ࡭ࡳࠦࡳࡵࡱࡳࠤࡧࡻࡩ࡭ࡦࠣࡶࡪࡷࡵࡦࡵࡷࠤࡹࡵࠠࡕࡧࡶࡸࡍࡻࡢ࠻࠼ࠣࠦ№") + str(error))
            return {
                bstack1l1lll1_opy_ (u"ࠨࡵࡷࡥࡹࡻࡳࠨ℗"): bstack1l1lll1_opy_ (u"ࠩࡨࡶࡷࡵࡲࠨ℘"),
                bstack1l1lll1_opy_ (u"ࠪࡱࡪࡹࡳࡢࡩࡨࠫℙ"): str(error)
            }
    @classmethod
    @error_handler(class_method=True)
    def bstack1llll1l1ll11_opy_(cls, response):
        bstack11ll11111l_opy_ = response.json() if not isinstance(response, dict) else response
        bstack1llll1l1l1l1_opy_ = {}
        if bstack11ll11111l_opy_.get(bstack1l1lll1_opy_ (u"ࠫ࡯ࡽࡴࠨℚ")) is None:
            os.environ[bstack1l1lll1_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡊࡘࡆࡤࡐࡗࡕࠩℛ")] = bstack1l1lll1_opy_ (u"࠭࡮ࡶ࡮࡯ࠫℜ")
        else:
            os.environ[bstack1l1lll1_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡋ࡙ࡗࠫℝ")] = bstack11ll11111l_opy_.get(bstack1l1lll1_opy_ (u"ࠨ࡬ࡺࡸࠬ℞"), bstack1l1lll1_opy_ (u"ࠩࡱࡹࡱࡲࠧ℟"))
        os.environ[bstack1l1lll1_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚ࡈࡖࡄࡢ࡙࡚ࡏࡄࠨ℠")] = bstack11ll11111l_opy_.get(bstack1l1lll1_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡢ࡬ࡦࡹࡨࡦࡦࡢ࡭ࡩ࠭℡"), bstack1l1lll1_opy_ (u"ࠬࡴࡵ࡭࡮ࠪ™"))
        logger.info(bstack1l1lll1_opy_ (u"࠭ࡔࡦࡵࡷ࡬ࡺࡨࠠࡴࡶࡤࡶࡹ࡫ࡤࠡࡹ࡬ࡸ࡭ࠦࡩࡥ࠼ࠣࠫ℣") + os.getenv(bstack1l1lll1_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡖࡗࡌࡈࠬℤ")));
        if bstack1l11lll1_opy_.bstack11l11l11lll_opy_(cls.bs_config, cls.bstack11llllll1l_opy_.get(bstack1l1lll1_opy_ (u"ࠨࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡺࡹࡥࡥࠩ℥"), bstack1l1lll1_opy_ (u"ࠩࠪΩ"))) is True:
            bstack11ll11l1l1l_opy_, build_hashed_id, bstack1llll1l1llll_opy_ = cls.bstack1llll1l1ll1l_opy_(bstack11ll11111l_opy_)
            if bstack11ll11l1l1l_opy_ != None and build_hashed_id != None:
                bstack1llll1l1l1l1_opy_[bstack1l1lll1_opy_ (u"ࠪࡳࡧࡹࡥࡳࡸࡤࡦ࡮ࡲࡩࡵࡻࠪ℧")] = {
                    bstack1l1lll1_opy_ (u"ࠫ࡯ࡽࡴࡠࡶࡲ࡯ࡪࡴࠧℨ"): bstack11ll11l1l1l_opy_,
                    bstack1l1lll1_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡣ࡭ࡧࡳࡩࡧࡧࡣ࡮ࡪࠧ℩"): build_hashed_id,
                    bstack1l1lll1_opy_ (u"࠭ࡡ࡭࡮ࡲࡻࡤࡹࡣࡳࡧࡨࡲࡸ࡮࡯ࡵࡵࠪK"): bstack1llll1l1llll_opy_
                }
            else:
                bstack1llll1l1l1l1_opy_[bstack1l1lll1_opy_ (u"ࠧࡰࡤࡶࡩࡷࡼࡡࡣ࡫࡯࡭ࡹࡿࠧÅ")] = {}
        else:
            bstack1llll1l1l1l1_opy_[bstack1l1lll1_opy_ (u"ࠨࡱࡥࡷࡪࡸࡶࡢࡤ࡬ࡰ࡮ࡺࡹࠨℬ")] = {}
        bstack1llll1l11l1l_opy_, build_hashed_id = cls.bstack1llll11lll1l_opy_(bstack11ll11111l_opy_)
        if bstack1llll1l11l1l_opy_ != None and build_hashed_id != None:
            bstack1llll1l1l1l1_opy_[bstack1l1lll1_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠩℭ")] = {
                bstack1l1lll1_opy_ (u"ࠪࡥࡺࡺࡨࡠࡶࡲ࡯ࡪࡴࠧ℮"): bstack1llll1l11l1l_opy_,
                bstack1l1lll1_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡢ࡬ࡦࡹࡨࡦࡦࡢ࡭ࡩ࠭ℯ"): build_hashed_id,
            }
        else:
            bstack1llll1l1l1l1_opy_[bstack1l1lll1_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠬℰ")] = {}
        if bstack1llll1l1l1l1_opy_[bstack1l1lll1_opy_ (u"࠭࡯ࡣࡵࡨࡶࡻࡧࡢࡪ࡮࡬ࡸࡾ࠭ℱ")].get(bstack1l1lll1_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡥࡨࡢࡵ࡫ࡩࡩࡥࡩࡥࠩℲ")) != None or bstack1llll1l1l1l1_opy_[bstack1l1lll1_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠨℳ")].get(bstack1l1lll1_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡠࡪࡤࡷ࡭࡫ࡤࡠ࡫ࡧࠫℴ")) != None:
            cls.bstack1llll1l111ll_opy_(bstack11ll11111l_opy_.get(bstack1l1lll1_opy_ (u"ࠪ࡮ࡼࡺࠧℵ")), bstack11ll11111l_opy_.get(bstack1l1lll1_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡢ࡬ࡦࡹࡨࡦࡦࡢ࡭ࡩ࠭ℶ")))
        return bstack1llll1l1l1l1_opy_
    @classmethod
    def bstack1llll1l1ll1l_opy_(cls, bstack11ll11111l_opy_):
        if bstack11ll11111l_opy_.get(bstack1l1lll1_opy_ (u"ࠬࡵࡢࡴࡧࡵࡺࡦࡨࡩ࡭࡫ࡷࡽࠬℷ")) == None:
            cls.bstack1llll1l111l1_opy_()
            return [None, None, None]
        if bstack11ll11111l_opy_[bstack1l1lll1_opy_ (u"࠭࡯ࡣࡵࡨࡶࡻࡧࡢࡪ࡮࡬ࡸࡾ࠭ℸ")][bstack1l1lll1_opy_ (u"ࠧࡴࡷࡦࡧࡪࡹࡳࠨℹ")] != True:
            cls.bstack1llll1l111l1_opy_(bstack11ll11111l_opy_[bstack1l1lll1_opy_ (u"ࠨࡱࡥࡷࡪࡸࡶࡢࡤ࡬ࡰ࡮ࡺࡹࠨ℺")])
            return [None, None, None]
        logger.debug(bstack1l1lll1_opy_ (u"ࠩࡾࢁࠥࡈࡵࡪ࡮ࡧࠤࡨࡸࡥࡢࡶ࡬ࡳࡳࠦࡓࡶࡥࡦࡩࡸࡹࡦࡶ࡮ࠤࠫ℻").format(bstack1lll1l1lll_opy_))
        os.environ[bstack1l1lll1_opy_ (u"ࠪࡆࡘࡥࡔࡆࡕࡗࡓࡕ࡙࡟ࡃࡗࡌࡐࡉࡥࡃࡐࡏࡓࡐࡊ࡚ࡅࡅࠩℼ")] = bstack1l1lll1_opy_ (u"ࠫࡹࡸࡵࡦࠩℽ")
        if bstack11ll11111l_opy_.get(bstack1l1lll1_opy_ (u"ࠬࡰࡷࡵࠩℾ")):
            os.environ[bstack1l1lll1_opy_ (u"࠭ࡃࡓࡇࡇࡉࡓ࡚ࡉࡂࡎࡖࡣࡋࡕࡒࡠࡅࡕࡅࡘࡎ࡟ࡓࡇࡓࡓࡗ࡚ࡉࡏࡉࠪℿ")] = json.dumps({
                bstack1l1lll1_opy_ (u"ࠧࡶࡵࡨࡶࡳࡧ࡭ࡦࠩ⅀"): bstack111l1111l1l_opy_(cls.bs_config),
                bstack1l1lll1_opy_ (u"ࠨࡲࡤࡷࡸࡽ࡯ࡳࡦࠪ⅁"): bstack111l11ll1ll_opy_(cls.bs_config)
            })
        if bstack11ll11111l_opy_.get(bstack1l1lll1_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡠࡪࡤࡷ࡭࡫ࡤࡠ࡫ࡧࠫ⅂")):
            os.environ[bstack1l1lll1_opy_ (u"ࠪࡆࡘࡥࡔࡆࡕࡗࡓࡕ࡙࡟ࡃࡗࡌࡐࡉࡥࡈࡂࡕࡋࡉࡉࡥࡉࡅࠩ⅃")] = bstack11ll11111l_opy_[bstack1l1lll1_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡢ࡬ࡦࡹࡨࡦࡦࡢ࡭ࡩ࠭⅄")]
        if bstack11ll11111l_opy_[bstack1l1lll1_opy_ (u"ࠬࡵࡢࡴࡧࡵࡺࡦࡨࡩ࡭࡫ࡷࡽࠬⅅ")].get(bstack1l1lll1_opy_ (u"࠭࡯ࡱࡶ࡬ࡳࡳࡹࠧⅆ"), {}).get(bstack1l1lll1_opy_ (u"ࠧࡢ࡮࡯ࡳࡼࡥࡳࡤࡴࡨࡩࡳࡹࡨࡰࡶࡶࠫⅇ")):
            os.environ[bstack1l1lll1_opy_ (u"ࠨࡄࡖࡣ࡙ࡋࡓࡕࡑࡓࡗࡤࡇࡌࡍࡑ࡚ࡣࡘࡉࡒࡆࡇࡑࡗࡍࡕࡔࡔࠩⅈ")] = str(bstack11ll11111l_opy_[bstack1l1lll1_opy_ (u"ࠩࡲࡦࡸ࡫ࡲࡷࡣࡥ࡭ࡱ࡯ࡴࡺࠩⅉ")][bstack1l1lll1_opy_ (u"ࠪࡳࡵࡺࡩࡰࡰࡶࠫ⅊")][bstack1l1lll1_opy_ (u"ࠫࡦࡲ࡬ࡰࡹࡢࡷࡨࡸࡥࡦࡰࡶ࡬ࡴࡺࡳࠨ⅋")])
        else:
            os.environ[bstack1l1lll1_opy_ (u"ࠬࡈࡓࡠࡖࡈࡗ࡙ࡕࡐࡔࡡࡄࡐࡑࡕࡗࡠࡕࡆࡖࡊࡋࡎࡔࡊࡒࡘࡘ࠭⅌")] = bstack1l1lll1_opy_ (u"ࠨ࡮ࡶ࡮࡯ࠦ⅍")
        return [bstack11ll11111l_opy_[bstack1l1lll1_opy_ (u"ࠧ࡫ࡹࡷࠫⅎ")], bstack11ll11111l_opy_[bstack1l1lll1_opy_ (u"ࠨࡤࡸ࡭ࡱࡪ࡟ࡩࡣࡶ࡬ࡪࡪ࡟ࡪࡦࠪ⅏")], os.environ[bstack1l1lll1_opy_ (u"ࠩࡅࡗࡤ࡚ࡅࡔࡖࡒࡔࡘࡥࡁࡍࡎࡒ࡛ࡤ࡙ࡃࡓࡇࡈࡒࡘࡎࡏࡕࡕࠪ⅐")]]
    @classmethod
    def bstack1llll11lll1l_opy_(cls, bstack11ll11111l_opy_):
        if bstack11ll11111l_opy_.get(bstack1l1lll1_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠪ⅑")) == None:
            cls.bstack1llll11ll111_opy_()
            return [None, None]
        if bstack11ll11111l_opy_[bstack1l1lll1_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠫ⅒")][bstack1l1lll1_opy_ (u"ࠬࡹࡵࡤࡥࡨࡷࡸ࠭⅓")] != True:
            cls.bstack1llll11ll111_opy_(bstack11ll11111l_opy_[bstack1l1lll1_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾ࠭⅔")])
            return [None, None]
        if bstack11ll11111l_opy_[bstack1l1lll1_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠧ⅕")].get(bstack1l1lll1_opy_ (u"ࠨࡱࡳࡸ࡮ࡵ࡮ࡴࠩ⅖")):
            logger.debug(bstack1l1lll1_opy_ (u"ࠩࡗࡩࡸࡺࠠࡂࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡃࡷ࡬ࡰࡩࠦࡣࡳࡧࡤࡸ࡮ࡵ࡮ࠡࡕࡸࡧࡨ࡫ࡳࡴࡨࡸࡰࠦ࠭⅗"))
            parsed = json.loads(os.getenv(bstack1l1lll1_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚࡟ࡂࡅࡆࡉࡘ࡙ࡉࡃࡋࡏࡍ࡙࡟࡟ࡄࡑࡑࡊࡎࡍࡕࡓࡃࡗࡍࡔࡔ࡟࡚ࡏࡏࠫ⅘"), bstack1l1lll1_opy_ (u"ࠫࢀࢃࠧ⅙")))
            capabilities = bstack1l1l1l1111_opy_.bstack1llll1l1l11l_opy_(bstack11ll11111l_opy_[bstack1l1lll1_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠬ⅚")][bstack1l1lll1_opy_ (u"࠭࡯ࡱࡶ࡬ࡳࡳࡹࠧ⅛")][bstack1l1lll1_opy_ (u"ࠧࡤࡣࡳࡥࡧ࡯࡬ࡪࡶ࡬ࡩࡸ࠭⅜")], bstack1l1lll1_opy_ (u"ࠨࡰࡤࡱࡪ࠭⅝"), bstack1l1lll1_opy_ (u"ࠩࡹࡥࡱࡻࡥࠨ⅞"))
            bstack1llll1l11l1l_opy_ = capabilities[bstack1l1lll1_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࡗࡳࡰ࡫࡮ࠨ⅟")]
            os.environ[bstack1l1lll1_opy_ (u"ࠫࡇ࡙࡟ࡂ࠳࠴࡝ࡤࡐࡗࡕࠩⅠ")] = bstack1llll1l11l1l_opy_
            if bstack1l1lll1_opy_ (u"ࠧࡧࡵࡵࡱࡰࡥࡹ࡫ࠢⅡ") in bstack11ll11111l_opy_ and bstack11ll11111l_opy_.get(bstack1l1lll1_opy_ (u"ࠨࡡࡱࡲࡢࡥࡺࡺ࡯࡮ࡣࡷࡩࠧⅢ")) is None:
                parsed[bstack1l1lll1_opy_ (u"ࠧࡴࡥࡤࡲࡳ࡫ࡲࡗࡧࡵࡷ࡮ࡵ࡮ࠨⅣ")] = capabilities[bstack1l1lll1_opy_ (u"ࠨࡵࡦࡥࡳࡴࡥࡳࡘࡨࡶࡸ࡯࡯࡯ࠩⅤ")]
            os.environ[bstack1l1lll1_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡥࡁࡄࡅࡈࡗࡘࡏࡂࡊࡎࡌࡘ࡞ࡥࡃࡐࡐࡉࡍࡌ࡛ࡒࡂࡖࡌࡓࡓࡥ࡙ࡎࡎࠪⅥ")] = json.dumps(parsed)
            scripts = bstack1l1l1l1111_opy_.bstack1llll1l1l11l_opy_(bstack11ll11111l_opy_[bstack1l1lll1_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠪⅦ")][bstack1l1lll1_opy_ (u"ࠫࡴࡶࡴࡪࡱࡱࡷࠬⅧ")][bstack1l1lll1_opy_ (u"ࠬࡹࡣࡳ࡫ࡳࡸࡸ࠭Ⅸ")], bstack1l1lll1_opy_ (u"࠭࡮ࡢ࡯ࡨࠫⅩ"), bstack1l1lll1_opy_ (u"ࠧࡤࡱࡰࡱࡦࡴࡤࠨⅪ"))
            bstack1l11111ll_opy_.bstack11l11l1ll_opy_(scripts)
            commands = bstack11ll11111l_opy_[bstack1l1lll1_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠨⅫ")][bstack1l1lll1_opy_ (u"ࠩࡲࡴࡹ࡯࡯࡯ࡵࠪⅬ")][bstack1l1lll1_opy_ (u"ࠪࡧࡴࡳ࡭ࡢࡰࡧࡷ࡙ࡵࡗࡳࡣࡳࠫⅭ")].get(bstack1l1lll1_opy_ (u"ࠫࡨࡵ࡭࡮ࡣࡱࡨࡸ࠭Ⅾ"))
            bstack1l11111ll_opy_.bstack1lllll1l11l1_opy_(commands)
            bstack1lllll11llll_opy_ = capabilities.get(bstack1l1lll1_opy_ (u"ࠬ࡭࡯ࡰࡩ࠽ࡧ࡭ࡸ࡯࡮ࡧࡒࡴࡹ࡯࡯࡯ࡵࠪⅯ"))
            bstack1l11111ll_opy_.bstack1lllll11lll1_opy_(bstack1lllll11llll_opy_)
            bstack1l11111ll_opy_.store()
        return [bstack1llll1l11l1l_opy_, bstack11ll11111l_opy_[bstack1l1lll1_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡤ࡮ࡡࡴࡪࡨࡨࡤ࡯ࡤࠨⅰ")]]
    @classmethod
    def bstack1llll1l111l1_opy_(cls, response=None):
        os.environ[bstack1l1lll1_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡖࡗࡌࡈࠬⅱ")] = bstack1l1lll1_opy_ (u"ࠨࡰࡸࡰࡱ࠭ⅲ")
        os.environ[bstack1l1lll1_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡎࡕࡃࡡࡍ࡛࡙࠭ⅳ")] = bstack1l1lll1_opy_ (u"ࠪࡲࡺࡲ࡬ࠨⅴ")
        os.environ[bstack1l1lll1_opy_ (u"ࠫࡇ࡙࡟ࡕࡇࡖࡘࡔࡖࡓࡠࡄࡘࡍࡑࡊ࡟ࡄࡑࡐࡔࡑࡋࡔࡆࡆࠪⅵ")] = bstack1l1lll1_opy_ (u"ࠬ࡬ࡡ࡭ࡵࡨࠫⅶ")
        os.environ[bstack1l1lll1_opy_ (u"࠭ࡂࡔࡡࡗࡉࡘ࡚ࡏࡑࡕࡢࡆ࡚ࡏࡌࡅࡡࡋࡅࡘࡎࡅࡅࡡࡌࡈࠬⅷ")] = bstack1l1lll1_opy_ (u"ࠢ࡯ࡷ࡯ࡰࠧⅸ")
        os.environ[bstack1l1lll1_opy_ (u"ࠨࡄࡖࡣ࡙ࡋࡓࡕࡑࡓࡗࡤࡇࡌࡍࡑ࡚ࡣࡘࡉࡒࡆࡇࡑࡗࡍࡕࡔࡔࠩⅹ")] = bstack1l1lll1_opy_ (u"ࠤࡱࡹࡱࡲࠢⅺ")
        cls.bstack1llll11ll1ll_opy_(response, bstack1l1lll1_opy_ (u"ࠥࡳࡧࡹࡥࡳࡸࡤࡦ࡮ࡲࡩࡵࡻࠥⅻ"))
        return [None, None, None]
    @classmethod
    def bstack1llll11ll111_opy_(cls, response=None):
        os.environ[bstack1l1lll1_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡉࡗࡅࡣ࡚࡛ࡉࡅࠩⅼ")] = bstack1l1lll1_opy_ (u"ࠬࡴࡵ࡭࡮ࠪⅽ")
        os.environ[bstack1l1lll1_opy_ (u"࠭ࡂࡔࡡࡄ࠵࠶࡟࡟ࡋ࡙ࡗࠫⅾ")] = bstack1l1lll1_opy_ (u"ࠧ࡯ࡷ࡯ࡰࠬⅿ")
        os.environ[bstack1l1lll1_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡍ࡛ࡂࡠࡌ࡚ࡘࠬↀ")] = bstack1l1lll1_opy_ (u"ࠩࡱࡹࡱࡲࠧↁ")
        cls.bstack1llll11ll1ll_opy_(response, bstack1l1lll1_opy_ (u"ࠥࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠥↂ"))
        return [None, None, None]
    @classmethod
    def bstack1llll1l111ll_opy_(cls, jwt, build_hashed_id):
        os.environ[bstack1l1lll1_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡉࡗࡅࡣࡏ࡝ࡔࠨↃ")] = jwt
        os.environ[bstack1l1lll1_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡊࡘࡆࡤ࡛ࡕࡊࡆࠪↄ")] = build_hashed_id
    @classmethod
    def bstack1llll11ll1ll_opy_(cls, response=None, product=bstack1l1lll1_opy_ (u"ࠨࠢↅ")):
        if response == None or response.get(bstack1l1lll1_opy_ (u"ࠧࡦࡴࡵࡳࡷࡹࠧↆ")) == None:
            logger.error(product + bstack1l1lll1_opy_ (u"ࠣࠢࡅࡹ࡮ࡲࡤࠡࡥࡵࡩࡦࡺࡩࡰࡰࠣࡪࡦ࡯࡬ࡦࡦࠥↇ"))
            return
        for error in response[bstack1l1lll1_opy_ (u"ࠩࡨࡶࡷࡵࡲࡴࠩↈ")]:
            bstack111l1l1llll_opy_ = error[bstack1l1lll1_opy_ (u"ࠪ࡯ࡪࡿࠧ↉")]
            error_message = error[bstack1l1lll1_opy_ (u"ࠫࡲ࡫ࡳࡴࡣࡪࡩࠬ↊")]
            if error_message:
                if bstack111l1l1llll_opy_ == bstack1l1lll1_opy_ (u"ࠧࡋࡒࡓࡑࡕࡣࡆࡉࡃࡆࡕࡖࡣࡉࡋࡎࡊࡇࡇࠦ↋"):
                    logger.info(error_message)
                else:
                    logger.error(error_message)
            else:
                logger.error(bstack1l1lll1_opy_ (u"ࠨࡄࡢࡶࡤࠤࡺࡶ࡬ࡰࡣࡧࠤࡹࡵࠠࡃࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࠦࠢ↌") + product + bstack1l1lll1_opy_ (u"ࠢࠡࡨࡤ࡭ࡱ࡫ࡤࠡࡦࡸࡩࠥࡺ࡯ࠡࡵࡲࡱࡪࠦࡥࡳࡴࡲࡶࠧ↍"))
    @classmethod
    def bstack1llll1l1l111_opy_(cls):
        if cls.bstack11l11l1l111_opy_ is not None:
            return
        cls.bstack11l11l1l111_opy_ = bstack111ll111l11_opy_(cls.post_data)
        cls.bstack11l11l1l111_opy_.start()
    @classmethod
    def bstack1ll11lll_opy_(cls):
        if cls.bstack11l11l1l111_opy_ is None:
            return
        cls.bstack11l11l1l111_opy_.shutdown()
    @classmethod
    @error_handler(class_method=True)
    def post_data(cls, bstack1l1l11ll_opy_, event_url=bstack1l1lll1_opy_ (u"ࠨࡣࡳ࡭࠴ࡼ࠱࠰ࡤࡤࡸࡨ࡮ࠧ↎")):
        config = {
            bstack1l1lll1_opy_ (u"ࠩ࡫ࡩࡦࡪࡥࡳࡵࠪ↏"): cls.default_headers()
        }
        logger.debug(bstack1l1lll1_opy_ (u"ࠥࡴࡴࡹࡴࡠࡦࡤࡸࡦࡀࠠࡔࡧࡱࡨ࡮ࡴࡧࠡࡦࡤࡸࡦࠦࡴࡰࠢࡷࡩࡸࡺࡨࡶࡤࠣࡪࡴࡸࠠࡦࡸࡨࡲࡹࡹࠠࡼࡿࠥ←").format(bstack1l1lll1_opy_ (u"ࠫ࠱ࠦࠧ↑").join([event[bstack1l1lll1_opy_ (u"ࠬ࡫ࡶࡦࡰࡷࡣࡹࡿࡰࡦࠩ→")] for event in bstack1l1l11ll_opy_])))
        response = bstack1l1l1l1l1l_opy_(bstack1l1lll1_opy_ (u"࠭ࡐࡐࡕࡗࠫ↓"), cls.request_url(event_url), bstack1l1l11ll_opy_, config)
        bstack1lllll11ll11_opy_ = response.json()
    @classmethod
    def bstack1lll1111_opy_(cls, bstack1l1l11ll_opy_, event_url=bstack1l1lll1_opy_ (u"ࠧࡢࡲ࡬࠳ࡻ࠷࠯ࡣࡣࡷࡧ࡭࠭↔")):
        logger.debug(bstack1l1lll1_opy_ (u"ࠣࡵࡨࡲࡩࡥࡤࡢࡶࡤ࠾ࠥࡇࡴࡵࡧࡰࡴࡹ࡯࡮ࡨࠢࡷࡳࠥࡧࡤࡥࠢࡧࡥࡹࡧࠠࡵࡱࠣࡦࡦࡺࡣࡩࠢࡺ࡭ࡹ࡮ࠠࡦࡸࡨࡲࡹࡥࡴࡺࡲࡨ࠾ࠥࢁࡽࠣ↕").format(bstack1l1l11ll_opy_[bstack1l1lll1_opy_ (u"ࠩࡨࡺࡪࡴࡴࡠࡶࡼࡴࡪ࠭↖")]))
        if not bstack1l1l1l1111_opy_.bstack1llll1l1l1ll_opy_(bstack1l1l11ll_opy_[bstack1l1lll1_opy_ (u"ࠪࡩࡻ࡫࡮ࡵࡡࡷࡽࡵ࡫ࠧ↗")]):
            logger.debug(bstack1l1lll1_opy_ (u"ࠦࡸ࡫࡮ࡥࡡࡧࡥࡹࡧ࠺ࠡࡐࡲࡸࠥࡧࡤࡥ࡫ࡱ࡫ࠥࡪࡡࡵࡣࠣࡻ࡮ࡺࡨࠡࡧࡹࡩࡳࡺ࡟ࡵࡻࡳࡩ࠿ࠦࡻࡾࠤ↘").format(bstack1l1l11ll_opy_[bstack1l1lll1_opy_ (u"ࠬ࡫ࡶࡦࡰࡷࡣࡹࡿࡰࡦࠩ↙")]))
            return
        bstack1ll11ll11l_opy_ = bstack1l1l1l1111_opy_.bstack1llll11llll1_opy_(bstack1l1l11ll_opy_[bstack1l1lll1_opy_ (u"࠭ࡥࡷࡧࡱࡸࡤࡺࡹࡱࡧࠪ↚")], bstack1l1l11ll_opy_.get(bstack1l1lll1_opy_ (u"ࠧࡵࡧࡶࡸࡤࡸࡵ࡯ࠩ↛")))
        if bstack1ll11ll11l_opy_ != None:
            if bstack1l1l11ll_opy_.get(bstack1l1lll1_opy_ (u"ࠨࡶࡨࡷࡹࡥࡲࡶࡰࠪ↜")) != None:
                bstack1l1l11ll_opy_[bstack1l1lll1_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡳࡷࡱࠫ↝")][bstack1l1lll1_opy_ (u"ࠪࡴࡷࡵࡤࡶࡥࡷࡣࡲࡧࡰࠨ↞")] = bstack1ll11ll11l_opy_
            else:
                bstack1l1l11ll_opy_[bstack1l1lll1_opy_ (u"ࠫࡵࡸ࡯ࡥࡷࡦࡸࡤࡳࡡࡱࠩ↟")] = bstack1ll11ll11l_opy_
        if event_url == bstack1l1lll1_opy_ (u"ࠬࡧࡰࡪ࠱ࡹ࠵࠴ࡨࡡࡵࡥ࡫ࠫ↠"):
            cls.bstack1llll1l1l111_opy_()
            logger.debug(bstack1l1lll1_opy_ (u"ࠨࡳࡦࡰࡧࡣࡩࡧࡴࡢ࠼ࠣࡅࡩࡪࡩ࡯ࡩࠣࡨࡦࡺࡡࠡࡶࡲࠤࡧࡧࡴࡤࡪࠣࡻ࡮ࡺࡨࠡࡧࡹࡩࡳࡺ࡟ࡵࡻࡳࡩ࠿ࠦࡻࡾࠤ↡").format(bstack1l1l11ll_opy_[bstack1l1lll1_opy_ (u"ࠧࡦࡸࡨࡲࡹࡥࡴࡺࡲࡨࠫ↢")]))
            cls.bstack11l11l1l111_opy_.add(bstack1l1l11ll_opy_)
        elif event_url == bstack1l1lll1_opy_ (u"ࠨࡣࡳ࡭࠴ࡼ࠱࠰ࡵࡦࡶࡪ࡫࡮ࡴࡪࡲࡸࡸ࠭↣"):
            cls.post_data([bstack1l1l11ll_opy_], event_url)
    @classmethod
    @error_handler(class_method=True)
    def bstack1l1l1111_opy_(cls, logs):
        for log in logs:
            bstack1llll1l11111_opy_ = {
                bstack1l1lll1_opy_ (u"ࠩ࡮࡭ࡳࡪࠧ↤"): bstack1l1lll1_opy_ (u"ࠪࡘࡊ࡙ࡔࡠࡎࡒࡋࠬ↥"),
                bstack1l1lll1_opy_ (u"ࠫࡱ࡫ࡶࡦ࡮ࠪ↦"): log[bstack1l1lll1_opy_ (u"ࠬࡲࡥࡷࡧ࡯ࠫ↧")],
                bstack1l1lll1_opy_ (u"࠭ࡴࡪ࡯ࡨࡷࡹࡧ࡭ࡱࠩ↨"): log[bstack1l1lll1_opy_ (u"ࠧࡵ࡫ࡰࡩࡸࡺࡡ࡮ࡲࠪ↩")],
                bstack1l1lll1_opy_ (u"ࠨࡪࡷࡸࡵࡥࡲࡦࡵࡳࡳࡳࡹࡥࠨ↪"): {},
                bstack1l1lll1_opy_ (u"ࠩࡰࡩࡸࡹࡡࡨࡧࠪ↫"): log[bstack1l1lll1_opy_ (u"ࠪࡱࡪࡹࡳࡢࡩࡨࠫ↬")],
            }
            if bstack1l1lll1_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠫ↭") in log:
                bstack1llll1l11111_opy_[bstack1l1lll1_opy_ (u"ࠬࡺࡥࡴࡶࡢࡶࡺࡴ࡟ࡶࡷ࡬ࡨࠬ↮")] = log[bstack1l1lll1_opy_ (u"࠭ࡴࡦࡵࡷࡣࡷࡻ࡮ࡠࡷࡸ࡭ࡩ࠭↯")]
            elif bstack1l1lll1_opy_ (u"ࠧࡩࡱࡲ࡯ࡤࡸࡵ࡯ࡡࡸࡹ࡮ࡪࠧ↰") in log:
                bstack1llll1l11111_opy_[bstack1l1lll1_opy_ (u"ࠨࡪࡲࡳࡰࡥࡲࡶࡰࡢࡹࡺ࡯ࡤࠨ↱")] = log[bstack1l1lll1_opy_ (u"ࠩ࡫ࡳࡴࡱ࡟ࡳࡷࡱࡣࡺࡻࡩࡥࠩ↲")]
            cls.bstack1lll1111_opy_({
                bstack1l1lll1_opy_ (u"ࠪࡩࡻ࡫࡮ࡵࡡࡷࡽࡵ࡫ࠧ↳"): bstack1l1lll1_opy_ (u"ࠫࡑࡵࡧࡄࡴࡨࡥࡹ࡫ࡤࠨ↴"),
                bstack1l1lll1_opy_ (u"ࠬࡲ࡯ࡨࡵࠪ↵"): [bstack1llll1l11111_opy_]
            })
    @classmethod
    @error_handler(class_method=True)
    def bstack1llll11ll11l_opy_(cls, steps):
        bstack1llll11lll11_opy_ = []
        for step in steps:
            bstack1llll11lllll_opy_ = {
                bstack1l1lll1_opy_ (u"࠭࡫ࡪࡰࡧࠫ↶"): bstack1l1lll1_opy_ (u"ࠧࡕࡇࡖࡘࡤ࡙ࡔࡆࡒࠪ↷"),
                bstack1l1lll1_opy_ (u"ࠨ࡮ࡨࡺࡪࡲࠧ↸"): step[bstack1l1lll1_opy_ (u"ࠩ࡯ࡩࡻ࡫࡬ࠨ↹")],
                bstack1l1lll1_opy_ (u"ࠪࡸ࡮ࡳࡥࡴࡶࡤࡱࡵ࠭↺"): step[bstack1l1lll1_opy_ (u"ࠫࡹ࡯࡭ࡦࡵࡷࡥࡲࡶࠧ↻")],
                bstack1l1lll1_opy_ (u"ࠬࡳࡥࡴࡵࡤ࡫ࡪ࠭↼"): step[bstack1l1lll1_opy_ (u"࠭࡭ࡦࡵࡶࡥ࡬࡫ࠧ↽")],
                bstack1l1lll1_opy_ (u"ࠧࡥࡷࡵࡥࡹ࡯࡯࡯ࠩ↾"): step[bstack1l1lll1_opy_ (u"ࠨࡦࡸࡶࡦࡺࡩࡰࡰࠪ↿")]
            }
            if bstack1l1lll1_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡳࡷࡱࡣࡺࡻࡩࡥࠩ⇀") in step:
                bstack1llll11lllll_opy_[bstack1l1lll1_opy_ (u"ࠪࡸࡪࡹࡴࡠࡴࡸࡲࡤࡻࡵࡪࡦࠪ⇁")] = step[bstack1l1lll1_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠫ⇂")]
            elif bstack1l1lll1_opy_ (u"ࠬ࡮࡯ࡰ࡭ࡢࡶࡺࡴ࡟ࡶࡷ࡬ࡨࠬ⇃") in step:
                bstack1llll11lllll_opy_[bstack1l1lll1_opy_ (u"࠭ࡨࡰࡱ࡮ࡣࡷࡻ࡮ࡠࡷࡸ࡭ࡩ࠭⇄")] = step[bstack1l1lll1_opy_ (u"ࠧࡩࡱࡲ࡯ࡤࡸࡵ࡯ࡡࡸࡹ࡮ࡪࠧ⇅")]
            bstack1llll11lll11_opy_.append(bstack1llll11lllll_opy_)
        cls.bstack1lll1111_opy_({
            bstack1l1lll1_opy_ (u"ࠨࡧࡹࡩࡳࡺ࡟ࡵࡻࡳࡩࠬ⇆"): bstack1l1lll1_opy_ (u"ࠩࡏࡳ࡬ࡉࡲࡦࡣࡷࡩࡩ࠭⇇"),
            bstack1l1lll1_opy_ (u"ࠪࡰࡴ࡭ࡳࠨ⇈"): bstack1llll11lll11_opy_
        })
    @classmethod
    @error_handler(class_method=True)
    @measure(event_name=EVENTS.bstack1l111l1ll_opy_, stage=STAGE.bstack1111llll1l_opy_)
    def bstack1l111ll11_opy_(cls, screenshot):
        cls.bstack1lll1111_opy_({
            bstack1l1lll1_opy_ (u"ࠫࡪࡼࡥ࡯ࡶࡢࡸࡾࡶࡥࠨ⇉"): bstack1l1lll1_opy_ (u"ࠬࡒ࡯ࡨࡅࡵࡩࡦࡺࡥࡥࠩ⇊"),
            bstack1l1lll1_opy_ (u"࠭࡬ࡰࡩࡶࠫ⇋"): [{
                bstack1l1lll1_opy_ (u"ࠧ࡬࡫ࡱࡨࠬ⇌"): bstack1l1lll1_opy_ (u"ࠨࡖࡈࡗ࡙ࡥࡓࡄࡔࡈࡉࡓ࡙ࡈࡐࡖࠪ⇍"),
                bstack1l1lll1_opy_ (u"ࠩࡷ࡭ࡲ࡫ࡳࡵࡣࡰࡴࠬ⇎"): datetime.datetime.utcnow().isoformat() + bstack1l1lll1_opy_ (u"ࠪ࡞ࠬ⇏"),
                bstack1l1lll1_opy_ (u"ࠫࡲ࡫ࡳࡴࡣࡪࡩࠬ⇐"): screenshot[bstack1l1lll1_opy_ (u"ࠬ࡯࡭ࡢࡩࡨࠫ⇑")],
                bstack1l1lll1_opy_ (u"࠭ࡴࡦࡵࡷࡣࡷࡻ࡮ࡠࡷࡸ࡭ࡩ࠭⇒"): screenshot[bstack1l1lll1_opy_ (u"ࠧࡵࡧࡶࡸࡤࡸࡵ࡯ࡡࡸࡹ࡮ࡪࠧ⇓")]
            }]
        }, event_url=bstack1l1lll1_opy_ (u"ࠨࡣࡳ࡭࠴ࡼ࠱࠰ࡵࡦࡶࡪ࡫࡮ࡴࡪࡲࡸࡸ࠭⇔"))
    @classmethod
    @error_handler(class_method=True)
    def bstack111l111l1_opy_(cls, driver):
        current_test_uuid = cls.current_test_uuid()
        if not current_test_uuid:
            return
        cls.bstack1lll1111_opy_({
            bstack1l1lll1_opy_ (u"ࠩࡨࡺࡪࡴࡴࡠࡶࡼࡴࡪ࠭⇕"): bstack1l1lll1_opy_ (u"ࠪࡇࡇ࡚ࡓࡦࡵࡶ࡭ࡴࡴࡃࡳࡧࡤࡸࡪࡪࠧ⇖"),
            bstack1l1lll1_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡵࡹࡳ࠭⇗"): {
                bstack1l1lll1_opy_ (u"ࠧࡻࡵࡪࡦࠥ⇘"): cls.current_test_uuid(),
                bstack1l1lll1_opy_ (u"ࠨࡩ࡯ࡶࡨ࡫ࡷࡧࡴࡪࡱࡱࡷࠧ⇙"): cls.bstack1l111ll1_opy_(driver)
            }
        })
    @classmethod
    def bstack1l1lllll_opy_(cls, event: str, bstack1l1l11ll_opy_: bstack1ll1l1l1_opy_):
        bstack1l1ll111_opy_ = {
            bstack1l1lll1_opy_ (u"ࠧࡦࡸࡨࡲࡹࡥࡴࡺࡲࡨࠫ⇚"): event,
            bstack1l1l11ll_opy_.event_key(): bstack1l1l11ll_opy_.bstack1l1lll11_opy_(event)
        }
        cls.bstack1lll1111_opy_(bstack1l1ll111_opy_)
        result = getattr(bstack1l1l11ll_opy_, bstack1l1lll1_opy_ (u"ࠨࡴࡨࡷࡺࡲࡴࠨ⇛"), None)
        if event == bstack1l1lll1_opy_ (u"ࠩࡗࡩࡸࡺࡒࡶࡰࡖࡸࡦࡸࡴࡦࡦࠪ⇜"):
            threading.current_thread().bstackTestMeta = {bstack1l1lll1_opy_ (u"ࠪࡷࡹࡧࡴࡶࡵࠪ⇝"): bstack1l1lll1_opy_ (u"ࠫࡵ࡫࡮ࡥ࡫ࡱ࡫ࠬ⇞")}
        elif event == bstack1l1lll1_opy_ (u"࡚ࠬࡥࡴࡶࡕࡹࡳࡌࡩ࡯࡫ࡶ࡬ࡪࡪࠧ⇟"):
            threading.current_thread().bstackTestMeta = {bstack1l1lll1_opy_ (u"࠭ࡳࡵࡣࡷࡹࡸ࠭⇠"): getattr(result, bstack1l1lll1_opy_ (u"ࠧࡳࡧࡶࡹࡱࡺࠧ⇡"), bstack1l1lll1_opy_ (u"ࠨࠩ⇢"))}
    @classmethod
    def on(cls):
        if (os.environ.get(bstack1l1lll1_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡎࡕࡃࡡࡍ࡛࡙࠭⇣"), None) is None or os.environ[bstack1l1lll1_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚ࡈࡖࡄࡢࡎ࡜࡚ࠧ⇤")] == bstack1l1lll1_opy_ (u"ࠦࡳࡻ࡬࡭ࠤ⇥")) and (os.environ.get(bstack1l1lll1_opy_ (u"ࠬࡈࡓࡠࡃ࠴࠵࡞ࡥࡊࡘࡖࠪ⇦"), None) is None or os.environ[bstack1l1lll1_opy_ (u"࠭ࡂࡔࡡࡄ࠵࠶࡟࡟ࡋ࡙ࡗࠫ⇧")] == bstack1l1lll1_opy_ (u"ࠢ࡯ࡷ࡯ࡰࠧ⇨")):
            return False
        return True
    @staticmethod
    def bstack1llll1l1lll1_opy_(func):
        def wrap(*args, **kwargs):
            if bstack1l11ll1l_opy_.on():
                return func(*args, **kwargs)
            return
        return wrap
    @staticmethod
    def default_headers():
        headers = {
            bstack1l1lll1_opy_ (u"ࠨࡅࡲࡲࡹ࡫࡮ࡵ࠯ࡗࡽࡵ࡫ࠧ⇩"): bstack1l1lll1_opy_ (u"ࠩࡤࡴࡵࡲࡩࡤࡣࡷ࡭ࡴࡴ࠯࡫ࡵࡲࡲࠬ⇪"),
            bstack1l1lll1_opy_ (u"ࠪ࡜࠲ࡈࡓࡕࡃࡆࡏ࠲࡚ࡅࡔࡖࡒࡔࡘ࠭⇫"): bstack1l1lll1_opy_ (u"ࠫࡹࡸࡵࡦࠩ⇬")
        }
        if os.environ.get(bstack1l1lll1_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡊࡘࡆࡤࡐࡗࡕࠩ⇭"), None):
            headers[bstack1l1lll1_opy_ (u"࠭ࡁࡶࡶ࡫ࡳࡷ࡯ࡺࡢࡶ࡬ࡳࡳ࠭⇮")] = bstack1l1lll1_opy_ (u"ࠧࡃࡧࡤࡶࡪࡸࠠࡼࡿࠪ⇯").format(os.environ[bstack1l1lll1_opy_ (u"ࠣࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡍ࡛ࡂࡠࡌ࡚ࡘࠧ⇰")])
        return headers
    @staticmethod
    def request_url(url):
        return bstack1l1lll1_opy_ (u"ࠩࡾࢁ࠴ࢁࡽࠨ⇱").format(bstack1llll1l11l11_opy_, url)
    @staticmethod
    def current_test_uuid():
        return getattr(threading.current_thread(), bstack1l1lll1_opy_ (u"ࠪࡧࡺࡸࡲࡦࡰࡷࡣࡹ࡫ࡳࡵࡡࡸࡹ࡮ࡪࠧ⇲"), None)
    @staticmethod
    def bstack1l111ll1_opy_(driver):
        return {
            bstack111l1l11l11_opy_(): bstack111l1lll1ll_opy_(driver)
        }
    @staticmethod
    def bstack1llll11ll1l1_opy_(exception_info, report):
        return [{bstack1l1lll1_opy_ (u"ࠫࡧࡧࡣ࡬ࡶࡵࡥࡨ࡫ࠧ⇳"): [exception_info.exconly(), report.longreprtext]}]
    @staticmethod
    def bstack11111l1111_opy_(typename):
        if bstack1l1lll1_opy_ (u"ࠧࡇࡳࡴࡧࡵࡸ࡮ࡵ࡮ࠣ⇴") in typename:
            return bstack1l1lll1_opy_ (u"ࠨࡁࡴࡵࡨࡶࡹ࡯࡯࡯ࡇࡵࡶࡴࡸࠢ⇵")
        return bstack1l1lll1_opy_ (u"ࠢࡖࡰ࡫ࡥࡳࡪ࡬ࡦࡦࡈࡶࡷࡵࡲࠣ⇶")