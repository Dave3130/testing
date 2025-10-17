# coding: UTF-8
import sys
bstack111l11_opy_ = sys.version_info [0] == 2
bstack111ll1l_opy_ = 2048
bstack1_opy_ = 7
def bstack11111_opy_ (bstack1l111ll_opy_):
    global bstack111ll11_opy_
    bstack1lllll_opy_ = ord (bstack1l111ll_opy_ [-1])
    bstack1l1llll_opy_ = bstack1l111ll_opy_ [:-1]
    bstack11l11l_opy_ = bstack1lllll_opy_ % len (bstack1l1llll_opy_)
    bstack111l_opy_ = bstack1l1llll_opy_ [:bstack11l11l_opy_] + bstack1l1llll_opy_ [bstack11l11l_opy_:]
    if bstack111l11_opy_:
        bstack1l1l1l_opy_ = unicode () .join ([unichr (ord (char) - bstack111ll1l_opy_ - (bstack1l_opy_ + bstack1lllll_opy_) % bstack1_opy_) for bstack1l_opy_, char in enumerate (bstack111l_opy_)])
    else:
        bstack1l1l1l_opy_ = str () .join ([chr (ord (char) - bstack111ll1l_opy_ - (bstack1l_opy_ + bstack1lllll_opy_) % bstack1_opy_) for bstack1l_opy_, char in enumerate (bstack111l_opy_)])
    return eval (bstack1l1l1l_opy_)
import json
import logging
import os
import datetime
import threading
from bstack_utils.constants import EVENTS, STAGE
from bstack_utils.helper import bstack111l11ll1l1_opy_, bstack111l11l11ll_opy_, bstack1ll1l11lll_opy_, error_handler, bstack111l1l1111l_opy_, bstack1111ll1llll_opy_, bstack111l1l1l1l1_opy_, bstack1l11llll_opy_, bstack1l1lllll_opy_
from bstack_utils.measure import measure
from bstack_utils.bstack11l11l1l111_opy_ import bstack111ll11l1l1_opy_
import bstack_utils.bstack11ll11ll11_opy_ as bstack1ll1ll1ll_opy_
from bstack_utils.bstack1l1lll11_opy_ import bstack11llll11_opy_
import bstack_utils.accessibility as bstack1lll1ll1l_opy_
from bstack_utils.bstack11l1l1l1l1_opy_ import bstack11l1l1l1l1_opy_
from bstack_utils.bstack1ll1ll11_opy_ import bstack1ll11ll1_opy_
from bstack_utils.constants import bstack1l111l111_opy_
bstack1llll11llll1_opy_ = bstack11111_opy_ (u"ࠨࡪࡷࡸࡵࡹ࠺࠰࠱ࡦࡳࡱࡲࡥࡤࡶࡲࡶ࠲ࡵࡢࡴࡧࡵࡺࡦࡨࡩ࡭࡫ࡷࡽ࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡨࡵ࡭ࠨ⃭")
logger = logging.getLogger(__name__)
class bstack1l11lll1_opy_:
    bstack11l11l1l111_opy_ = None
    bs_config = None
    bstack1l1l11l1ll_opy_ = None
    @classmethod
    @error_handler(class_method=True)
    @measure(event_name=EVENTS.bstack11l1l1l1111_opy_, stage=STAGE.bstack1111llll1l_opy_)
    def launch(cls, bs_config, bstack1l1l11l1ll_opy_):
        cls.bs_config = bs_config
        cls.bstack1l1l11l1ll_opy_ = bstack1l1l11l1ll_opy_
        try:
            cls.bstack1llll1l111l1_opy_()
            bstack1llll1lll1ll_opy_ = bstack111l11ll1l1_opy_(bs_config)
            bstack1lllll111l1l_opy_ = bstack111l11l11ll_opy_(bs_config)
            data = bstack1ll1ll1ll_opy_.bstack1llll1l1ll11_opy_(bs_config, bstack1l1l11l1ll_opy_)
            config = {
                bstack11111_opy_ (u"ࠩࡤࡹࡹ࡮⃮ࠧ"): (bstack1llll1lll1ll_opy_, bstack1lllll111l1l_opy_),
                bstack11111_opy_ (u"ࠪ࡬ࡪࡧࡤࡦࡴࡶ⃯ࠫ"): cls.default_headers()
            }
            response = bstack1ll1l11lll_opy_(bstack11111_opy_ (u"ࠫࡕࡕࡓࡕࠩ⃰"), cls.request_url(bstack11111_opy_ (u"ࠬࡧࡰࡪ࠱ࡹ࠶࠴ࡨࡵࡪ࡮ࡧࡷࠬ⃱")), data, config)
            if response.status_code != 200:
                bstack1llll1l11l_opy_ = response.json()
                if bstack1llll1l11l_opy_[bstack11111_opy_ (u"࠭ࡳࡶࡥࡦࡩࡸࡹࠧ⃲")] == False:
                    cls.bstack1llll1l11l11_opy_(bstack1llll1l11l_opy_)
                    return
                cls.bstack1llll11ll111_opy_(bstack1llll1l11l_opy_[bstack11111_opy_ (u"ࠧࡰࡤࡶࡩࡷࡼࡡࡣ࡫࡯࡭ࡹࡿࠧ⃳")])
                cls.bstack1llll1l11lll_opy_(bstack1llll1l11l_opy_[bstack11111_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠨ⃴")])
                return None
            bstack1llll1l11111_opy_ = cls.bstack1llll1l1ll1l_opy_(response)
            return bstack1llll1l11111_opy_, response.json()
        except Exception as error:
            logger.error(bstack11111_opy_ (u"ࠤࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥࡽࡨࡪ࡮ࡨࠤࡨࡸࡥࡢࡶ࡬ࡲ࡬ࠦࡢࡶ࡫࡯ࡨࠥ࡬࡯ࡳࠢࡗࡩࡸࡺࡈࡶࡤ࠽ࠤࢀࢃࠢ⃵").format(str(error)))
            return None
    @classmethod
    @error_handler(class_method=True)
    def stop(cls, bstack1llll1l111ll_opy_=None):
        if not bstack11llll11_opy_.on() and not bstack1lll1ll1l_opy_.on():
            return
        if os.environ.get(bstack11111_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚ࡈࡖࡄࡢࡎ࡜࡚ࠧ⃶")) == bstack11111_opy_ (u"ࠦࡳࡻ࡬࡭ࠤ⃷") or os.environ.get(bstack11111_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡊࡘࡆࡤ࡛ࡕࡊࡆࠪ⃸")) == bstack11111_opy_ (u"ࠨ࡮ࡶ࡮࡯ࠦ⃹"):
            logger.error(bstack11111_opy_ (u"ࠧࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣ࡭ࡳࠦࡳࡵࡱࡳࠤࡧࡻࡩ࡭ࡦࠣࡶࡪࡷࡵࡦࡵࡷࠤࡹࡵࠠࡕࡧࡶࡸࡍࡻࡢ࠻ࠢࡐ࡭ࡸࡹࡩ࡯ࡩࠣࡥࡺࡺࡨࡦࡰࡷ࡭ࡨࡧࡴࡪࡱࡱࠤࡹࡵ࡫ࡦࡰࠪ⃺"))
            return {
                bstack11111_opy_ (u"ࠨࡵࡷࡥࡹࡻࡳࠨ⃻"): bstack11111_opy_ (u"ࠩࡨࡶࡷࡵࡲࠨ⃼"),
                bstack11111_opy_ (u"ࠪࡱࡪࡹࡳࡢࡩࡨࠫ⃽"): bstack11111_opy_ (u"࡙ࠫࡵ࡫ࡦࡰ࠲ࡦࡺ࡯࡬ࡥࡋࡇࠤ࡮ࡹࠠࡶࡰࡧࡩ࡫࡯࡮ࡦࡦ࠯ࠤࡧࡻࡩ࡭ࡦࠣࡧࡷ࡫ࡡࡵ࡫ࡲࡲࠥࡳࡩࡨࡪࡷࠤ࡭ࡧࡶࡦࠢࡩࡥ࡮ࡲࡥࡥࠩ⃾")
            }
        try:
            cls.bstack11l11l1l111_opy_.shutdown()
            data = {
                bstack11111_opy_ (u"ࠬ࡬ࡩ࡯࡫ࡶ࡬ࡪࡪ࡟ࡢࡶࠪ⃿"): bstack1l11llll_opy_()
            }
            if not bstack1llll1l111ll_opy_ is None:
                data[bstack11111_opy_ (u"࠭ࡦࡪࡰ࡬ࡷ࡭࡫ࡤࡠ࡯ࡨࡸࡦࡪࡡࡵࡣࠪ℀")] = [{
                    bstack11111_opy_ (u"ࠧࡳࡧࡤࡷࡴࡴࠧ℁"): bstack11111_opy_ (u"ࠨࡷࡶࡩࡷࡥ࡫ࡪ࡮࡯ࡩࡩ࠭ℂ"),
                    bstack11111_opy_ (u"ࠩࡶ࡭࡬ࡴࡡ࡭ࠩ℃"): bstack1llll1l111ll_opy_
                }]
            config = {
                bstack11111_opy_ (u"ࠪ࡬ࡪࡧࡤࡦࡴࡶࠫ℄"): cls.default_headers()
            }
            bstack11ll11ll111_opy_ = bstack11111_opy_ (u"ࠫࡦࡶࡩ࠰ࡸ࠴࠳ࡧࡻࡩ࡭ࡦࡶ࠳ࢀࢃ࠯ࡴࡶࡲࡴࠬ℅").format(os.environ[bstack11111_opy_ (u"ࠧࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡊࡘࡆࡤ࡛ࡕࡊࡆࠥ℆")])
            bstack1llll1l1111l_opy_ = cls.request_url(bstack11ll11ll111_opy_)
            response = bstack1ll1l11lll_opy_(bstack11111_opy_ (u"࠭ࡐࡖࡖࠪℇ"), bstack1llll1l1111l_opy_, data, config)
            if not response.ok:
                raise Exception(bstack11111_opy_ (u"ࠢࡔࡶࡲࡴࠥࡸࡥࡲࡷࡨࡷࡹࠦ࡮ࡰࡶࠣࡳࡰࠨ℈"))
        except Exception as error:
            logger.error(bstack11111_opy_ (u"ࠣࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡴࡶࡲࡴࠥࡨࡵࡪ࡮ࡧࠤࡷ࡫ࡱࡶࡧࡶࡸࠥࡺ࡯ࠡࡖࡨࡷࡹࡎࡵࡣ࠼࠽ࠤࠧ℉") + str(error))
            return {
                bstack11111_opy_ (u"ࠩࡶࡸࡦࡺࡵࡴࠩℊ"): bstack11111_opy_ (u"ࠪࡩࡷࡸ࡯ࡳࠩℋ"),
                bstack11111_opy_ (u"ࠫࡲ࡫ࡳࡴࡣࡪࡩࠬℌ"): str(error)
            }
    @classmethod
    @error_handler(class_method=True)
    def bstack1llll1l1ll1l_opy_(cls, response):
        bstack1llll1l11l_opy_ = response.json() if not isinstance(response, dict) else response
        bstack1llll1l11111_opy_ = {}
        if bstack1llll1l11l_opy_.get(bstack11111_opy_ (u"ࠬࡰࡷࡵࠩℍ")) is None:
            os.environ[bstack11111_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡊࡘࡖࠪℎ")] = bstack11111_opy_ (u"ࠧ࡯ࡷ࡯ࡰࠬℏ")
        else:
            os.environ[bstack11111_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡍ࡛ࡂࡠࡌ࡚ࡘࠬℐ")] = bstack1llll1l11l_opy_.get(bstack11111_opy_ (u"ࠩ࡭ࡻࡹ࠭ℑ"), bstack11111_opy_ (u"ࠪࡲࡺࡲ࡬ࠨℒ"))
        os.environ[bstack11111_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡉࡗࡅࡣ࡚࡛ࡉࡅࠩℓ")] = bstack1llll1l11l_opy_.get(bstack11111_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡣ࡭ࡧࡳࡩࡧࡧࡣ࡮ࡪࠧ℔"), bstack11111_opy_ (u"࠭࡮ࡶ࡮࡯ࠫℕ"))
        logger.info(bstack11111_opy_ (u"ࠧࡕࡧࡶࡸ࡭ࡻࡢࠡࡵࡷࡥࡷࡺࡥࡥࠢࡺ࡭ࡹ࡮ࠠࡪࡦ࠽ࠤࠬ№") + os.getenv(bstack11111_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡍ࡛ࡂࡠࡗࡘࡍࡉ࠭℗")));
        if bstack11llll11_opy_.bstack11l11l1l1l1_opy_(cls.bs_config, cls.bstack1l1l11l1ll_opy_.get(bstack11111_opy_ (u"ࠩࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࡤࡻࡳࡦࡦࠪ℘"), bstack11111_opy_ (u"ࠪࠫℙ"))) is True:
            bstack11ll11l1ll1_opy_, build_hashed_id, bstack1llll11lll1l_opy_ = cls.bstack1llll1l11l1l_opy_(bstack1llll1l11l_opy_)
            if bstack11ll11l1ll1_opy_ != None and build_hashed_id != None:
                bstack1llll1l11111_opy_[bstack11111_opy_ (u"ࠫࡴࡨࡳࡦࡴࡹࡥࡧ࡯࡬ࡪࡶࡼࠫℚ")] = {
                    bstack11111_opy_ (u"ࠬࡰࡷࡵࡡࡷࡳࡰ࡫࡮ࠨℛ"): bstack11ll11l1ll1_opy_,
                    bstack11111_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡤ࡮ࡡࡴࡪࡨࡨࡤ࡯ࡤࠨℜ"): build_hashed_id,
                    bstack11111_opy_ (u"ࠧࡢ࡮࡯ࡳࡼࡥࡳࡤࡴࡨࡩࡳࡹࡨࡰࡶࡶࠫℝ"): bstack1llll11lll1l_opy_
                }
            else:
                bstack1llll1l11111_opy_[bstack11111_opy_ (u"ࠨࡱࡥࡷࡪࡸࡶࡢࡤ࡬ࡰ࡮ࡺࡹࠨ℞")] = {}
        else:
            bstack1llll1l11111_opy_[bstack11111_opy_ (u"ࠩࡲࡦࡸ࡫ࡲࡷࡣࡥ࡭ࡱ࡯ࡴࡺࠩ℟")] = {}
        bstack1llll11ll1l1_opy_, build_hashed_id = cls.bstack1llll1l1l11l_opy_(bstack1llll1l11l_opy_)
        if bstack1llll11ll1l1_opy_ != None and build_hashed_id != None:
            bstack1llll1l11111_opy_[bstack11111_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠪ℠")] = {
                bstack11111_opy_ (u"ࠫࡦࡻࡴࡩࡡࡷࡳࡰ࡫࡮ࠨ℡"): bstack1llll11ll1l1_opy_,
                bstack11111_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡣ࡭ࡧࡳࡩࡧࡧࡣ࡮ࡪࠧ™"): build_hashed_id,
            }
        else:
            bstack1llll1l11111_opy_[bstack11111_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾ࠭℣")] = {}
        if bstack1llll1l11111_opy_[bstack11111_opy_ (u"ࠧࡰࡤࡶࡩࡷࡼࡡࡣ࡫࡯࡭ࡹࡿࠧℤ")].get(bstack11111_opy_ (u"ࠨࡤࡸ࡭ࡱࡪ࡟ࡩࡣࡶ࡬ࡪࡪ࡟ࡪࡦࠪ℥")) != None or bstack1llll1l11111_opy_[bstack11111_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠩΩ")].get(bstack11111_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡡ࡫ࡥࡸ࡮ࡥࡥࡡ࡬ࡨࠬ℧")) != None:
            cls.bstack1llll1l11ll1_opy_(bstack1llll1l11l_opy_.get(bstack11111_opy_ (u"ࠫ࡯ࡽࡴࠨℨ")), bstack1llll1l11l_opy_.get(bstack11111_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡣ࡭ࡧࡳࡩࡧࡧࡣ࡮ࡪࠧ℩")))
        return bstack1llll1l11111_opy_
    @classmethod
    def bstack1llll1l11l1l_opy_(cls, bstack1llll1l11l_opy_):
        if bstack1llll1l11l_opy_.get(bstack11111_opy_ (u"࠭࡯ࡣࡵࡨࡶࡻࡧࡢࡪ࡮࡬ࡸࡾ࠭K")) == None:
            cls.bstack1llll11ll111_opy_()
            return [None, None, None]
        if bstack1llll1l11l_opy_[bstack11111_opy_ (u"ࠧࡰࡤࡶࡩࡷࡼࡡࡣ࡫࡯࡭ࡹࡿࠧÅ")][bstack11111_opy_ (u"ࠨࡵࡸࡧࡨ࡫ࡳࡴࠩℬ")] != True:
            cls.bstack1llll11ll111_opy_(bstack1llll1l11l_opy_[bstack11111_opy_ (u"ࠩࡲࡦࡸ࡫ࡲࡷࡣࡥ࡭ࡱ࡯ࡴࡺࠩℭ")])
            return [None, None, None]
        logger.debug(bstack11111_opy_ (u"ࠪࡿࢂࠦࡂࡶ࡫࡯ࡨࠥࡩࡲࡦࡣࡷ࡭ࡴࡴࠠࡔࡷࡦࡧࡪࡹࡳࡧࡷ࡯ࠥࠬ℮").format(bstack1l111l111_opy_))
        os.environ[bstack11111_opy_ (u"ࠫࡇ࡙࡟ࡕࡇࡖࡘࡔࡖࡓࡠࡄࡘࡍࡑࡊ࡟ࡄࡑࡐࡔࡑࡋࡔࡆࡆࠪℯ")] = bstack11111_opy_ (u"ࠬࡺࡲࡶࡧࠪℰ")
        if bstack1llll1l11l_opy_.get(bstack11111_opy_ (u"࠭ࡪࡸࡶࠪℱ")):
            os.environ[bstack11111_opy_ (u"ࠧࡄࡔࡈࡈࡊࡔࡔࡊࡃࡏࡗࡤࡌࡏࡓࡡࡆࡖࡆ࡙ࡈࡠࡔࡈࡔࡔࡘࡔࡊࡐࡊࠫℲ")] = json.dumps({
                bstack11111_opy_ (u"ࠨࡷࡶࡩࡷࡴࡡ࡮ࡧࠪℳ"): bstack111l11ll1l1_opy_(cls.bs_config),
                bstack11111_opy_ (u"ࠩࡳࡥࡸࡹࡷࡰࡴࡧࠫℴ"): bstack111l11l11ll_opy_(cls.bs_config)
            })
        if bstack1llll1l11l_opy_.get(bstack11111_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡡ࡫ࡥࡸ࡮ࡥࡥࡡ࡬ࡨࠬℵ")):
            os.environ[bstack11111_opy_ (u"ࠫࡇ࡙࡟ࡕࡇࡖࡘࡔࡖࡓࡠࡄࡘࡍࡑࡊ࡟ࡉࡃࡖࡌࡊࡊ࡟ࡊࡆࠪℶ")] = bstack1llll1l11l_opy_[bstack11111_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡣ࡭ࡧࡳࡩࡧࡧࡣ࡮ࡪࠧℷ")]
        if bstack1llll1l11l_opy_[bstack11111_opy_ (u"࠭࡯ࡣࡵࡨࡶࡻࡧࡢࡪ࡮࡬ࡸࡾ࠭ℸ")].get(bstack11111_opy_ (u"ࠧࡰࡲࡷ࡭ࡴࡴࡳࠨℹ"), {}).get(bstack11111_opy_ (u"ࠨࡣ࡯ࡰࡴࡽ࡟ࡴࡥࡵࡩࡪࡴࡳࡩࡱࡷࡷࠬ℺")):
            os.environ[bstack11111_opy_ (u"ࠩࡅࡗࡤ࡚ࡅࡔࡖࡒࡔࡘࡥࡁࡍࡎࡒ࡛ࡤ࡙ࡃࡓࡇࡈࡒࡘࡎࡏࡕࡕࠪ℻")] = str(bstack1llll1l11l_opy_[bstack11111_opy_ (u"ࠪࡳࡧࡹࡥࡳࡸࡤࡦ࡮ࡲࡩࡵࡻࠪℼ")][bstack11111_opy_ (u"ࠫࡴࡶࡴࡪࡱࡱࡷࠬℽ")][bstack11111_opy_ (u"ࠬࡧ࡬࡭ࡱࡺࡣࡸࡩࡲࡦࡧࡱࡷ࡭ࡵࡴࡴࠩℾ")])
        else:
            os.environ[bstack11111_opy_ (u"࠭ࡂࡔࡡࡗࡉࡘ࡚ࡏࡑࡕࡢࡅࡑࡒࡏࡘࡡࡖࡇࡗࡋࡅࡏࡕࡋࡓ࡙࡙ࠧℿ")] = bstack11111_opy_ (u"ࠢ࡯ࡷ࡯ࡰࠧ⅀")
        return [bstack1llll1l11l_opy_[bstack11111_opy_ (u"ࠨ࡬ࡺࡸࠬ⅁")], bstack1llll1l11l_opy_[bstack11111_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡠࡪࡤࡷ࡭࡫ࡤࡠ࡫ࡧࠫ⅂")], os.environ[bstack11111_opy_ (u"ࠪࡆࡘࡥࡔࡆࡕࡗࡓࡕ࡙࡟ࡂࡎࡏࡓ࡜ࡥࡓࡄࡔࡈࡉࡓ࡙ࡈࡐࡖࡖࠫ⅃")]]
    @classmethod
    def bstack1llll1l1l11l_opy_(cls, bstack1llll1l11l_opy_):
        if bstack1llll1l11l_opy_.get(bstack11111_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠫ⅄")) == None:
            cls.bstack1llll1l11lll_opy_()
            return [None, None]
        if bstack1llll1l11l_opy_[bstack11111_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠬⅅ")][bstack11111_opy_ (u"࠭ࡳࡶࡥࡦࡩࡸࡹࠧⅆ")] != True:
            cls.bstack1llll1l11lll_opy_(bstack1llll1l11l_opy_[bstack11111_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠧⅇ")])
            return [None, None]
        if bstack1llll1l11l_opy_[bstack11111_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠨⅈ")].get(bstack11111_opy_ (u"ࠩࡲࡴࡹ࡯࡯࡯ࡵࠪⅉ")):
            logger.debug(bstack11111_opy_ (u"ࠪࡘࡪࡹࡴࠡࡃࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡄࡸ࡭ࡱࡪࠠࡤࡴࡨࡥࡹ࡯࡯࡯ࠢࡖࡹࡨࡩࡥࡴࡵࡩࡹࡱࠧࠧ⅊"))
            parsed = json.loads(os.getenv(bstack11111_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡠࡃࡆࡇࡊ࡙ࡓࡊࡄࡌࡐࡎ࡚࡙ࡠࡅࡒࡒࡋࡏࡇࡖࡔࡄࡘࡎࡕࡎࡠ࡛ࡐࡐࠬ⅋"), bstack11111_opy_ (u"ࠬࢁࡽࠨ⅌")))
            capabilities = bstack1ll1ll1ll_opy_.bstack1llll11ll11l_opy_(bstack1llll1l11l_opy_[bstack11111_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾ࠭⅍")][bstack11111_opy_ (u"ࠧࡰࡲࡷ࡭ࡴࡴࡳࠨⅎ")][bstack11111_opy_ (u"ࠨࡥࡤࡴࡦࡨࡩ࡭࡫ࡷ࡭ࡪࡹࠧ⅏")], bstack11111_opy_ (u"ࠩࡱࡥࡲ࡫ࠧ⅐"), bstack11111_opy_ (u"ࠪࡺࡦࡲࡵࡦࠩ⅑"))
            bstack1llll11ll1l1_opy_ = capabilities[bstack11111_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࡘࡴࡱࡥ࡯ࠩ⅒")]
            os.environ[bstack11111_opy_ (u"ࠬࡈࡓࡠࡃ࠴࠵࡞ࡥࡊࡘࡖࠪ⅓")] = bstack1llll11ll1l1_opy_
            if bstack11111_opy_ (u"ࠨࡡࡶࡶࡲࡱࡦࡺࡥࠣ⅔") in bstack1llll1l11l_opy_ and bstack1llll1l11l_opy_.get(bstack11111_opy_ (u"ࠢࡢࡲࡳࡣࡦࡻࡴࡰ࡯ࡤࡸࡪࠨ⅕")) is None:
                parsed[bstack11111_opy_ (u"ࠨࡵࡦࡥࡳࡴࡥࡳࡘࡨࡶࡸ࡯࡯࡯ࠩ⅖")] = capabilities[bstack11111_opy_ (u"ࠩࡶࡧࡦࡴ࡮ࡦࡴ࡙ࡩࡷࡹࡩࡰࡰࠪ⅗")]
            os.environ[bstack11111_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚࡟ࡂࡅࡆࡉࡘ࡙ࡉࡃࡋࡏࡍ࡙࡟࡟ࡄࡑࡑࡊࡎࡍࡕࡓࡃࡗࡍࡔࡔ࡟࡚ࡏࡏࠫ⅘")] = json.dumps(parsed)
            scripts = bstack1ll1ll1ll_opy_.bstack1llll11ll11l_opy_(bstack1llll1l11l_opy_[bstack11111_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠫ⅙")][bstack11111_opy_ (u"ࠬࡵࡰࡵ࡫ࡲࡲࡸ࠭⅚")][bstack11111_opy_ (u"࠭ࡳࡤࡴ࡬ࡴࡹࡹࠧ⅛")], bstack11111_opy_ (u"ࠧ࡯ࡣࡰࡩࠬ⅜"), bstack11111_opy_ (u"ࠨࡥࡲࡱࡲࡧ࡮ࡥࠩ⅝"))
            bstack11l1l1l1l1_opy_.bstack1llll1ll11_opy_(scripts)
            commands = bstack1llll1l11l_opy_[bstack11111_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠩ⅞")][bstack11111_opy_ (u"ࠪࡳࡵࡺࡩࡰࡰࡶࠫ⅟")][bstack11111_opy_ (u"ࠫࡨࡵ࡭࡮ࡣࡱࡨࡸ࡚࡯ࡘࡴࡤࡴࠬⅠ")].get(bstack11111_opy_ (u"ࠬࡩ࡯࡮࡯ࡤࡲࡩࡹࠧⅡ"))
            bstack11l1l1l1l1_opy_.bstack1lllll1l11ll_opy_(commands)
            bstack1lllll11llll_opy_ = capabilities.get(bstack11111_opy_ (u"࠭ࡧࡰࡱࡪ࠾ࡨ࡮ࡲࡰ࡯ࡨࡓࡵࡺࡩࡰࡰࡶࠫⅢ"))
            bstack11l1l1l1l1_opy_.bstack1lllll1l1111_opy_(bstack1lllll11llll_opy_)
            bstack11l1l1l1l1_opy_.store()
        return [bstack1llll11ll1l1_opy_, bstack1llll1l11l_opy_[bstack11111_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡥࡨࡢࡵ࡫ࡩࡩࡥࡩࡥࠩⅣ")]]
    @classmethod
    def bstack1llll11ll111_opy_(cls, response=None):
        os.environ[bstack11111_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡍ࡛ࡂࡠࡗࡘࡍࡉ࠭Ⅴ")] = bstack11111_opy_ (u"ࠩࡱࡹࡱࡲࠧⅥ")
        os.environ[bstack11111_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚ࡈࡖࡄࡢࡎ࡜࡚ࠧⅦ")] = bstack11111_opy_ (u"ࠫࡳࡻ࡬࡭ࠩⅧ")
        os.environ[bstack11111_opy_ (u"ࠬࡈࡓࡠࡖࡈࡗ࡙ࡕࡐࡔࡡࡅ࡙ࡎࡒࡄࡠࡅࡒࡑࡕࡒࡅࡕࡇࡇࠫⅨ")] = bstack11111_opy_ (u"࠭ࡦࡢ࡮ࡶࡩࠬⅩ")
        os.environ[bstack11111_opy_ (u"ࠧࡃࡕࡢࡘࡊ࡙ࡔࡐࡒࡖࡣࡇ࡛ࡉࡍࡆࡢࡌࡆ࡙ࡈࡆࡆࡢࡍࡉ࠭Ⅺ")] = bstack11111_opy_ (u"ࠣࡰࡸࡰࡱࠨⅫ")
        os.environ[bstack11111_opy_ (u"ࠩࡅࡗࡤ࡚ࡅࡔࡖࡒࡔࡘࡥࡁࡍࡎࡒ࡛ࡤ࡙ࡃࡓࡇࡈࡒࡘࡎࡏࡕࡕࠪⅬ")] = bstack11111_opy_ (u"ࠥࡲࡺࡲ࡬ࠣⅭ")
        cls.bstack1llll1l11l11_opy_(response, bstack11111_opy_ (u"ࠦࡴࡨࡳࡦࡴࡹࡥࡧ࡯࡬ࡪࡶࡼࠦⅮ"))
        return [None, None, None]
    @classmethod
    def bstack1llll1l11lll_opy_(cls, response=None):
        os.environ[bstack11111_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡊࡘࡆࡤ࡛ࡕࡊࡆࠪⅯ")] = bstack11111_opy_ (u"࠭࡮ࡶ࡮࡯ࠫⅰ")
        os.environ[bstack11111_opy_ (u"ࠧࡃࡕࡢࡅ࠶࠷࡙ࡠࡌ࡚ࡘࠬⅱ")] = bstack11111_opy_ (u"ࠨࡰࡸࡰࡱ࠭ⅲ")
        os.environ[bstack11111_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡎࡕࡃࡡࡍ࡛࡙࠭ⅳ")] = bstack11111_opy_ (u"ࠪࡲࡺࡲ࡬ࠨⅴ")
        cls.bstack1llll1l11l11_opy_(response, bstack11111_opy_ (u"ࠦࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠦⅵ"))
        return [None, None, None]
    @classmethod
    def bstack1llll1l11ll1_opy_(cls, jwt, build_hashed_id):
        os.environ[bstack11111_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡊࡘࡆࡤࡐࡗࡕࠩⅶ")] = jwt
        os.environ[bstack11111_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡕࡖࡋࡇࠫⅷ")] = build_hashed_id
    @classmethod
    def bstack1llll1l11l11_opy_(cls, response=None, product=bstack11111_opy_ (u"ࠢࠣⅸ")):
        if response == None or response.get(bstack11111_opy_ (u"ࠨࡧࡵࡶࡴࡸࡳࠨⅹ")) == None:
            logger.error(product + bstack11111_opy_ (u"ࠤࠣࡆࡺ࡯࡬ࡥࠢࡦࡶࡪࡧࡴࡪࡱࡱࠤ࡫ࡧࡩ࡭ࡧࡧࠦⅺ"))
            return
        for error in response[bstack11111_opy_ (u"ࠪࡩࡷࡸ࡯ࡳࡵࠪⅻ")]:
            bstack1111ll11l11_opy_ = error[bstack11111_opy_ (u"ࠫࡰ࡫ࡹࠨⅼ")]
            error_message = error[bstack11111_opy_ (u"ࠬࡳࡥࡴࡵࡤ࡫ࡪ࠭ⅽ")]
            if error_message:
                if bstack1111ll11l11_opy_ == bstack11111_opy_ (u"ࠨࡅࡓࡔࡒࡖࡤࡇࡃࡄࡇࡖࡗࡤࡊࡅࡏࡋࡈࡈࠧⅾ"):
                    logger.info(error_message)
                else:
                    logger.error(error_message)
            else:
                logger.error(bstack11111_opy_ (u"ࠢࡅࡣࡷࡥࠥࡻࡰ࡭ࡱࡤࡨࠥࡺ࡯ࠡࡄࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࠠࠣⅿ") + product + bstack11111_opy_ (u"ࠣࠢࡩࡥ࡮ࡲࡥࡥࠢࡧࡹࡪࠦࡴࡰࠢࡶࡳࡲ࡫ࠠࡦࡴࡵࡳࡷࠨↀ"))
    @classmethod
    def bstack1llll1l111l1_opy_(cls):
        if cls.bstack11l11l1l111_opy_ is not None:
            return
        cls.bstack11l11l1l111_opy_ = bstack111ll11l1l1_opy_(cls.post_data)
        cls.bstack11l11l1l111_opy_.start()
    @classmethod
    def bstack1l1l1l1l_opy_(cls):
        if cls.bstack11l11l1l111_opy_ is None:
            return
        cls.bstack11l11l1l111_opy_.shutdown()
    @classmethod
    @error_handler(class_method=True)
    def post_data(cls, bstack1l11l111_opy_, event_url=bstack11111_opy_ (u"ࠩࡤࡴ࡮࠵ࡶ࠲࠱ࡥࡥࡹࡩࡨࠨↁ")):
        config = {
            bstack11111_opy_ (u"ࠪ࡬ࡪࡧࡤࡦࡴࡶࠫↂ"): cls.default_headers()
        }
        logger.debug(bstack11111_opy_ (u"ࠦࡵࡵࡳࡵࡡࡧࡥࡹࡧ࠺ࠡࡕࡨࡲࡩ࡯࡮ࡨࠢࡧࡥࡹࡧࠠࡵࡱࠣࡸࡪࡹࡴࡩࡷࡥࠤ࡫ࡵࡲࠡࡧࡹࡩࡳࡺࡳࠡࡽࢀࠦↃ").format(bstack11111_opy_ (u"ࠬ࠲ࠠࠨↄ").join([event[bstack11111_opy_ (u"࠭ࡥࡷࡧࡱࡸࡤࡺࡹࡱࡧࠪↅ")] for event in bstack1l11l111_opy_])))
        response = bstack1ll1l11lll_opy_(bstack11111_opy_ (u"ࠧࡑࡑࡖࡘࠬↆ"), cls.request_url(event_url), bstack1l11l111_opy_, config)
        bstack1lllll11l1l1_opy_ = response.json()
    @classmethod
    def bstack1ll11lll_opy_(cls, bstack1l11l111_opy_, event_url=bstack11111_opy_ (u"ࠨࡣࡳ࡭࠴ࡼ࠱࠰ࡤࡤࡸࡨ࡮ࠧↇ")):
        logger.debug(bstack11111_opy_ (u"ࠤࡶࡩࡳࡪ࡟ࡥࡣࡷࡥ࠿ࠦࡁࡵࡶࡨࡱࡵࡺࡩ࡯ࡩࠣࡸࡴࠦࡡࡥࡦࠣࡨࡦࡺࡡࠡࡶࡲࠤࡧࡧࡴࡤࡪࠣࡻ࡮ࡺࡨࠡࡧࡹࡩࡳࡺ࡟ࡵࡻࡳࡩ࠿ࠦࡻࡾࠤↈ").format(bstack1l11l111_opy_[bstack11111_opy_ (u"ࠪࡩࡻ࡫࡮ࡵࡡࡷࡽࡵ࡫ࠧ↉")]))
        if not bstack1ll1ll1ll_opy_.bstack1llll11lllll_opy_(bstack1l11l111_opy_[bstack11111_opy_ (u"ࠫࡪࡼࡥ࡯ࡶࡢࡸࡾࡶࡥࠨ↊")]):
            logger.debug(bstack11111_opy_ (u"ࠧࡹࡥ࡯ࡦࡢࡨࡦࡺࡡ࠻ࠢࡑࡳࡹࠦࡡࡥࡦ࡬ࡲ࡬ࠦࡤࡢࡶࡤࠤࡼ࡯ࡴࡩࠢࡨࡺࡪࡴࡴࡠࡶࡼࡴࡪࡀࠠࡼࡿࠥ↋").format(bstack1l11l111_opy_[bstack11111_opy_ (u"࠭ࡥࡷࡧࡱࡸࡤࡺࡹࡱࡧࠪ↌")]))
            return
        bstack111lllll1_opy_ = bstack1ll1ll1ll_opy_.bstack1llll11lll11_opy_(bstack1l11l111_opy_[bstack11111_opy_ (u"ࠧࡦࡸࡨࡲࡹࡥࡴࡺࡲࡨࠫ↍")], bstack1l11l111_opy_.get(bstack11111_opy_ (u"ࠨࡶࡨࡷࡹࡥࡲࡶࡰࠪ↎")))
        if bstack111lllll1_opy_ != None:
            if bstack1l11l111_opy_.get(bstack11111_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡳࡷࡱࠫ↏")) != None:
                bstack1l11l111_opy_[bstack11111_opy_ (u"ࠪࡸࡪࡹࡴࡠࡴࡸࡲࠬ←")][bstack11111_opy_ (u"ࠫࡵࡸ࡯ࡥࡷࡦࡸࡤࡳࡡࡱࠩ↑")] = bstack111lllll1_opy_
            else:
                bstack1l11l111_opy_[bstack11111_opy_ (u"ࠬࡶࡲࡰࡦࡸࡧࡹࡥ࡭ࡢࡲࠪ→")] = bstack111lllll1_opy_
        if event_url == bstack11111_opy_ (u"࠭ࡡࡱ࡫࠲ࡺ࠶࠵ࡢࡢࡶࡦ࡬ࠬ↓"):
            cls.bstack1llll1l111l1_opy_()
            logger.debug(bstack11111_opy_ (u"ࠢࡴࡧࡱࡨࡤࡪࡡࡵࡣ࠽ࠤࡆࡪࡤࡪࡰࡪࠤࡩࡧࡴࡢࠢࡷࡳࠥࡨࡡࡵࡥ࡫ࠤࡼ࡯ࡴࡩࠢࡨࡺࡪࡴࡴࡠࡶࡼࡴࡪࡀࠠࡼࡿࠥ↔").format(bstack1l11l111_opy_[bstack11111_opy_ (u"ࠨࡧࡹࡩࡳࡺ࡟ࡵࡻࡳࡩࠬ↕")]))
            cls.bstack11l11l1l111_opy_.add(bstack1l11l111_opy_)
        elif event_url == bstack11111_opy_ (u"ࠩࡤࡴ࡮࠵ࡶ࠲࠱ࡶࡧࡷ࡫ࡥ࡯ࡵ࡫ࡳࡹࡹࠧ↖"):
            cls.post_data([bstack1l11l111_opy_], event_url)
    @classmethod
    @error_handler(class_method=True)
    def bstack11llllll_opy_(cls, logs):
        for log in logs:
            bstack1llll1l1l1l1_opy_ = {
                bstack11111_opy_ (u"ࠪ࡯࡮ࡴࡤࠨ↗"): bstack11111_opy_ (u"࡙ࠫࡋࡓࡕࡡࡏࡓࡌ࠭↘"),
                bstack11111_opy_ (u"ࠬࡲࡥࡷࡧ࡯ࠫ↙"): log[bstack11111_opy_ (u"࠭࡬ࡦࡸࡨࡰࠬ↚")],
                bstack11111_opy_ (u"ࠧࡵ࡫ࡰࡩࡸࡺࡡ࡮ࡲࠪ↛"): log[bstack11111_opy_ (u"ࠨࡶ࡬ࡱࡪࡹࡴࡢ࡯ࡳࠫ↜")],
                bstack11111_opy_ (u"ࠩ࡫ࡸࡹࡶ࡟ࡳࡧࡶࡴࡴࡴࡳࡦࠩ↝"): {},
                bstack11111_opy_ (u"ࠪࡱࡪࡹࡳࡢࡩࡨࠫ↞"): log[bstack11111_opy_ (u"ࠫࡲ࡫ࡳࡴࡣࡪࡩࠬ↟")],
            }
            if bstack11111_opy_ (u"ࠬࡺࡥࡴࡶࡢࡶࡺࡴ࡟ࡶࡷ࡬ࡨࠬ↠") in log:
                bstack1llll1l1l1l1_opy_[bstack11111_opy_ (u"࠭ࡴࡦࡵࡷࡣࡷࡻ࡮ࡠࡷࡸ࡭ࡩ࠭↡")] = log[bstack11111_opy_ (u"ࠧࡵࡧࡶࡸࡤࡸࡵ࡯ࡡࡸࡹ࡮ࡪࠧ↢")]
            elif bstack11111_opy_ (u"ࠨࡪࡲࡳࡰࡥࡲࡶࡰࡢࡹࡺ࡯ࡤࠨ↣") in log:
                bstack1llll1l1l1l1_opy_[bstack11111_opy_ (u"ࠩ࡫ࡳࡴࡱ࡟ࡳࡷࡱࡣࡺࡻࡩࡥࠩ↤")] = log[bstack11111_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡠࡴࡸࡲࡤࡻࡵࡪࡦࠪ↥")]
            cls.bstack1ll11lll_opy_({
                bstack11111_opy_ (u"ࠫࡪࡼࡥ࡯ࡶࡢࡸࡾࡶࡥࠨ↦"): bstack11111_opy_ (u"ࠬࡒ࡯ࡨࡅࡵࡩࡦࡺࡥࡥࠩ↧"),
                bstack11111_opy_ (u"࠭࡬ࡰࡩࡶࠫ↨"): [bstack1llll1l1l1l1_opy_]
            })
    @classmethod
    @error_handler(class_method=True)
    def bstack1llll1l1l1ll_opy_(cls, steps):
        bstack1llll11ll1ll_opy_ = []
        for step in steps:
            bstack1llll1l1llll_opy_ = {
                bstack11111_opy_ (u"ࠧ࡬࡫ࡱࡨࠬ↩"): bstack11111_opy_ (u"ࠨࡖࡈࡗ࡙ࡥࡓࡕࡇࡓࠫ↪"),
                bstack11111_opy_ (u"ࠩ࡯ࡩࡻ࡫࡬ࠨ↫"): step[bstack11111_opy_ (u"ࠪࡰࡪࡼࡥ࡭ࠩ↬")],
                bstack11111_opy_ (u"ࠫࡹ࡯࡭ࡦࡵࡷࡥࡲࡶࠧ↭"): step[bstack11111_opy_ (u"ࠬࡺࡩ࡮ࡧࡶࡸࡦࡳࡰࠨ↮")],
                bstack11111_opy_ (u"࠭࡭ࡦࡵࡶࡥ࡬࡫ࠧ↯"): step[bstack11111_opy_ (u"ࠧ࡮ࡧࡶࡷࡦ࡭ࡥࠨ↰")],
                bstack11111_opy_ (u"ࠨࡦࡸࡶࡦࡺࡩࡰࡰࠪ↱"): step[bstack11111_opy_ (u"ࠩࡧࡹࡷࡧࡴࡪࡱࡱࠫ↲")]
            }
            if bstack11111_opy_ (u"ࠪࡸࡪࡹࡴࡠࡴࡸࡲࡤࡻࡵࡪࡦࠪ↳") in step:
                bstack1llll1l1llll_opy_[bstack11111_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠫ↴")] = step[bstack11111_opy_ (u"ࠬࡺࡥࡴࡶࡢࡶࡺࡴ࡟ࡶࡷ࡬ࡨࠬ↵")]
            elif bstack11111_opy_ (u"࠭ࡨࡰࡱ࡮ࡣࡷࡻ࡮ࡠࡷࡸ࡭ࡩ࠭↶") in step:
                bstack1llll1l1llll_opy_[bstack11111_opy_ (u"ࠧࡩࡱࡲ࡯ࡤࡸࡵ࡯ࡡࡸࡹ࡮ࡪࠧ↷")] = step[bstack11111_opy_ (u"ࠨࡪࡲࡳࡰࡥࡲࡶࡰࡢࡹࡺ࡯ࡤࠨ↸")]
            bstack1llll11ll1ll_opy_.append(bstack1llll1l1llll_opy_)
        cls.bstack1ll11lll_opy_({
            bstack11111_opy_ (u"ࠩࡨࡺࡪࡴࡴࡠࡶࡼࡴࡪ࠭↹"): bstack11111_opy_ (u"ࠪࡐࡴ࡭ࡃࡳࡧࡤࡸࡪࡪࠧ↺"),
            bstack11111_opy_ (u"ࠫࡱࡵࡧࡴࠩ↻"): bstack1llll11ll1ll_opy_
        })
    @classmethod
    @error_handler(class_method=True)
    @measure(event_name=EVENTS.bstack1l1ll11111_opy_, stage=STAGE.bstack1111llll1l_opy_)
    def bstack1111ll1l1l_opy_(cls, screenshot):
        cls.bstack1ll11lll_opy_({
            bstack11111_opy_ (u"ࠬ࡫ࡶࡦࡰࡷࡣࡹࡿࡰࡦࠩ↼"): bstack11111_opy_ (u"࠭ࡌࡰࡩࡆࡶࡪࡧࡴࡦࡦࠪ↽"),
            bstack11111_opy_ (u"ࠧ࡭ࡱࡪࡷࠬ↾"): [{
                bstack11111_opy_ (u"ࠨ࡭࡬ࡲࡩ࠭↿"): bstack11111_opy_ (u"ࠩࡗࡉࡘ࡚࡟ࡔࡅࡕࡉࡊࡔࡓࡉࡑࡗࠫ⇀"),
                bstack11111_opy_ (u"ࠪࡸ࡮ࡳࡥࡴࡶࡤࡱࡵ࠭⇁"): datetime.datetime.utcnow().isoformat() + bstack11111_opy_ (u"ࠫ࡟࠭⇂"),
                bstack11111_opy_ (u"ࠬࡳࡥࡴࡵࡤ࡫ࡪ࠭⇃"): screenshot[bstack11111_opy_ (u"࠭ࡩ࡮ࡣࡪࡩࠬ⇄")],
                bstack11111_opy_ (u"ࠧࡵࡧࡶࡸࡤࡸࡵ࡯ࡡࡸࡹ࡮ࡪࠧ⇅"): screenshot[bstack11111_opy_ (u"ࠨࡶࡨࡷࡹࡥࡲࡶࡰࡢࡹࡺ࡯ࡤࠨ⇆")]
            }]
        }, event_url=bstack11111_opy_ (u"ࠩࡤࡴ࡮࠵ࡶ࠲࠱ࡶࡧࡷ࡫ࡥ࡯ࡵ࡫ࡳࡹࡹࠧ⇇"))
    @classmethod
    @error_handler(class_method=True)
    def bstack1l1lll1ll_opy_(cls, driver):
        current_test_uuid = cls.current_test_uuid()
        if not current_test_uuid:
            return
        cls.bstack1ll11lll_opy_({
            bstack11111_opy_ (u"ࠪࡩࡻ࡫࡮ࡵࡡࡷࡽࡵ࡫ࠧ⇈"): bstack11111_opy_ (u"ࠫࡈࡈࡔࡔࡧࡶࡷ࡮ࡵ࡮ࡄࡴࡨࡥࡹ࡫ࡤࠨ⇉"),
            bstack11111_opy_ (u"ࠬࡺࡥࡴࡶࡢࡶࡺࡴࠧ⇊"): {
                bstack11111_opy_ (u"ࠨࡵࡶ࡫ࡧࠦ⇋"): cls.current_test_uuid(),
                bstack11111_opy_ (u"ࠢࡪࡰࡷࡩ࡬ࡸࡡࡵ࡫ࡲࡲࡸࠨ⇌"): cls.bstack1l1l1lll_opy_(driver)
            }
        })
    @classmethod
    def bstack11llll1l_opy_(cls, event: str, bstack1l11l111_opy_: bstack1ll11ll1_opy_):
        bstack11lll111_opy_ = {
            bstack11111_opy_ (u"ࠨࡧࡹࡩࡳࡺ࡟ࡵࡻࡳࡩࠬ⇍"): event,
            bstack1l11l111_opy_.event_key(): bstack1l11l111_opy_.bstack1l11111l_opy_(event)
        }
        cls.bstack1ll11lll_opy_(bstack11lll111_opy_)
        result = getattr(bstack1l11l111_opy_, bstack11111_opy_ (u"ࠩࡵࡩࡸࡻ࡬ࡵࠩ⇎"), None)
        if event == bstack11111_opy_ (u"ࠪࡘࡪࡹࡴࡓࡷࡱࡗࡹࡧࡲࡵࡧࡧࠫ⇏"):
            threading.current_thread().bstackTestMeta = {bstack11111_opy_ (u"ࠫࡸࡺࡡࡵࡷࡶࠫ⇐"): bstack11111_opy_ (u"ࠬࡶࡥ࡯ࡦ࡬ࡲ࡬࠭⇑")}
        elif event == bstack11111_opy_ (u"࠭ࡔࡦࡵࡷࡖࡺࡴࡆࡪࡰ࡬ࡷ࡭࡫ࡤࠨ⇒"):
            threading.current_thread().bstackTestMeta = {bstack11111_opy_ (u"ࠧࡴࡶࡤࡸࡺࡹࠧ⇓"): getattr(result, bstack11111_opy_ (u"ࠨࡴࡨࡷࡺࡲࡴࠨ⇔"), bstack11111_opy_ (u"ࠩࠪ⇕"))}
    @classmethod
    def on(cls):
        if (os.environ.get(bstack11111_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚ࡈࡖࡄࡢࡎ࡜࡚ࠧ⇖"), None) is None or os.environ[bstack11111_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡉࡗࡅࡣࡏ࡝ࡔࠨ⇗")] == bstack11111_opy_ (u"ࠧࡴࡵ࡭࡮ࠥ⇘")) and (os.environ.get(bstack11111_opy_ (u"࠭ࡂࡔࡡࡄ࠵࠶࡟࡟ࡋ࡙ࡗࠫ⇙"), None) is None or os.environ[bstack11111_opy_ (u"ࠧࡃࡕࡢࡅ࠶࠷࡙ࡠࡌ࡚ࡘࠬ⇚")] == bstack11111_opy_ (u"ࠣࡰࡸࡰࡱࠨ⇛")):
            return False
        return True
    @staticmethod
    def bstack1llll1l1l111_opy_(func):
        def wrap(*args, **kwargs):
            if bstack1l11lll1_opy_.on():
                return func(*args, **kwargs)
            return
        return wrap
    @staticmethod
    def default_headers():
        headers = {
            bstack11111_opy_ (u"ࠩࡆࡳࡳࡺࡥ࡯ࡶ࠰ࡘࡾࡶࡥࠨ⇜"): bstack11111_opy_ (u"ࠪࡥࡵࡶ࡬ࡪࡥࡤࡸ࡮ࡵ࡮࠰࡬ࡶࡳࡳ࠭⇝"),
            bstack11111_opy_ (u"ࠫ࡝࠳ࡂࡔࡖࡄࡇࡐ࠳ࡔࡆࡕࡗࡓࡕ࡙ࠧ⇞"): bstack11111_opy_ (u"ࠬࡺࡲࡶࡧࠪ⇟")
        }
        if os.environ.get(bstack11111_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡊࡘࡖࠪ⇠"), None):
            headers[bstack11111_opy_ (u"ࠧࡂࡷࡷ࡬ࡴࡸࡩࡻࡣࡷ࡭ࡴࡴࠧ⇡")] = bstack11111_opy_ (u"ࠨࡄࡨࡥࡷ࡫ࡲࠡࡽࢀࠫ⇢").format(os.environ[bstack11111_opy_ (u"ࠤࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡎࡕࡃࡡࡍ࡛࡙ࠨ⇣")])
        return headers
    @staticmethod
    def request_url(url):
        return bstack11111_opy_ (u"ࠪࡿࢂ࠵ࡻࡾࠩ⇤").format(bstack1llll11llll1_opy_, url)
    @staticmethod
    def current_test_uuid():
        return getattr(threading.current_thread(), bstack11111_opy_ (u"ࠫࡨࡻࡲࡳࡧࡱࡸࡤࡺࡥࡴࡶࡢࡹࡺ࡯ࡤࠨ⇥"), None)
    @staticmethod
    def bstack1l1l1lll_opy_(driver):
        return {
            bstack111l1l1111l_opy_(): bstack1111ll1llll_opy_(driver)
        }
    @staticmethod
    def bstack1llll1l1lll1_opy_(exception_info, report):
        return [{bstack11111_opy_ (u"ࠬࡨࡡࡤ࡭ࡷࡶࡦࡩࡥࠨ⇦"): [exception_info.exconly(), report.longreprtext]}]
    @staticmethod
    def bstack111111lll1_opy_(typename):
        if bstack11111_opy_ (u"ࠨࡁࡴࡵࡨࡶࡹ࡯࡯࡯ࠤ⇧") in typename:
            return bstack11111_opy_ (u"ࠢࡂࡵࡶࡩࡷࡺࡩࡰࡰࡈࡶࡷࡵࡲࠣ⇨")
        return bstack11111_opy_ (u"ࠣࡗࡱ࡬ࡦࡴࡤ࡭ࡧࡧࡉࡷࡸ࡯ࡳࠤ⇩")