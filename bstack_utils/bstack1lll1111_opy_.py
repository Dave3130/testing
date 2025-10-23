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
import json
import logging
import os
import datetime
import threading
from bstack_utils.constants import EVENTS, STAGE
from bstack_utils.helper import bstack1111ll1lll1_opy_, bstack111l1l1111l_opy_, bstack1l11l1ll1l_opy_, error_handler, bstack111l1111l1l_opy_, bstack111l1l1ll11_opy_, bstack111l1111ll1_opy_, bstack1llll1ll_opy_, bstack1lll111l_opy_
from bstack_utils.measure import measure
from bstack_utils.bstack11l11l1l1ll_opy_ import bstack111ll111lll_opy_
import bstack_utils.bstack11ll111l1l_opy_ as bstack1l1l1l1l1_opy_
from bstack_utils.bstack1l1111l1_opy_ import bstack1ll1l1ll_opy_
import bstack_utils.accessibility as bstack1llll111l_opy_
from bstack_utils.bstack11l1llll11_opy_ import bstack11l1llll11_opy_
from bstack_utils.bstack1l11ll11_opy_ import bstack11lll1l1_opy_
from bstack_utils.constants import bstack11ll1ll1l1_opy_
bstack1llll1l11l1l_opy_ = bstack111111l_opy_ (u"࠭ࡨࡵࡶࡳࡷ࠿࠵࠯ࡤࡱ࡯ࡰࡪࡩࡴࡰࡴ࠰ࡳࡧࡹࡥࡳࡸࡤࡦ࡮ࡲࡩࡵࡻ࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡦࡳࡲ࠭⃲")
logger = logging.getLogger(__name__)
class bstack1ll1l111_opy_:
    bstack11l11l1l1ll_opy_ = None
    bs_config = None
    bstack11l1lll11_opy_ = None
    @classmethod
    @error_handler(class_method=True)
    @measure(event_name=EVENTS.bstack11l1l11l111_opy_, stage=STAGE.bstack11l11ll11_opy_)
    def launch(cls, bs_config, bstack11l1lll11_opy_):
        cls.bs_config = bs_config
        cls.bstack11l1lll11_opy_ = bstack11l1lll11_opy_
        try:
            cls.bstack1llll1l1llll_opy_()
            bstack1llll1llllll_opy_ = bstack1111ll1lll1_opy_(bs_config)
            bstack1lllll11111l_opy_ = bstack111l1l1111l_opy_(bs_config)
            data = bstack1l1l1l1l1_opy_.bstack1llll1l1ll1l_opy_(bs_config, bstack11l1lll11_opy_)
            config = {
                bstack111111l_opy_ (u"ࠧࡢࡷࡷ࡬ࠬ⃳"): (bstack1llll1llllll_opy_, bstack1lllll11111l_opy_),
                bstack111111l_opy_ (u"ࠨࡪࡨࡥࡩ࡫ࡲࡴࠩ⃴"): cls.default_headers()
            }
            response = bstack1l11l1ll1l_opy_(bstack111111l_opy_ (u"ࠩࡓࡓࡘ࡚ࠧ⃵"), cls.request_url(bstack111111l_opy_ (u"ࠪࡥࡵ࡯࠯ࡷ࠴࠲ࡦࡺ࡯࡬ࡥࡵࠪ⃶")), data, config)
            if response.status_code != 200:
                bstack111ll1111_opy_ = response.json()
                if bstack111ll1111_opy_[bstack111111l_opy_ (u"ࠫࡸࡻࡣࡤࡧࡶࡷࠬ⃷")] == False:
                    cls.bstack1llll1l111ll_opy_(bstack111ll1111_opy_)
                    return
                cls.bstack1llll11lll1l_opy_(bstack111ll1111_opy_[bstack111111l_opy_ (u"ࠬࡵࡢࡴࡧࡵࡺࡦࡨࡩ࡭࡫ࡷࡽࠬ⃸")])
                cls.bstack1llll1l1l11l_opy_(bstack111ll1111_opy_[bstack111111l_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾ࠭⃹")])
                return None
            bstack1llll11ll1l1_opy_ = cls.bstack1llll1l1l111_opy_(response)
            return bstack1llll11ll1l1_opy_, response.json()
        except Exception as error:
            logger.error(bstack111111l_opy_ (u"ࠢࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣࡻ࡭࡯࡬ࡦࠢࡦࡶࡪࡧࡴࡪࡰࡪࠤࡧࡻࡩ࡭ࡦࠣࡪࡴࡸࠠࡕࡧࡶࡸࡍࡻࡢ࠻ࠢࡾࢁࠧ⃺").format(str(error)))
            return None
    @classmethod
    @error_handler(class_method=True)
    def stop(cls, bstack1llll1ll111l_opy_=None):
        if not bstack1ll1l1ll_opy_.on() and not bstack1llll111l_opy_.on():
            return
        if os.environ.get(bstack111111l_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡍ࡛ࡂࡠࡌ࡚ࡘࠬ⃻")) == bstack111111l_opy_ (u"ࠤࡱࡹࡱࡲࠢ⃼") or os.environ.get(bstack111111l_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚ࡈࡖࡄࡢ࡙࡚ࡏࡄࠨ⃽")) == bstack111111l_opy_ (u"ࠦࡳࡻ࡬࡭ࠤ⃾"):
            logger.error(bstack111111l_opy_ (u"ࠬࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡ࡫ࡱࠤࡸࡺ࡯ࡱࠢࡥࡹ࡮ࡲࡤࠡࡴࡨࡵࡺ࡫ࡳࡵࠢࡷࡳ࡚ࠥࡥࡴࡶࡋࡹࡧࡀࠠࡎ࡫ࡶࡷ࡮ࡴࡧࠡࡣࡸࡸ࡭࡫࡮ࡵ࡫ࡦࡥࡹ࡯࡯࡯ࠢࡷࡳࡰ࡫࡮ࠨ⃿"))
            return {
                bstack111111l_opy_ (u"࠭ࡳࡵࡣࡷࡹࡸ࠭℀"): bstack111111l_opy_ (u"ࠧࡦࡴࡵࡳࡷ࠭℁"),
                bstack111111l_opy_ (u"ࠨ࡯ࡨࡷࡸࡧࡧࡦࠩℂ"): bstack111111l_opy_ (u"ࠩࡗࡳࡰ࡫࡮࠰ࡤࡸ࡭ࡱࡪࡉࡅࠢ࡬ࡷࠥࡻ࡮ࡥࡧࡩ࡭ࡳ࡫ࡤ࠭ࠢࡥࡹ࡮ࡲࡤࠡࡥࡵࡩࡦࡺࡩࡰࡰࠣࡱ࡮࡭ࡨࡵࠢ࡫ࡥࡻ࡫ࠠࡧࡣ࡬ࡰࡪࡪࠧ℃")
            }
        try:
            cls.bstack11l11l1l1ll_opy_.shutdown()
            data = {
                bstack111111l_opy_ (u"ࠪࡪ࡮ࡴࡩࡴࡪࡨࡨࡤࡧࡴࠨ℄"): bstack1llll1ll_opy_()
            }
            if not bstack1llll1ll111l_opy_ is None:
                data[bstack111111l_opy_ (u"ࠫ࡫࡯࡮ࡪࡵ࡫ࡩࡩࡥ࡭ࡦࡶࡤࡨࡦࡺࡡࠨ℅")] = [{
                    bstack111111l_opy_ (u"ࠬࡸࡥࡢࡵࡲࡲࠬ℆"): bstack111111l_opy_ (u"࠭ࡵࡴࡧࡵࡣࡰ࡯࡬࡭ࡧࡧࠫℇ"),
                    bstack111111l_opy_ (u"ࠧࡴ࡫ࡪࡲࡦࡲࠧ℈"): bstack1llll1ll111l_opy_
                }]
            config = {
                bstack111111l_opy_ (u"ࠨࡪࡨࡥࡩ࡫ࡲࡴࠩ℉"): cls.default_headers()
            }
            bstack11ll11ll111_opy_ = bstack111111l_opy_ (u"ࠩࡤࡴ࡮࠵ࡶ࠲࠱ࡥࡹ࡮ࡲࡤࡴ࠱ࡾࢁ࠴ࡹࡴࡰࡲࠪℊ").format(os.environ[bstack111111l_opy_ (u"ࠥࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚ࡈࡖࡄࡢ࡙࡚ࡏࡄࠣℋ")])
            bstack1llll1l1ll11_opy_ = cls.request_url(bstack11ll11ll111_opy_)
            response = bstack1l11l1ll1l_opy_(bstack111111l_opy_ (u"ࠫࡕ࡛ࡔࠨℌ"), bstack1llll1l1ll11_opy_, data, config)
            if not response.ok:
                raise Exception(bstack111111l_opy_ (u"࡙ࠧࡴࡰࡲࠣࡶࡪࡷࡵࡦࡵࡷࠤࡳࡵࡴࠡࡱ࡮ࠦℍ"))
        except Exception as error:
            logger.error(bstack111111l_opy_ (u"ࠨࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥࡹࡴࡰࡲࠣࡦࡺ࡯࡬ࡥࠢࡵࡩࡶࡻࡥࡴࡶࠣࡸࡴࠦࡔࡦࡵࡷࡌࡺࡨ࠺࠻ࠢࠥℎ") + str(error))
            return {
                bstack111111l_opy_ (u"ࠧࡴࡶࡤࡸࡺࡹࠧℏ"): bstack111111l_opy_ (u"ࠨࡧࡵࡶࡴࡸࠧℐ"),
                bstack111111l_opy_ (u"ࠩࡰࡩࡸࡹࡡࡨࡧࠪℑ"): str(error)
            }
    @classmethod
    @error_handler(class_method=True)
    def bstack1llll1l1l111_opy_(cls, response):
        bstack111ll1111_opy_ = response.json() if not isinstance(response, dict) else response
        bstack1llll11ll1l1_opy_ = {}
        if bstack111ll1111_opy_.get(bstack111111l_opy_ (u"ࠪ࡮ࡼࡺࠧℒ")) is None:
            os.environ[bstack111111l_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡉࡗࡅࡣࡏ࡝ࡔࠨℓ")] = bstack111111l_opy_ (u"ࠬࡴࡵ࡭࡮ࠪ℔")
        else:
            os.environ[bstack111111l_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡊࡘࡖࠪℕ")] = bstack111ll1111_opy_.get(bstack111111l_opy_ (u"ࠧ࡫ࡹࡷࠫ№"), bstack111111l_opy_ (u"ࠨࡰࡸࡰࡱ࠭℗"))
        os.environ[bstack111111l_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡎࡕࡃࡡࡘ࡙ࡎࡊࠧ℘")] = bstack111ll1111_opy_.get(bstack111111l_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡡ࡫ࡥࡸ࡮ࡥࡥࡡ࡬ࡨࠬℙ"), bstack111111l_opy_ (u"ࠫࡳࡻ࡬࡭ࠩℚ"))
        logger.info(bstack111111l_opy_ (u"࡚ࠬࡥࡴࡶ࡫ࡹࡧࠦࡳࡵࡣࡵࡸࡪࡪࠠࡸ࡫ࡷ࡬ࠥ࡯ࡤ࠻ࠢࠪℛ") + os.getenv(bstack111111l_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡕࡖࡋࡇࠫℜ")));
        if bstack1ll1l1ll_opy_.bstack11l11l1l1l1_opy_(cls.bs_config, cls.bstack11l1lll11_opy_.get(bstack111111l_opy_ (u"ࠧࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡹࡸ࡫ࡤࠨℝ"), bstack111111l_opy_ (u"ࠨࠩ℞"))) is True:
            bstack11ll11l11ll_opy_, build_hashed_id, bstack1llll1l11111_opy_ = cls.bstack1llll1l1l1ll_opy_(bstack111ll1111_opy_)
            if bstack11ll11l11ll_opy_ != None and build_hashed_id != None:
                bstack1llll11ll1l1_opy_[bstack111111l_opy_ (u"ࠩࡲࡦࡸ࡫ࡲࡷࡣࡥ࡭ࡱ࡯ࡴࡺࠩ℟")] = {
                    bstack111111l_opy_ (u"ࠪ࡮ࡼࡺ࡟ࡵࡱ࡮ࡩࡳ࠭℠"): bstack11ll11l11ll_opy_,
                    bstack111111l_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡢ࡬ࡦࡹࡨࡦࡦࡢ࡭ࡩ࠭℡"): build_hashed_id,
                    bstack111111l_opy_ (u"ࠬࡧ࡬࡭ࡱࡺࡣࡸࡩࡲࡦࡧࡱࡷ࡭ࡵࡴࡴࠩ™"): bstack1llll1l11111_opy_
                }
            else:
                bstack1llll11ll1l1_opy_[bstack111111l_opy_ (u"࠭࡯ࡣࡵࡨࡶࡻࡧࡢࡪ࡮࡬ࡸࡾ࠭℣")] = {}
        else:
            bstack1llll11ll1l1_opy_[bstack111111l_opy_ (u"ࠧࡰࡤࡶࡩࡷࡼࡡࡣ࡫࡯࡭ࡹࡿࠧℤ")] = {}
        bstack1llll11ll1ll_opy_, build_hashed_id = cls.bstack1llll1l1lll1_opy_(bstack111ll1111_opy_)
        if bstack1llll11ll1ll_opy_ != None and build_hashed_id != None:
            bstack1llll11ll1l1_opy_[bstack111111l_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠨ℥")] = {
                bstack111111l_opy_ (u"ࠩࡤࡹࡹ࡮࡟ࡵࡱ࡮ࡩࡳ࠭Ω"): bstack1llll11ll1ll_opy_,
                bstack111111l_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡡ࡫ࡥࡸ࡮ࡥࡥࡡ࡬ࡨࠬ℧"): build_hashed_id,
            }
        else:
            bstack1llll11ll1l1_opy_[bstack111111l_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠫℨ")] = {}
        if bstack1llll11ll1l1_opy_[bstack111111l_opy_ (u"ࠬࡵࡢࡴࡧࡵࡺࡦࡨࡩ࡭࡫ࡷࡽࠬ℩")].get(bstack111111l_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡤ࡮ࡡࡴࡪࡨࡨࡤ࡯ࡤࠨK")) != None or bstack1llll11ll1l1_opy_[bstack111111l_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠧÅ")].get(bstack111111l_opy_ (u"ࠨࡤࡸ࡭ࡱࡪ࡟ࡩࡣࡶ࡬ࡪࡪ࡟ࡪࡦࠪℬ")) != None:
            cls.bstack1llll11llll1_opy_(bstack111ll1111_opy_.get(bstack111111l_opy_ (u"ࠩ࡭ࡻࡹ࠭ℭ")), bstack111ll1111_opy_.get(bstack111111l_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡡ࡫ࡥࡸ࡮ࡥࡥࡡ࡬ࡨࠬ℮")))
        return bstack1llll11ll1l1_opy_
    @classmethod
    def bstack1llll1l1l1ll_opy_(cls, bstack111ll1111_opy_):
        if bstack111ll1111_opy_.get(bstack111111l_opy_ (u"ࠫࡴࡨࡳࡦࡴࡹࡥࡧ࡯࡬ࡪࡶࡼࠫℯ")) == None:
            cls.bstack1llll11lll1l_opy_()
            return [None, None, None]
        if bstack111ll1111_opy_[bstack111111l_opy_ (u"ࠬࡵࡢࡴࡧࡵࡺࡦࡨࡩ࡭࡫ࡷࡽࠬℰ")][bstack111111l_opy_ (u"࠭ࡳࡶࡥࡦࡩࡸࡹࠧℱ")] != True:
            cls.bstack1llll11lll1l_opy_(bstack111ll1111_opy_[bstack111111l_opy_ (u"ࠧࡰࡤࡶࡩࡷࡼࡡࡣ࡫࡯࡭ࡹࡿࠧℲ")])
            return [None, None, None]
        logger.debug(bstack111111l_opy_ (u"ࠨࡽࢀࠤࡇࡻࡩ࡭ࡦࠣࡧࡷ࡫ࡡࡵ࡫ࡲࡲ࡙ࠥࡵࡤࡥࡨࡷࡸ࡬ࡵ࡭ࠣࠪℳ").format(bstack11ll1ll1l1_opy_))
        os.environ[bstack111111l_opy_ (u"ࠩࡅࡗࡤ࡚ࡅࡔࡖࡒࡔࡘࡥࡂࡖࡋࡏࡈࡤࡉࡏࡎࡒࡏࡉ࡙ࡋࡄࠨℴ")] = bstack111111l_opy_ (u"ࠪࡸࡷࡻࡥࠨℵ")
        if bstack111ll1111_opy_.get(bstack111111l_opy_ (u"ࠫ࡯ࡽࡴࠨℶ")):
            os.environ[bstack111111l_opy_ (u"ࠬࡉࡒࡆࡆࡈࡒ࡙ࡏࡁࡍࡕࡢࡊࡔࡘ࡟ࡄࡔࡄࡗࡍࡥࡒࡆࡒࡒࡖ࡙ࡏࡎࡈࠩℷ")] = json.dumps({
                bstack111111l_opy_ (u"࠭ࡵࡴࡧࡵࡲࡦࡳࡥࠨℸ"): bstack1111ll1lll1_opy_(cls.bs_config),
                bstack111111l_opy_ (u"ࠧࡱࡣࡶࡷࡼࡵࡲࡥࠩℹ"): bstack111l1l1111l_opy_(cls.bs_config)
            })
        if bstack111ll1111_opy_.get(bstack111111l_opy_ (u"ࠨࡤࡸ࡭ࡱࡪ࡟ࡩࡣࡶ࡬ࡪࡪ࡟ࡪࡦࠪ℺")):
            os.environ[bstack111111l_opy_ (u"ࠩࡅࡗࡤ࡚ࡅࡔࡖࡒࡔࡘࡥࡂࡖࡋࡏࡈࡤࡎࡁࡔࡊࡈࡈࡤࡏࡄࠨ℻")] = bstack111ll1111_opy_[bstack111111l_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡡ࡫ࡥࡸ࡮ࡥࡥࡡ࡬ࡨࠬℼ")]
        if bstack111ll1111_opy_[bstack111111l_opy_ (u"ࠫࡴࡨࡳࡦࡴࡹࡥࡧ࡯࡬ࡪࡶࡼࠫℽ")].get(bstack111111l_opy_ (u"ࠬࡵࡰࡵ࡫ࡲࡲࡸ࠭ℾ"), {}).get(bstack111111l_opy_ (u"࠭ࡡ࡭࡮ࡲࡻࡤࡹࡣࡳࡧࡨࡲࡸ࡮࡯ࡵࡵࠪℿ")):
            os.environ[bstack111111l_opy_ (u"ࠧࡃࡕࡢࡘࡊ࡙ࡔࡐࡒࡖࡣࡆࡒࡌࡐ࡙ࡢࡗࡈࡘࡅࡆࡐࡖࡌࡔ࡚ࡓࠨ⅀")] = str(bstack111ll1111_opy_[bstack111111l_opy_ (u"ࠨࡱࡥࡷࡪࡸࡶࡢࡤ࡬ࡰ࡮ࡺࡹࠨ⅁")][bstack111111l_opy_ (u"ࠩࡲࡴࡹ࡯࡯࡯ࡵࠪ⅂")][bstack111111l_opy_ (u"ࠪࡥࡱࡲ࡯ࡸࡡࡶࡧࡷ࡫ࡥ࡯ࡵ࡫ࡳࡹࡹࠧ⅃")])
        else:
            os.environ[bstack111111l_opy_ (u"ࠫࡇ࡙࡟ࡕࡇࡖࡘࡔࡖࡓࡠࡃࡏࡐࡔ࡝࡟ࡔࡅࡕࡉࡊࡔࡓࡉࡑࡗࡗࠬ⅄")] = bstack111111l_opy_ (u"ࠧࡴࡵ࡭࡮ࠥⅅ")
        return [bstack111ll1111_opy_[bstack111111l_opy_ (u"࠭ࡪࡸࡶࠪⅆ")], bstack111ll1111_opy_[bstack111111l_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡥࡨࡢࡵ࡫ࡩࡩࡥࡩࡥࠩⅇ")], os.environ[bstack111111l_opy_ (u"ࠨࡄࡖࡣ࡙ࡋࡓࡕࡑࡓࡗࡤࡇࡌࡍࡑ࡚ࡣࡘࡉࡒࡆࡇࡑࡗࡍࡕࡔࡔࠩⅈ")]]
    @classmethod
    def bstack1llll1l1lll1_opy_(cls, bstack111ll1111_opy_):
        if bstack111ll1111_opy_.get(bstack111111l_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠩⅉ")) == None:
            cls.bstack1llll1l1l11l_opy_()
            return [None, None]
        if bstack111ll1111_opy_[bstack111111l_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠪ⅊")][bstack111111l_opy_ (u"ࠫࡸࡻࡣࡤࡧࡶࡷࠬ⅋")] != True:
            cls.bstack1llll1l1l11l_opy_(bstack111ll1111_opy_[bstack111111l_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠬ⅌")])
            return [None, None]
        if bstack111ll1111_opy_[bstack111111l_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾ࠭⅍")].get(bstack111111l_opy_ (u"ࠧࡰࡲࡷ࡭ࡴࡴࡳࠨⅎ")):
            logger.debug(bstack111111l_opy_ (u"ࠨࡖࡨࡷࡹࠦࡁࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡂࡶ࡫࡯ࡨࠥࡩࡲࡦࡣࡷ࡭ࡴࡴࠠࡔࡷࡦࡧࡪࡹࡳࡧࡷ࡯ࠥࠬ⅏"))
            parsed = json.loads(os.getenv(bstack111111l_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡥࡁࡄࡅࡈࡗࡘࡏࡂࡊࡎࡌࡘ࡞ࡥࡃࡐࡐࡉࡍࡌ࡛ࡒࡂࡖࡌࡓࡓࡥ࡙ࡎࡎࠪ⅐"), bstack111111l_opy_ (u"ࠪࡿࢂ࠭⅑")))
            capabilities = bstack1l1l1l1l1_opy_.bstack1llll1l11l11_opy_(bstack111ll1111_opy_[bstack111111l_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠫ⅒")][bstack111111l_opy_ (u"ࠬࡵࡰࡵ࡫ࡲࡲࡸ࠭⅓")][bstack111111l_opy_ (u"࠭ࡣࡢࡲࡤࡦ࡮ࡲࡩࡵ࡫ࡨࡷࠬ⅔")], bstack111111l_opy_ (u"ࠧ࡯ࡣࡰࡩࠬ⅕"), bstack111111l_opy_ (u"ࠨࡸࡤࡰࡺ࡫ࠧ⅖"))
            bstack1llll11ll1ll_opy_ = capabilities[bstack111111l_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࡖࡲ࡯ࡪࡴࠧ⅗")]
            os.environ[bstack111111l_opy_ (u"ࠪࡆࡘࡥࡁ࠲࠳࡜ࡣࡏ࡝ࡔࠨ⅘")] = bstack1llll11ll1ll_opy_
            if bstack111111l_opy_ (u"ࠦࡦࡻࡴࡰ࡯ࡤࡸࡪࠨ⅙") in bstack111ll1111_opy_ and bstack111ll1111_opy_.get(bstack111111l_opy_ (u"ࠧࡧࡰࡱࡡࡤࡹࡹࡵ࡭ࡢࡶࡨࠦ⅚")) is None:
                parsed[bstack111111l_opy_ (u"࠭ࡳࡤࡣࡱࡲࡪࡸࡖࡦࡴࡶ࡭ࡴࡴࠧ⅛")] = capabilities[bstack111111l_opy_ (u"ࠧࡴࡥࡤࡲࡳ࡫ࡲࡗࡧࡵࡷ࡮ࡵ࡮ࠨ⅜")]
            os.environ[bstack111111l_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡤࡇࡃࡄࡇࡖࡗࡎࡈࡉࡍࡋࡗ࡝ࡤࡉࡏࡏࡈࡌࡋ࡚ࡘࡁࡕࡋࡒࡒࡤ࡟ࡍࡍࠩ⅝")] = json.dumps(parsed)
            scripts = bstack1l1l1l1l1_opy_.bstack1llll1l11l11_opy_(bstack111ll1111_opy_[bstack111111l_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠩ⅞")][bstack111111l_opy_ (u"ࠪࡳࡵࡺࡩࡰࡰࡶࠫ⅟")][bstack111111l_opy_ (u"ࠫࡸࡩࡲࡪࡲࡷࡷࠬⅠ")], bstack111111l_opy_ (u"ࠬࡴࡡ࡮ࡧࠪⅡ"), bstack111111l_opy_ (u"࠭ࡣࡰ࡯ࡰࡥࡳࡪࠧⅢ"))
            bstack11l1llll11_opy_.bstack1l1llll11l_opy_(scripts)
            commands = bstack111ll1111_opy_[bstack111111l_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠧⅣ")][bstack111111l_opy_ (u"ࠨࡱࡳࡸ࡮ࡵ࡮ࡴࠩⅤ")][bstack111111l_opy_ (u"ࠩࡦࡳࡲࡳࡡ࡯ࡦࡶࡘࡴ࡝ࡲࡢࡲࠪⅥ")].get(bstack111111l_opy_ (u"ࠪࡧࡴࡳ࡭ࡢࡰࡧࡷࠬⅦ"))
            bstack11l1llll11_opy_.bstack1lllll11llll_opy_(commands)
            bstack1lllll1l1ll1_opy_ = capabilities.get(bstack111111l_opy_ (u"ࠫ࡬ࡵ࡯ࡨ࠼ࡦ࡬ࡷࡵ࡭ࡦࡑࡳࡸ࡮ࡵ࡮ࡴࠩⅧ"))
            bstack11l1llll11_opy_.bstack1lllll1l1111_opy_(bstack1lllll1l1ll1_opy_)
            bstack11l1llll11_opy_.store()
        return [bstack1llll11ll1ll_opy_, bstack111ll1111_opy_[bstack111111l_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡣ࡭ࡧࡳࡩࡧࡧࡣ࡮ࡪࠧⅨ")]]
    @classmethod
    def bstack1llll11lll1l_opy_(cls, response=None):
        os.environ[bstack111111l_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡕࡖࡋࡇࠫⅩ")] = bstack111111l_opy_ (u"ࠧ࡯ࡷ࡯ࡰࠬⅪ")
        os.environ[bstack111111l_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡍ࡛ࡂࡠࡌ࡚ࡘࠬⅫ")] = bstack111111l_opy_ (u"ࠩࡱࡹࡱࡲࠧⅬ")
        os.environ[bstack111111l_opy_ (u"ࠪࡆࡘࡥࡔࡆࡕࡗࡓࡕ࡙࡟ࡃࡗࡌࡐࡉࡥࡃࡐࡏࡓࡐࡊ࡚ࡅࡅࠩⅭ")] = bstack111111l_opy_ (u"ࠫ࡫ࡧ࡬ࡴࡧࠪⅮ")
        os.environ[bstack111111l_opy_ (u"ࠬࡈࡓࡠࡖࡈࡗ࡙ࡕࡐࡔࡡࡅ࡙ࡎࡒࡄࡠࡊࡄࡗࡍࡋࡄࡠࡋࡇࠫⅯ")] = bstack111111l_opy_ (u"ࠨ࡮ࡶ࡮࡯ࠦⅰ")
        os.environ[bstack111111l_opy_ (u"ࠧࡃࡕࡢࡘࡊ࡙ࡔࡐࡒࡖࡣࡆࡒࡌࡐ࡙ࡢࡗࡈࡘࡅࡆࡐࡖࡌࡔ࡚ࡓࠨⅱ")] = bstack111111l_opy_ (u"ࠣࡰࡸࡰࡱࠨⅲ")
        cls.bstack1llll1l111ll_opy_(response, bstack111111l_opy_ (u"ࠤࡲࡦࡸ࡫ࡲࡷࡣࡥ࡭ࡱ࡯ࡴࡺࠤⅳ"))
        return [None, None, None]
    @classmethod
    def bstack1llll1l1l11l_opy_(cls, response=None):
        os.environ[bstack111111l_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚ࡈࡖࡄࡢ࡙࡚ࡏࡄࠨⅴ")] = bstack111111l_opy_ (u"ࠫࡳࡻ࡬࡭ࠩⅵ")
        os.environ[bstack111111l_opy_ (u"ࠬࡈࡓࡠࡃ࠴࠵࡞ࡥࡊࡘࡖࠪⅶ")] = bstack111111l_opy_ (u"࠭࡮ࡶ࡮࡯ࠫⅷ")
        os.environ[bstack111111l_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡋ࡙ࡗࠫⅸ")] = bstack111111l_opy_ (u"ࠨࡰࡸࡰࡱ࠭ⅹ")
        cls.bstack1llll1l111ll_opy_(response, bstack111111l_opy_ (u"ࠤࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠤⅺ"))
        return [None, None, None]
    @classmethod
    def bstack1llll11llll1_opy_(cls, jwt, build_hashed_id):
        os.environ[bstack111111l_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚ࡈࡖࡄࡢࡎ࡜࡚ࠧⅻ")] = jwt
        os.environ[bstack111111l_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡉࡗࡅࡣ࡚࡛ࡉࡅࠩⅼ")] = build_hashed_id
    @classmethod
    def bstack1llll1l111ll_opy_(cls, response=None, product=bstack111111l_opy_ (u"ࠧࠨⅽ")):
        if response == None or response.get(bstack111111l_opy_ (u"࠭ࡥࡳࡴࡲࡶࡸ࠭ⅾ")) == None:
            logger.error(product + bstack111111l_opy_ (u"ࠢࠡࡄࡸ࡭ࡱࡪࠠࡤࡴࡨࡥࡹ࡯࡯࡯ࠢࡩࡥ࡮ࡲࡥࡥࠤⅿ"))
            return
        for error in response[bstack111111l_opy_ (u"ࠨࡧࡵࡶࡴࡸࡳࠨↀ")]:
            bstack1111lll1ll1_opy_ = error[bstack111111l_opy_ (u"ࠩ࡮ࡩࡾ࠭ↁ")]
            error_message = error[bstack111111l_opy_ (u"ࠪࡱࡪࡹࡳࡢࡩࡨࠫↂ")]
            if error_message:
                if bstack1111lll1ll1_opy_ == bstack111111l_opy_ (u"ࠦࡊࡘࡒࡐࡔࡢࡅࡈࡉࡅࡔࡕࡢࡈࡊࡔࡉࡆࡆࠥↃ"):
                    logger.info(error_message)
                else:
                    logger.error(error_message)
            else:
                logger.error(bstack111111l_opy_ (u"ࠧࡊࡡࡵࡣࠣࡹࡵࡲ࡯ࡢࡦࠣࡸࡴࠦࡂࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࠥࠨↄ") + product + bstack111111l_opy_ (u"ࠨࠠࡧࡣ࡬ࡰࡪࡪࠠࡥࡷࡨࠤࡹࡵࠠࡴࡱࡰࡩࠥ࡫ࡲࡳࡱࡵࠦↅ"))
    @classmethod
    def bstack1llll1l1llll_opy_(cls):
        if cls.bstack11l11l1l1ll_opy_ is not None:
            return
        cls.bstack11l11l1l1ll_opy_ = bstack111ll111lll_opy_(cls.post_data)
        cls.bstack11l11l1l1ll_opy_.start()
    @classmethod
    def bstack11lll11l_opy_(cls):
        if cls.bstack11l11l1l1ll_opy_ is None:
            return
        cls.bstack11l11l1l1ll_opy_.shutdown()
    @classmethod
    @error_handler(class_method=True)
    def post_data(cls, bstack1l111111_opy_, event_url=bstack111111l_opy_ (u"ࠧࡢࡲ࡬࠳ࡻ࠷࠯ࡣࡣࡷࡧ࡭࠭ↆ")):
        config = {
            bstack111111l_opy_ (u"ࠨࡪࡨࡥࡩ࡫ࡲࡴࠩↇ"): cls.default_headers()
        }
        logger.debug(bstack111111l_opy_ (u"ࠤࡳࡳࡸࡺ࡟ࡥࡣࡷࡥ࠿ࠦࡓࡦࡰࡧ࡭ࡳ࡭ࠠࡥࡣࡷࡥࠥࡺ࡯ࠡࡶࡨࡷࡹ࡮ࡵࡣࠢࡩࡳࡷࠦࡥࡷࡧࡱࡸࡸࠦࡻࡾࠤↈ").format(bstack111111l_opy_ (u"ࠪ࠰ࠥ࠭↉").join([event[bstack111111l_opy_ (u"ࠫࡪࡼࡥ࡯ࡶࡢࡸࡾࡶࡥࠨ↊")] for event in bstack1l111111_opy_])))
        response = bstack1l11l1ll1l_opy_(bstack111111l_opy_ (u"ࠬࡖࡏࡔࡖࠪ↋"), cls.request_url(event_url), bstack1l111111_opy_, config)
        bstack1llll1lll111_opy_ = response.json()
    @classmethod
    def bstack1l11l1ll_opy_(cls, bstack1l111111_opy_, event_url=bstack111111l_opy_ (u"࠭ࡡࡱ࡫࠲ࡺ࠶࠵ࡢࡢࡶࡦ࡬ࠬ↌")):
        logger.debug(bstack111111l_opy_ (u"ࠢࡴࡧࡱࡨࡤࡪࡡࡵࡣ࠽ࠤࡆࡺࡴࡦ࡯ࡳࡸ࡮ࡴࡧࠡࡶࡲࠤࡦࡪࡤࠡࡦࡤࡸࡦࠦࡴࡰࠢࡥࡥࡹࡩࡨࠡࡹ࡬ࡸ࡭ࠦࡥࡷࡧࡱࡸࡤࡺࡹࡱࡧ࠽ࠤࢀࢃࠢ↍").format(bstack1l111111_opy_[bstack111111l_opy_ (u"ࠨࡧࡹࡩࡳࡺ࡟ࡵࡻࡳࡩࠬ↎")]))
        if not bstack1l1l1l1l1_opy_.bstack1llll1l1111l_opy_(bstack1l111111_opy_[bstack111111l_opy_ (u"ࠩࡨࡺࡪࡴࡴࡠࡶࡼࡴࡪ࠭↏")]):
            logger.debug(bstack111111l_opy_ (u"ࠥࡷࡪࡴࡤࡠࡦࡤࡸࡦࡀࠠࡏࡱࡷࠤࡦࡪࡤࡪࡰࡪࠤࡩࡧࡴࡢࠢࡺ࡭ࡹ࡮ࠠࡦࡸࡨࡲࡹࡥࡴࡺࡲࡨ࠾ࠥࢁࡽࠣ←").format(bstack1l111111_opy_[bstack111111l_opy_ (u"ࠫࡪࡼࡥ࡯ࡶࡢࡸࡾࡶࡥࠨ↑")]))
            return
        bstack1l1l1l1ll_opy_ = bstack1l1l1l1l1_opy_.bstack1llll1l1l1l1_opy_(bstack1l111111_opy_[bstack111111l_opy_ (u"ࠬ࡫ࡶࡦࡰࡷࡣࡹࡿࡰࡦࠩ→")], bstack1l111111_opy_.get(bstack111111l_opy_ (u"࠭ࡴࡦࡵࡷࡣࡷࡻ࡮ࠨ↓")))
        if bstack1l1l1l1ll_opy_ != None:
            if bstack1l111111_opy_.get(bstack111111l_opy_ (u"ࠧࡵࡧࡶࡸࡤࡸࡵ࡯ࠩ↔")) != None:
                bstack1l111111_opy_[bstack111111l_opy_ (u"ࠨࡶࡨࡷࡹࡥࡲࡶࡰࠪ↕")][bstack111111l_opy_ (u"ࠩࡳࡶࡴࡪࡵࡤࡶࡢࡱࡦࡶࠧ↖")] = bstack1l1l1l1ll_opy_
            else:
                bstack1l111111_opy_[bstack111111l_opy_ (u"ࠪࡴࡷࡵࡤࡶࡥࡷࡣࡲࡧࡰࠨ↗")] = bstack1l1l1l1ll_opy_
        if event_url == bstack111111l_opy_ (u"ࠫࡦࡶࡩ࠰ࡸ࠴࠳ࡧࡧࡴࡤࡪࠪ↘"):
            cls.bstack1llll1l1llll_opy_()
            logger.debug(bstack111111l_opy_ (u"ࠧࡹࡥ࡯ࡦࡢࡨࡦࡺࡡ࠻ࠢࡄࡨࡩ࡯࡮ࡨࠢࡧࡥࡹࡧࠠࡵࡱࠣࡦࡦࡺࡣࡩࠢࡺ࡭ࡹ࡮ࠠࡦࡸࡨࡲࡹࡥࡴࡺࡲࡨ࠾ࠥࢁࡽࠣ↙").format(bstack1l111111_opy_[bstack111111l_opy_ (u"࠭ࡥࡷࡧࡱࡸࡤࡺࡹࡱࡧࠪ↚")]))
            cls.bstack11l11l1l1ll_opy_.add(bstack1l111111_opy_)
        elif event_url == bstack111111l_opy_ (u"ࠧࡢࡲ࡬࠳ࡻ࠷࠯ࡴࡥࡵࡩࡪࡴࡳࡩࡱࡷࡷࠬ↛"):
            cls.post_data([bstack1l111111_opy_], event_url)
    @classmethod
    @error_handler(class_method=True)
    def bstack1l11l1l1_opy_(cls, logs):
        for log in logs:
            bstack1llll1l111l1_opy_ = {
                bstack111111l_opy_ (u"ࠨ࡭࡬ࡲࡩ࠭↜"): bstack111111l_opy_ (u"ࠩࡗࡉࡘ࡚࡟ࡍࡑࡊࠫ↝"),
                bstack111111l_opy_ (u"ࠪࡰࡪࡼࡥ࡭ࠩ↞"): log[bstack111111l_opy_ (u"ࠫࡱ࡫ࡶࡦ࡮ࠪ↟")],
                bstack111111l_opy_ (u"ࠬࡺࡩ࡮ࡧࡶࡸࡦࡳࡰࠨ↠"): log[bstack111111l_opy_ (u"࠭ࡴࡪ࡯ࡨࡷࡹࡧ࡭ࡱࠩ↡")],
                bstack111111l_opy_ (u"ࠧࡩࡶࡷࡴࡤࡸࡥࡴࡲࡲࡲࡸ࡫ࠧ↢"): {},
                bstack111111l_opy_ (u"ࠨ࡯ࡨࡷࡸࡧࡧࡦࠩ↣"): log[bstack111111l_opy_ (u"ࠩࡰࡩࡸࡹࡡࡨࡧࠪ↤")],
            }
            if bstack111111l_opy_ (u"ࠪࡸࡪࡹࡴࡠࡴࡸࡲࡤࡻࡵࡪࡦࠪ↥") in log:
                bstack1llll1l111l1_opy_[bstack111111l_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠫ↦")] = log[bstack111111l_opy_ (u"ࠬࡺࡥࡴࡶࡢࡶࡺࡴ࡟ࡶࡷ࡬ࡨࠬ↧")]
            elif bstack111111l_opy_ (u"࠭ࡨࡰࡱ࡮ࡣࡷࡻ࡮ࡠࡷࡸ࡭ࡩ࠭↨") in log:
                bstack1llll1l111l1_opy_[bstack111111l_opy_ (u"ࠧࡩࡱࡲ࡯ࡤࡸࡵ࡯ࡡࡸࡹ࡮ࡪࠧ↩")] = log[bstack111111l_opy_ (u"ࠨࡪࡲࡳࡰࡥࡲࡶࡰࡢࡹࡺ࡯ࡤࠨ↪")]
            cls.bstack1l11l1ll_opy_({
                bstack111111l_opy_ (u"ࠩࡨࡺࡪࡴࡴࡠࡶࡼࡴࡪ࠭↫"): bstack111111l_opy_ (u"ࠪࡐࡴ࡭ࡃࡳࡧࡤࡸࡪࡪࠧ↬"),
                bstack111111l_opy_ (u"ࠫࡱࡵࡧࡴࠩ↭"): [bstack1llll1l111l1_opy_]
            })
    @classmethod
    @error_handler(class_method=True)
    def bstack1llll11lll11_opy_(cls, steps):
        bstack1llll1ll1111_opy_ = []
        for step in steps:
            bstack1llll11lllll_opy_ = {
                bstack111111l_opy_ (u"ࠬࡱࡩ࡯ࡦࠪ↮"): bstack111111l_opy_ (u"࠭ࡔࡆࡕࡗࡣࡘ࡚ࡅࡑࠩ↯"),
                bstack111111l_opy_ (u"ࠧ࡭ࡧࡹࡩࡱ࠭↰"): step[bstack111111l_opy_ (u"ࠨ࡮ࡨࡺࡪࡲࠧ↱")],
                bstack111111l_opy_ (u"ࠩࡷ࡭ࡲ࡫ࡳࡵࡣࡰࡴࠬ↲"): step[bstack111111l_opy_ (u"ࠪࡸ࡮ࡳࡥࡴࡶࡤࡱࡵ࠭↳")],
                bstack111111l_opy_ (u"ࠫࡲ࡫ࡳࡴࡣࡪࡩࠬ↴"): step[bstack111111l_opy_ (u"ࠬࡳࡥࡴࡵࡤ࡫ࡪ࠭↵")],
                bstack111111l_opy_ (u"࠭ࡤࡶࡴࡤࡸ࡮ࡵ࡮ࠨ↶"): step[bstack111111l_opy_ (u"ࠧࡥࡷࡵࡥࡹ࡯࡯࡯ࠩ↷")]
            }
            if bstack111111l_opy_ (u"ࠨࡶࡨࡷࡹࡥࡲࡶࡰࡢࡹࡺ࡯ࡤࠨ↸") in step:
                bstack1llll11lllll_opy_[bstack111111l_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡳࡷࡱࡣࡺࡻࡩࡥࠩ↹")] = step[bstack111111l_opy_ (u"ࠪࡸࡪࡹࡴࡠࡴࡸࡲࡤࡻࡵࡪࡦࠪ↺")]
            elif bstack111111l_opy_ (u"ࠫ࡭ࡵ࡯࡬ࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠫ↻") in step:
                bstack1llll11lllll_opy_[bstack111111l_opy_ (u"ࠬ࡮࡯ࡰ࡭ࡢࡶࡺࡴ࡟ࡶࡷ࡬ࡨࠬ↼")] = step[bstack111111l_opy_ (u"࠭ࡨࡰࡱ࡮ࡣࡷࡻ࡮ࡠࡷࡸ࡭ࡩ࠭↽")]
            bstack1llll1ll1111_opy_.append(bstack1llll11lllll_opy_)
        cls.bstack1l11l1ll_opy_({
            bstack111111l_opy_ (u"ࠧࡦࡸࡨࡲࡹࡥࡴࡺࡲࡨࠫ↾"): bstack111111l_opy_ (u"ࠨࡎࡲ࡫ࡈࡸࡥࡢࡶࡨࡨࠬ↿"),
            bstack111111l_opy_ (u"ࠩ࡯ࡳ࡬ࡹࠧ⇀"): bstack1llll1ll1111_opy_
        })
    @classmethod
    @error_handler(class_method=True)
    @measure(event_name=EVENTS.bstack1l11l11l1_opy_, stage=STAGE.bstack11l11ll11_opy_)
    def bstack1l11ll111l_opy_(cls, screenshot):
        cls.bstack1l11l1ll_opy_({
            bstack111111l_opy_ (u"ࠪࡩࡻ࡫࡮ࡵࡡࡷࡽࡵ࡫ࠧ⇁"): bstack111111l_opy_ (u"ࠫࡑࡵࡧࡄࡴࡨࡥࡹ࡫ࡤࠨ⇂"),
            bstack111111l_opy_ (u"ࠬࡲ࡯ࡨࡵࠪ⇃"): [{
                bstack111111l_opy_ (u"࠭࡫ࡪࡰࡧࠫ⇄"): bstack111111l_opy_ (u"ࠧࡕࡇࡖࡘࡤ࡙ࡃࡓࡇࡈࡒࡘࡎࡏࡕࠩ⇅"),
                bstack111111l_opy_ (u"ࠨࡶ࡬ࡱࡪࡹࡴࡢ࡯ࡳࠫ⇆"): datetime.datetime.utcnow().isoformat() + bstack111111l_opy_ (u"ࠩ࡝ࠫ⇇"),
                bstack111111l_opy_ (u"ࠪࡱࡪࡹࡳࡢࡩࡨࠫ⇈"): screenshot[bstack111111l_opy_ (u"ࠫ࡮ࡳࡡࡨࡧࠪ⇉")],
                bstack111111l_opy_ (u"ࠬࡺࡥࡴࡶࡢࡶࡺࡴ࡟ࡶࡷ࡬ࡨࠬ⇊"): screenshot[bstack111111l_opy_ (u"࠭ࡴࡦࡵࡷࡣࡷࡻ࡮ࡠࡷࡸ࡭ࡩ࠭⇋")]
            }]
        }, event_url=bstack111111l_opy_ (u"ࠧࡢࡲ࡬࠳ࡻ࠷࠯ࡴࡥࡵࡩࡪࡴࡳࡩࡱࡷࡷࠬ⇌"))
    @classmethod
    @error_handler(class_method=True)
    def bstack1lll1l11l1_opy_(cls, driver):
        current_test_uuid = cls.current_test_uuid()
        if not current_test_uuid:
            return
        cls.bstack1l11l1ll_opy_({
            bstack111111l_opy_ (u"ࠨࡧࡹࡩࡳࡺ࡟ࡵࡻࡳࡩࠬ⇍"): bstack111111l_opy_ (u"ࠩࡆࡆ࡙࡙ࡥࡴࡵ࡬ࡳࡳࡉࡲࡦࡣࡷࡩࡩ࠭⇎"),
            bstack111111l_opy_ (u"ࠪࡸࡪࡹࡴࡠࡴࡸࡲࠬ⇏"): {
                bstack111111l_opy_ (u"ࠦࡺࡻࡩࡥࠤ⇐"): cls.current_test_uuid(),
                bstack111111l_opy_ (u"ࠧ࡯࡮ࡵࡧࡪࡶࡦࡺࡩࡰࡰࡶࠦ⇑"): cls.bstack1l11l111_opy_(driver)
            }
        })
    @classmethod
    def bstack1llll1l1_opy_(cls, event: str, bstack1l111111_opy_: bstack11lll1l1_opy_):
        bstack1l1ll111_opy_ = {
            bstack111111l_opy_ (u"࠭ࡥࡷࡧࡱࡸࡤࡺࡹࡱࡧࠪ⇒"): event,
            bstack1l111111_opy_.event_key(): bstack1l111111_opy_.bstack1ll11l11_opy_(event)
        }
        cls.bstack1l11l1ll_opy_(bstack1l1ll111_opy_)
        result = getattr(bstack1l111111_opy_, bstack111111l_opy_ (u"ࠧࡳࡧࡶࡹࡱࡺࠧ⇓"), None)
        if event == bstack111111l_opy_ (u"ࠨࡖࡨࡷࡹࡘࡵ࡯ࡕࡷࡥࡷࡺࡥࡥࠩ⇔"):
            threading.current_thread().bstackTestMeta = {bstack111111l_opy_ (u"ࠩࡶࡸࡦࡺࡵࡴࠩ⇕"): bstack111111l_opy_ (u"ࠪࡴࡪࡴࡤࡪࡰࡪࠫ⇖")}
        elif event == bstack111111l_opy_ (u"࡙ࠫ࡫ࡳࡵࡔࡸࡲࡋ࡯࡮ࡪࡵ࡫ࡩࡩ࠭⇗"):
            threading.current_thread().bstackTestMeta = {bstack111111l_opy_ (u"ࠬࡹࡴࡢࡶࡸࡷࠬ⇘"): getattr(result, bstack111111l_opy_ (u"࠭ࡲࡦࡵࡸࡰࡹ࠭⇙"), bstack111111l_opy_ (u"ࠧࠨ⇚"))}
    @classmethod
    def on(cls):
        if (os.environ.get(bstack111111l_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡍ࡛ࡂࡠࡌ࡚ࡘࠬ⇛"), None) is None or os.environ[bstack111111l_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡎࡕࡃࡡࡍ࡛࡙࠭⇜")] == bstack111111l_opy_ (u"ࠥࡲࡺࡲ࡬ࠣ⇝")) and (os.environ.get(bstack111111l_opy_ (u"ࠫࡇ࡙࡟ࡂ࠳࠴࡝ࡤࡐࡗࡕࠩ⇞"), None) is None or os.environ[bstack111111l_opy_ (u"ࠬࡈࡓࡠࡃ࠴࠵࡞ࡥࡊࡘࡖࠪ⇟")] == bstack111111l_opy_ (u"ࠨ࡮ࡶ࡮࡯ࠦ⇠")):
            return False
        return True
    @staticmethod
    def bstack1llll1l11lll_opy_(func):
        def wrap(*args, **kwargs):
            if bstack1ll1l111_opy_.on():
                return func(*args, **kwargs)
            return
        return wrap
    @staticmethod
    def default_headers():
        headers = {
            bstack111111l_opy_ (u"ࠧࡄࡱࡱࡸࡪࡴࡴ࠮ࡖࡼࡴࡪ࠭⇡"): bstack111111l_opy_ (u"ࠨࡣࡳࡴࡱ࡯ࡣࡢࡶ࡬ࡳࡳ࠵ࡪࡴࡱࡱࠫ⇢"),
            bstack111111l_opy_ (u"࡛ࠩ࠱ࡇ࡙ࡔࡂࡅࡎ࠱࡙ࡋࡓࡕࡑࡓࡗࠬ⇣"): bstack111111l_opy_ (u"ࠪࡸࡷࡻࡥࠨ⇤")
        }
        if os.environ.get(bstack111111l_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡉࡗࡅࡣࡏ࡝ࡔࠨ⇥"), None):
            headers[bstack111111l_opy_ (u"ࠬࡇࡵࡵࡪࡲࡶ࡮ࢀࡡࡵ࡫ࡲࡲࠬ⇦")] = bstack111111l_opy_ (u"࠭ࡂࡦࡣࡵࡩࡷࠦࡻࡾࠩ⇧").format(os.environ[bstack111111l_opy_ (u"ࠢࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡋ࡙ࡗࠦ⇨")])
        return headers
    @staticmethod
    def request_url(url):
        return bstack111111l_opy_ (u"ࠨࡽࢀ࠳ࢀࢃࠧ⇩").format(bstack1llll1l11l1l_opy_, url)
    @staticmethod
    def current_test_uuid():
        return getattr(threading.current_thread(), bstack111111l_opy_ (u"ࠩࡦࡹࡷࡸࡥ࡯ࡶࡢࡸࡪࡹࡴࡠࡷࡸ࡭ࡩ࠭⇪"), None)
    @staticmethod
    def bstack1l11l111_opy_(driver):
        return {
            bstack111l1111l1l_opy_(): bstack111l1l1ll11_opy_(driver)
        }
    @staticmethod
    def bstack1llll1l11ll1_opy_(exception_info, report):
        return [{bstack111111l_opy_ (u"ࠪࡦࡦࡩ࡫ࡵࡴࡤࡧࡪ࠭⇫"): [exception_info.exconly(), report.longreprtext]}]
    @staticmethod
    def bstack11111l111l_opy_(typename):
        if bstack111111l_opy_ (u"ࠦࡆࡹࡳࡦࡴࡷ࡭ࡴࡴࠢ⇬") in typename:
            return bstack111111l_opy_ (u"ࠧࡇࡳࡴࡧࡵࡸ࡮ࡵ࡮ࡆࡴࡵࡳࡷࠨ⇭")
        return bstack111111l_opy_ (u"ࠨࡕ࡯ࡪࡤࡲࡩࡲࡥࡥࡇࡵࡶࡴࡸࠢ⇮")