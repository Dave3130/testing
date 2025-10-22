# coding: UTF-8
import sys
bstack1l111_opy_ = sys.version_info [0] == 2
bstack11l111_opy_ = 2048
bstack1l1l_opy_ = 7
def bstack1l111ll_opy_ (bstack1llllll1_opy_):
    global bstack111l1l1_opy_
    bstack1lll111_opy_ = ord (bstack1llllll1_opy_ [-1])
    bstack1ll11l1_opy_ = bstack1llllll1_opy_ [:-1]
    bstack1l11lll_opy_ = bstack1lll111_opy_ % len (bstack1ll11l1_opy_)
    bstack11l1l1_opy_ = bstack1ll11l1_opy_ [:bstack1l11lll_opy_] + bstack1ll11l1_opy_ [bstack1l11lll_opy_:]
    if bstack1l111_opy_:
        bstack11l11l_opy_ = unicode () .join ([unichr (ord (char) - bstack11l111_opy_ - (bstack11l1l1l_opy_ + bstack1lll111_opy_) % bstack1l1l_opy_) for bstack11l1l1l_opy_, char in enumerate (bstack11l1l1_opy_)])
    else:
        bstack11l11l_opy_ = str () .join ([chr (ord (char) - bstack11l111_opy_ - (bstack11l1l1l_opy_ + bstack1lll111_opy_) % bstack1l1l_opy_) for bstack11l1l1l_opy_, char in enumerate (bstack11l1l1_opy_)])
    return eval (bstack11l11l_opy_)
import json
import logging
import os
import datetime
import threading
from bstack_utils.constants import EVENTS, STAGE
from bstack_utils.helper import bstack1111l1ll1ll_opy_, bstack111l11ll11l_opy_, bstack11l1lllll1_opy_, error_handler, bstack111l1ll1lll_opy_, bstack1111l1l1111_opy_, bstack111l1l11lll_opy_, bstack1ll11lll_opy_, bstack1l1111ll_opy_
from bstack_utils.measure import measure
from bstack_utils.bstack11l111lllll_opy_ import bstack111l1llll1l_opy_
import bstack_utils.bstack1ll1ll1ll1_opy_ as bstack1l1111llll_opy_
from bstack_utils.bstack1l1l1l11_opy_ import bstack1l11llll_opy_
import bstack_utils.accessibility as bstack11111111_opy_
from bstack_utils.bstack1ll11l1ll_opy_ import bstack1ll11l1ll_opy_
from bstack_utils.bstack1lll1111_opy_ import bstack11lll1l1_opy_
from bstack_utils.constants import bstack1ll11ll11l_opy_
bstack1llll1l111ll_opy_ = bstack1l111ll_opy_ (u"ࠫ࡭ࡺࡴࡱࡵ࠽࠳࠴ࡩ࡯࡭࡮ࡨࡧࡹࡵࡲ࠮ࡱࡥࡷࡪࡸࡶࡢࡤ࡬ࡰ࡮ࡺࡹ࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡤࡱࡰࠫℚ")
logger = logging.getLogger(__name__)
class bstack1lll1l11_opy_:
    bstack11l111lllll_opy_ = None
    bs_config = None
    bstack11l11ll111_opy_ = None
    @classmethod
    @error_handler(class_method=True)
    @measure(event_name=EVENTS.bstack11l1l1111l1_opy_, stage=STAGE.bstack1ll11l111l_opy_)
    def launch(cls, bs_config, bstack11l11ll111_opy_):
        cls.bs_config = bs_config
        cls.bstack11l11ll111_opy_ = bstack11l11ll111_opy_
        try:
            cls.bstack1llll11l1111_opy_()
            bstack1llll1ll1l11_opy_ = bstack1111l1ll1ll_opy_(bs_config)
            bstack1llll1l1l111_opy_ = bstack111l11ll11l_opy_(bs_config)
            data = bstack1l1111llll_opy_.bstack1llll11lll11_opy_(bs_config, bstack11l11ll111_opy_)
            config = {
                bstack1l111ll_opy_ (u"ࠬࡧࡵࡵࡪࠪℛ"): (bstack1llll1ll1l11_opy_, bstack1llll1l1l111_opy_),
                bstack1l111ll_opy_ (u"࠭ࡨࡦࡣࡧࡩࡷࡹࠧℜ"): cls.default_headers()
            }
            response = bstack11l1lllll1_opy_(bstack1l111ll_opy_ (u"ࠧࡑࡑࡖࡘࠬℝ"), cls.request_url(bstack1l111ll_opy_ (u"ࠨࡣࡳ࡭࠴ࡼ࠲࠰ࡤࡸ࡭ࡱࡪࡳࠨ℞")), data, config)
            if response.status_code != 200:
                bstack111l1ll11l_opy_ = response.json()
                if bstack111l1ll11l_opy_[bstack1l111ll_opy_ (u"ࠩࡶࡹࡨࡩࡥࡴࡵࠪ℟")] == False:
                    cls.bstack1llll111llll_opy_(bstack111l1ll11l_opy_)
                    return
                cls.bstack1llll11ll1ll_opy_(bstack111l1ll11l_opy_[bstack1l111ll_opy_ (u"ࠪࡳࡧࡹࡥࡳࡸࡤࡦ࡮ࡲࡩࡵࡻࠪ℠")])
                cls.bstack1llll11l1l1l_opy_(bstack111l1ll11l_opy_[bstack1l111ll_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠫ℡")])
                return None
            bstack1llll1l11111_opy_ = cls.bstack1llll11l11l1_opy_(response)
            return bstack1llll1l11111_opy_, response.json()
        except Exception as error:
            logger.error(bstack1l111ll_opy_ (u"ࠧࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡࡹ࡫࡭ࡱ࡫ࠠࡤࡴࡨࡥࡹ࡯࡮ࡨࠢࡥࡹ࡮ࡲࡤࠡࡨࡲࡶ࡚ࠥࡥࡴࡶࡋࡹࡧࡀࠠࡼࡿࠥ™").format(str(error)))
            return None
    @classmethod
    @error_handler(class_method=True)
    def stop(cls, bstack1llll11llll1_opy_=None):
        if not bstack1l11llll_opy_.on() and not bstack11111111_opy_.on():
            return
        if os.environ.get(bstack1l111ll_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡊࡘࡖࠪ℣")) == bstack1l111ll_opy_ (u"ࠢ࡯ࡷ࡯ࡰࠧℤ") or os.environ.get(bstack1l111ll_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡍ࡛ࡂࡠࡗࡘࡍࡉ࠭℥")) == bstack1l111ll_opy_ (u"ࠤࡱࡹࡱࡲࠢΩ"):
            logger.error(bstack1l111ll_opy_ (u"ࠪࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩ࡯ࠢࡶࡸࡴࡶࠠࡣࡷ࡬ࡰࡩࠦࡲࡦࡳࡸࡩࡸࡺࠠࡵࡱࠣࡘࡪࡹࡴࡉࡷࡥ࠾ࠥࡓࡩࡴࡵ࡬ࡲ࡬ࠦࡡࡶࡶ࡫ࡩࡳࡺࡩࡤࡣࡷ࡭ࡴࡴࠠࡵࡱ࡮ࡩࡳ࠭℧"))
            return {
                bstack1l111ll_opy_ (u"ࠫࡸࡺࡡࡵࡷࡶࠫℨ"): bstack1l111ll_opy_ (u"ࠬ࡫ࡲࡳࡱࡵࠫ℩"),
                bstack1l111ll_opy_ (u"࠭࡭ࡦࡵࡶࡥ࡬࡫ࠧK"): bstack1l111ll_opy_ (u"ࠧࡕࡱ࡮ࡩࡳ࠵ࡢࡶ࡫࡯ࡨࡎࡊࠠࡪࡵࠣࡹࡳࡪࡥࡧ࡫ࡱࡩࡩ࠲ࠠࡣࡷ࡬ࡰࡩࠦࡣࡳࡧࡤࡸ࡮ࡵ࡮ࠡ࡯࡬࡫࡭ࡺࠠࡩࡣࡹࡩࠥ࡬ࡡࡪ࡮ࡨࡨࠬÅ")
            }
        try:
            cls.bstack11l111lllll_opy_.shutdown()
            data = {
                bstack1l111ll_opy_ (u"ࠨࡨ࡬ࡲ࡮ࡹࡨࡦࡦࡢࡥࡹ࠭ℬ"): bstack1ll11lll_opy_()
            }
            if not bstack1llll11llll1_opy_ is None:
                data[bstack1l111ll_opy_ (u"ࠩࡩ࡭ࡳ࡯ࡳࡩࡧࡧࡣࡲ࡫ࡴࡢࡦࡤࡸࡦ࠭ℭ")] = [{
                    bstack1l111ll_opy_ (u"ࠪࡶࡪࡧࡳࡰࡰࠪ℮"): bstack1l111ll_opy_ (u"ࠫࡺࡹࡥࡳࡡ࡮࡭ࡱࡲࡥࡥࠩℯ"),
                    bstack1l111ll_opy_ (u"ࠬࡹࡩࡨࡰࡤࡰࠬℰ"): bstack1llll11llll1_opy_
                }]
            config = {
                bstack1l111ll_opy_ (u"࠭ࡨࡦࡣࡧࡩࡷࡹࠧℱ"): cls.default_headers()
            }
            bstack11ll111ll11_opy_ = bstack1l111ll_opy_ (u"ࠧࡢࡲ࡬࠳ࡻ࠷࠯ࡣࡷ࡬ࡰࡩࡹ࠯ࡼࡿ࠲ࡷࡹࡵࡰࠨℲ").format(os.environ[bstack1l111ll_opy_ (u"ࠣࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡍ࡛ࡂࡠࡗࡘࡍࡉࠨℳ")])
            bstack1llll11l1ll1_opy_ = cls.request_url(bstack11ll111ll11_opy_)
            response = bstack11l1lllll1_opy_(bstack1l111ll_opy_ (u"ࠩࡓ࡙࡙࠭ℴ"), bstack1llll11l1ll1_opy_, data, config)
            if not response.ok:
                raise Exception(bstack1l111ll_opy_ (u"ࠥࡗࡹࡵࡰࠡࡴࡨࡵࡺ࡫ࡳࡵࠢࡱࡳࡹࠦ࡯࡬ࠤℵ"))
        except Exception as error:
            logger.error(bstack1l111ll_opy_ (u"ࠦࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣࡷࡹࡵࡰࠡࡤࡸ࡭ࡱࡪࠠࡳࡧࡴࡹࡪࡹࡴࠡࡶࡲࠤ࡙࡫ࡳࡵࡊࡸࡦ࠿ࡀࠠࠣℶ") + str(error))
            return {
                bstack1l111ll_opy_ (u"ࠬࡹࡴࡢࡶࡸࡷࠬℷ"): bstack1l111ll_opy_ (u"࠭ࡥࡳࡴࡲࡶࠬℸ"),
                bstack1l111ll_opy_ (u"ࠧ࡮ࡧࡶࡷࡦ࡭ࡥࠨℹ"): str(error)
            }
    @classmethod
    @error_handler(class_method=True)
    def bstack1llll11l11l1_opy_(cls, response):
        bstack111l1ll11l_opy_ = response.json() if not isinstance(response, dict) else response
        bstack1llll1l11111_opy_ = {}
        if bstack111l1ll11l_opy_.get(bstack1l111ll_opy_ (u"ࠨ࡬ࡺࡸࠬ℺")) is None:
            os.environ[bstack1l111ll_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡎࡕࡃࡡࡍ࡛࡙࠭℻")] = bstack1l111ll_opy_ (u"ࠪࡲࡺࡲ࡬ࠨℼ")
        else:
            os.environ[bstack1l111ll_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡉࡗࡅࡣࡏ࡝ࡔࠨℽ")] = bstack111l1ll11l_opy_.get(bstack1l111ll_opy_ (u"ࠬࡰࡷࡵࠩℾ"), bstack1l111ll_opy_ (u"࠭࡮ࡶ࡮࡯ࠫℿ"))
        os.environ[bstack1l111ll_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡖࡗࡌࡈࠬ⅀")] = bstack111l1ll11l_opy_.get(bstack1l111ll_opy_ (u"ࠨࡤࡸ࡭ࡱࡪ࡟ࡩࡣࡶ࡬ࡪࡪ࡟ࡪࡦࠪ⅁"), bstack1l111ll_opy_ (u"ࠩࡱࡹࡱࡲࠧ⅂"))
        logger.info(bstack1l111ll_opy_ (u"ࠪࡘࡪࡹࡴࡩࡷࡥࠤࡸࡺࡡࡳࡶࡨࡨࠥࡽࡩࡵࡪࠣ࡭ࡩࡀࠠࠨ⅃") + os.getenv(bstack1l111ll_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡉࡗࡅࡣ࡚࡛ࡉࡅࠩ⅄")));
        if bstack1l11llll_opy_.bstack11l11l11111_opy_(cls.bs_config, cls.bstack11l11ll111_opy_.get(bstack1l111ll_opy_ (u"ࠬ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡷࡶࡩࡩ࠭ⅅ"), bstack1l111ll_opy_ (u"࠭ࠧⅆ"))) is True:
            bstack11ll111l1l1_opy_, build_hashed_id, bstack1llll11l1l11_opy_ = cls.bstack1llll11l11ll_opy_(bstack111l1ll11l_opy_)
            if bstack11ll111l1l1_opy_ != None and build_hashed_id != None:
                bstack1llll1l11111_opy_[bstack1l111ll_opy_ (u"ࠧࡰࡤࡶࡩࡷࡼࡡࡣ࡫࡯࡭ࡹࡿࠧⅇ")] = {
                    bstack1l111ll_opy_ (u"ࠨ࡬ࡺࡸࡤࡺ࡯࡬ࡧࡱࠫⅈ"): bstack11ll111l1l1_opy_,
                    bstack1l111ll_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡠࡪࡤࡷ࡭࡫ࡤࡠ࡫ࡧࠫⅉ"): build_hashed_id,
                    bstack1l111ll_opy_ (u"ࠪࡥࡱࡲ࡯ࡸࡡࡶࡧࡷ࡫ࡥ࡯ࡵ࡫ࡳࡹࡹࠧ⅊"): bstack1llll11l1l11_opy_
                }
            else:
                bstack1llll1l11111_opy_[bstack1l111ll_opy_ (u"ࠫࡴࡨࡳࡦࡴࡹࡥࡧ࡯࡬ࡪࡶࡼࠫ⅋")] = {}
        else:
            bstack1llll1l11111_opy_[bstack1l111ll_opy_ (u"ࠬࡵࡢࡴࡧࡵࡺࡦࡨࡩ࡭࡫ࡷࡽࠬ⅌")] = {}
        bstack1llll1l111l1_opy_, build_hashed_id = cls.bstack1llll11ll1l1_opy_(bstack111l1ll11l_opy_)
        if bstack1llll1l111l1_opy_ != None and build_hashed_id != None:
            bstack1llll1l11111_opy_[bstack1l111ll_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾ࠭⅍")] = {
                bstack1l111ll_opy_ (u"ࠧࡢࡷࡷ࡬ࡤࡺ࡯࡬ࡧࡱࠫⅎ"): bstack1llll1l111l1_opy_,
                bstack1l111ll_opy_ (u"ࠨࡤࡸ࡭ࡱࡪ࡟ࡩࡣࡶ࡬ࡪࡪ࡟ࡪࡦࠪ⅏"): build_hashed_id,
            }
        else:
            bstack1llll1l11111_opy_[bstack1l111ll_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠩ⅐")] = {}
        if bstack1llll1l11111_opy_[bstack1l111ll_opy_ (u"ࠪࡳࡧࡹࡥࡳࡸࡤࡦ࡮ࡲࡩࡵࡻࠪ⅑")].get(bstack1l111ll_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡢ࡬ࡦࡹࡨࡦࡦࡢ࡭ࡩ࠭⅒")) != None or bstack1llll1l11111_opy_[bstack1l111ll_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠬ⅓")].get(bstack1l111ll_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡤ࡮ࡡࡴࡪࡨࡨࡤ࡯ࡤࠨ⅔")) != None:
            cls.bstack1llll11lll1l_opy_(bstack111l1ll11l_opy_.get(bstack1l111ll_opy_ (u"ࠧ࡫ࡹࡷࠫ⅕")), bstack111l1ll11l_opy_.get(bstack1l111ll_opy_ (u"ࠨࡤࡸ࡭ࡱࡪ࡟ࡩࡣࡶ࡬ࡪࡪ࡟ࡪࡦࠪ⅖")))
        return bstack1llll1l11111_opy_
    @classmethod
    def bstack1llll11l11ll_opy_(cls, bstack111l1ll11l_opy_):
        if bstack111l1ll11l_opy_.get(bstack1l111ll_opy_ (u"ࠩࡲࡦࡸ࡫ࡲࡷࡣࡥ࡭ࡱ࡯ࡴࡺࠩ⅗")) == None:
            cls.bstack1llll11ll1ll_opy_()
            return [None, None, None]
        if bstack111l1ll11l_opy_[bstack1l111ll_opy_ (u"ࠪࡳࡧࡹࡥࡳࡸࡤࡦ࡮ࡲࡩࡵࡻࠪ⅘")][bstack1l111ll_opy_ (u"ࠫࡸࡻࡣࡤࡧࡶࡷࠬ⅙")] != True:
            cls.bstack1llll11ll1ll_opy_(bstack111l1ll11l_opy_[bstack1l111ll_opy_ (u"ࠬࡵࡢࡴࡧࡵࡺࡦࡨࡩ࡭࡫ࡷࡽࠬ⅚")])
            return [None, None, None]
        logger.debug(bstack1l111ll_opy_ (u"࠭ࡻࡾࠢࡅࡹ࡮ࡲࡤࠡࡥࡵࡩࡦࡺࡩࡰࡰࠣࡗࡺࡩࡣࡦࡵࡶࡪࡺࡲࠡࠨ⅛").format(bstack1ll11ll11l_opy_))
        os.environ[bstack1l111ll_opy_ (u"ࠧࡃࡕࡢࡘࡊ࡙ࡔࡐࡒࡖࡣࡇ࡛ࡉࡍࡆࡢࡇࡔࡓࡐࡍࡇࡗࡉࡉ࠭⅜")] = bstack1l111ll_opy_ (u"ࠨࡶࡵࡹࡪ࠭⅝")
        if bstack111l1ll11l_opy_.get(bstack1l111ll_opy_ (u"ࠩ࡭ࡻࡹ࠭⅞")):
            os.environ[bstack1l111ll_opy_ (u"ࠪࡇࡗࡋࡄࡆࡐࡗࡍࡆࡒࡓࡠࡈࡒࡖࡤࡉࡒࡂࡕࡋࡣࡗࡋࡐࡐࡔࡗࡍࡓࡍࠧ⅟")] = json.dumps({
                bstack1l111ll_opy_ (u"ࠫࡺࡹࡥࡳࡰࡤࡱࡪ࠭Ⅰ"): bstack1111l1ll1ll_opy_(cls.bs_config),
                bstack1l111ll_opy_ (u"ࠬࡶࡡࡴࡵࡺࡳࡷࡪࠧⅡ"): bstack111l11ll11l_opy_(cls.bs_config)
            })
        if bstack111l1ll11l_opy_.get(bstack1l111ll_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡤ࡮ࡡࡴࡪࡨࡨࡤ࡯ࡤࠨⅢ")):
            os.environ[bstack1l111ll_opy_ (u"ࠧࡃࡕࡢࡘࡊ࡙ࡔࡐࡒࡖࡣࡇ࡛ࡉࡍࡆࡢࡌࡆ࡙ࡈࡆࡆࡢࡍࡉ࠭Ⅳ")] = bstack111l1ll11l_opy_[bstack1l111ll_opy_ (u"ࠨࡤࡸ࡭ࡱࡪ࡟ࡩࡣࡶ࡬ࡪࡪ࡟ࡪࡦࠪⅤ")]
        if bstack111l1ll11l_opy_[bstack1l111ll_opy_ (u"ࠩࡲࡦࡸ࡫ࡲࡷࡣࡥ࡭ࡱ࡯ࡴࡺࠩⅥ")].get(bstack1l111ll_opy_ (u"ࠪࡳࡵࡺࡩࡰࡰࡶࠫⅦ"), {}).get(bstack1l111ll_opy_ (u"ࠫࡦࡲ࡬ࡰࡹࡢࡷࡨࡸࡥࡦࡰࡶ࡬ࡴࡺࡳࠨⅧ")):
            os.environ[bstack1l111ll_opy_ (u"ࠬࡈࡓࡠࡖࡈࡗ࡙ࡕࡐࡔࡡࡄࡐࡑࡕࡗࡠࡕࡆࡖࡊࡋࡎࡔࡊࡒࡘࡘ࠭Ⅸ")] = str(bstack111l1ll11l_opy_[bstack1l111ll_opy_ (u"࠭࡯ࡣࡵࡨࡶࡻࡧࡢࡪ࡮࡬ࡸࡾ࠭Ⅹ")][bstack1l111ll_opy_ (u"ࠧࡰࡲࡷ࡭ࡴࡴࡳࠨⅪ")][bstack1l111ll_opy_ (u"ࠨࡣ࡯ࡰࡴࡽ࡟ࡴࡥࡵࡩࡪࡴࡳࡩࡱࡷࡷࠬⅫ")])
        else:
            os.environ[bstack1l111ll_opy_ (u"ࠩࡅࡗࡤ࡚ࡅࡔࡖࡒࡔࡘࡥࡁࡍࡎࡒ࡛ࡤ࡙ࡃࡓࡇࡈࡒࡘࡎࡏࡕࡕࠪⅬ")] = bstack1l111ll_opy_ (u"ࠥࡲࡺࡲ࡬ࠣⅭ")
        return [bstack111l1ll11l_opy_[bstack1l111ll_opy_ (u"ࠫ࡯ࡽࡴࠨⅮ")], bstack111l1ll11l_opy_[bstack1l111ll_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡣ࡭ࡧࡳࡩࡧࡧࡣ࡮ࡪࠧⅯ")], os.environ[bstack1l111ll_opy_ (u"࠭ࡂࡔࡡࡗࡉࡘ࡚ࡏࡑࡕࡢࡅࡑࡒࡏࡘࡡࡖࡇࡗࡋࡅࡏࡕࡋࡓ࡙࡙ࠧⅰ")]]
    @classmethod
    def bstack1llll11ll1l1_opy_(cls, bstack111l1ll11l_opy_):
        if bstack111l1ll11l_opy_.get(bstack1l111ll_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠧⅱ")) == None:
            cls.bstack1llll11l1l1l_opy_()
            return [None, None]
        if bstack111l1ll11l_opy_[bstack1l111ll_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠨⅲ")][bstack1l111ll_opy_ (u"ࠩࡶࡹࡨࡩࡥࡴࡵࠪⅳ")] != True:
            cls.bstack1llll11l1l1l_opy_(bstack111l1ll11l_opy_[bstack1l111ll_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠪⅴ")])
            return [None, None]
        if bstack111l1ll11l_opy_[bstack1l111ll_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠫⅵ")].get(bstack1l111ll_opy_ (u"ࠬࡵࡰࡵ࡫ࡲࡲࡸ࠭ⅶ")):
            logger.debug(bstack1l111ll_opy_ (u"࠭ࡔࡦࡵࡷࠤࡆࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡇࡻࡩ࡭ࡦࠣࡧࡷ࡫ࡡࡵ࡫ࡲࡲ࡙ࠥࡵࡤࡥࡨࡷࡸ࡬ࡵ࡭ࠣࠪⅷ"))
            parsed = json.loads(os.getenv(bstack1l111ll_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡣࡆࡉࡃࡆࡕࡖࡍࡇࡏࡌࡊࡖ࡜ࡣࡈࡕࡎࡇࡋࡊ࡙ࡗࡇࡔࡊࡑࡑࡣ࡞ࡓࡌࠨⅸ"), bstack1l111ll_opy_ (u"ࠨࡽࢀࠫⅹ")))
            capabilities = bstack1l1111llll_opy_.bstack1llll11ll111_opy_(bstack111l1ll11l_opy_[bstack1l111ll_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠩⅺ")][bstack1l111ll_opy_ (u"ࠪࡳࡵࡺࡩࡰࡰࡶࠫⅻ")][bstack1l111ll_opy_ (u"ࠫࡨࡧࡰࡢࡤ࡬ࡰ࡮ࡺࡩࡦࡵࠪⅼ")], bstack1l111ll_opy_ (u"ࠬࡴࡡ࡮ࡧࠪⅽ"), bstack1l111ll_opy_ (u"࠭ࡶࡢ࡮ࡸࡩࠬⅾ"))
            bstack1llll1l111l1_opy_ = capabilities[bstack1l111ll_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࡔࡰ࡭ࡨࡲࠬⅿ")]
            os.environ[bstack1l111ll_opy_ (u"ࠨࡄࡖࡣࡆ࠷࠱࡚ࡡࡍ࡛࡙࠭ↀ")] = bstack1llll1l111l1_opy_
            if bstack1l111ll_opy_ (u"ࠤࡤࡹࡹࡵ࡭ࡢࡶࡨࠦↁ") in bstack111l1ll11l_opy_ and bstack111l1ll11l_opy_.get(bstack1l111ll_opy_ (u"ࠥࡥࡵࡶ࡟ࡢࡷࡷࡳࡲࡧࡴࡦࠤↂ")) is None:
                parsed[bstack1l111ll_opy_ (u"ࠫࡸࡩࡡ࡯ࡰࡨࡶ࡛࡫ࡲࡴ࡫ࡲࡲࠬↃ")] = capabilities[bstack1l111ll_opy_ (u"ࠬࡹࡣࡢࡰࡱࡩࡷ࡜ࡥࡳࡵ࡬ࡳࡳ࠭ↄ")]
            os.environ[bstack1l111ll_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡢࡅࡈࡉࡅࡔࡕࡌࡆࡎࡒࡉࡕ࡛ࡢࡇࡔࡔࡆࡊࡉࡘࡖࡆ࡚ࡉࡐࡐࡢ࡝ࡒࡒࠧↅ")] = json.dumps(parsed)
            scripts = bstack1l1111llll_opy_.bstack1llll11ll111_opy_(bstack111l1ll11l_opy_[bstack1l111ll_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠧↆ")][bstack1l111ll_opy_ (u"ࠨࡱࡳࡸ࡮ࡵ࡮ࡴࠩↇ")][bstack1l111ll_opy_ (u"ࠩࡶࡧࡷ࡯ࡰࡵࡵࠪↈ")], bstack1l111ll_opy_ (u"ࠪࡲࡦࡳࡥࠨ↉"), bstack1l111ll_opy_ (u"ࠫࡨࡵ࡭࡮ࡣࡱࡨࠬ↊"))
            bstack1ll11l1ll_opy_.bstack11l1l1lll_opy_(scripts)
            commands = bstack111l1ll11l_opy_[bstack1l111ll_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠬ↋")][bstack1l111ll_opy_ (u"࠭࡯ࡱࡶ࡬ࡳࡳࡹࠧ↌")][bstack1l111ll_opy_ (u"ࠧࡤࡱࡰࡱࡦࡴࡤࡴࡖࡲ࡛ࡷࡧࡰࠨ↍")].get(bstack1l111ll_opy_ (u"ࠨࡥࡲࡱࡲࡧ࡮ࡥࡵࠪ↎"))
            bstack1ll11l1ll_opy_.bstack1lllll1111ll_opy_(commands)
            bstack1lllll111lll_opy_ = capabilities.get(bstack1l111ll_opy_ (u"ࠩࡪࡳࡴ࡭࠺ࡤࡪࡵࡳࡲ࡫ࡏࡱࡶ࡬ࡳࡳࡹࠧ↏"))
            bstack1ll11l1ll_opy_.bstack1lllll11l111_opy_(bstack1lllll111lll_opy_)
            bstack1ll11l1ll_opy_.store()
        return [bstack1llll1l111l1_opy_, bstack111l1ll11l_opy_[bstack1l111ll_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡡ࡫ࡥࡸ࡮ࡥࡥࡡ࡬ࡨࠬ←")]]
    @classmethod
    def bstack1llll11ll1ll_opy_(cls, response=None):
        os.environ[bstack1l111ll_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡉࡗࡅࡣ࡚࡛ࡉࡅࠩ↑")] = bstack1l111ll_opy_ (u"ࠬࡴࡵ࡭࡮ࠪ→")
        os.environ[bstack1l111ll_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡊࡘࡖࠪ↓")] = bstack1l111ll_opy_ (u"ࠧ࡯ࡷ࡯ࡰࠬ↔")
        os.environ[bstack1l111ll_opy_ (u"ࠨࡄࡖࡣ࡙ࡋࡓࡕࡑࡓࡗࡤࡈࡕࡊࡎࡇࡣࡈࡕࡍࡑࡎࡈࡘࡊࡊࠧ↕")] = bstack1l111ll_opy_ (u"ࠩࡩࡥࡱࡹࡥࠨ↖")
        os.environ[bstack1l111ll_opy_ (u"ࠪࡆࡘࡥࡔࡆࡕࡗࡓࡕ࡙࡟ࡃࡗࡌࡐࡉࡥࡈࡂࡕࡋࡉࡉࡥࡉࡅࠩ↗")] = bstack1l111ll_opy_ (u"ࠦࡳࡻ࡬࡭ࠤ↘")
        os.environ[bstack1l111ll_opy_ (u"ࠬࡈࡓࡠࡖࡈࡗ࡙ࡕࡐࡔࡡࡄࡐࡑࡕࡗࡠࡕࡆࡖࡊࡋࡎࡔࡊࡒࡘࡘ࠭↙")] = bstack1l111ll_opy_ (u"ࠨ࡮ࡶ࡮࡯ࠦ↚")
        cls.bstack1llll111llll_opy_(response, bstack1l111ll_opy_ (u"ࠢࡰࡤࡶࡩࡷࡼࡡࡣ࡫࡯࡭ࡹࡿࠢ↛"))
        return [None, None, None]
    @classmethod
    def bstack1llll11l1l1l_opy_(cls, response=None):
        os.environ[bstack1l111ll_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡍ࡛ࡂࡠࡗࡘࡍࡉ࠭↜")] = bstack1l111ll_opy_ (u"ࠩࡱࡹࡱࡲࠧ↝")
        os.environ[bstack1l111ll_opy_ (u"ࠪࡆࡘࡥࡁ࠲࠳࡜ࡣࡏ࡝ࡔࠨ↞")] = bstack1l111ll_opy_ (u"ࠫࡳࡻ࡬࡭ࠩ↟")
        os.environ[bstack1l111ll_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡊࡘࡆࡤࡐࡗࡕࠩ↠")] = bstack1l111ll_opy_ (u"࠭࡮ࡶ࡮࡯ࠫ↡")
        cls.bstack1llll111llll_opy_(response, bstack1l111ll_opy_ (u"ࠢࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠢ↢"))
        return [None, None, None]
    @classmethod
    def bstack1llll11lll1l_opy_(cls, jwt, build_hashed_id):
        os.environ[bstack1l111ll_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡍ࡛ࡂࡠࡌ࡚ࡘࠬ↣")] = jwt
        os.environ[bstack1l111ll_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡎࡕࡃࡡࡘ࡙ࡎࡊࠧ↤")] = build_hashed_id
    @classmethod
    def bstack1llll111llll_opy_(cls, response=None, product=bstack1l111ll_opy_ (u"ࠥࠦ↥")):
        if response == None or response.get(bstack1l111ll_opy_ (u"ࠫࡪࡸࡲࡰࡴࡶࠫ↦")) == None:
            logger.error(product + bstack1l111ll_opy_ (u"ࠧࠦࡂࡶ࡫࡯ࡨࠥࡩࡲࡦࡣࡷ࡭ࡴࡴࠠࡧࡣ࡬ࡰࡪࡪࠢ↧"))
            return
        for error in response[bstack1l111ll_opy_ (u"࠭ࡥࡳࡴࡲࡶࡸ࠭↨")]:
            bstack111l11l1l1l_opy_ = error[bstack1l111ll_opy_ (u"ࠧ࡬ࡧࡼࠫ↩")]
            error_message = error[bstack1l111ll_opy_ (u"ࠨ࡯ࡨࡷࡸࡧࡧࡦࠩ↪")]
            if error_message:
                if bstack111l11l1l1l_opy_ == bstack1l111ll_opy_ (u"ࠤࡈࡖࡗࡕࡒࡠࡃࡆࡇࡊ࡙ࡓࡠࡆࡈࡒࡎࡋࡄࠣ↫"):
                    logger.info(error_message)
                else:
                    logger.error(error_message)
            else:
                logger.error(bstack1l111ll_opy_ (u"ࠥࡈࡦࡺࡡࠡࡷࡳࡰࡴࡧࡤࠡࡶࡲࠤࡇࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࠣࠦ↬") + product + bstack1l111ll_opy_ (u"ࠦࠥ࡬ࡡࡪ࡮ࡨࡨࠥࡪࡵࡦࠢࡷࡳࠥࡹ࡯࡮ࡧࠣࡩࡷࡸ࡯ࡳࠤ↭"))
    @classmethod
    def bstack1llll11l1111_opy_(cls):
        if cls.bstack11l111lllll_opy_ is not None:
            return
        cls.bstack11l111lllll_opy_ = bstack111l1llll1l_opy_(cls.post_data)
        cls.bstack11l111lllll_opy_.start()
    @classmethod
    def bstack11llllll_opy_(cls):
        if cls.bstack11l111lllll_opy_ is None:
            return
        cls.bstack11l111lllll_opy_.shutdown()
    @classmethod
    @error_handler(class_method=True)
    def post_data(cls, bstack1l111lll_opy_, event_url=bstack1l111ll_opy_ (u"ࠬࡧࡰࡪ࠱ࡹ࠵࠴ࡨࡡࡵࡥ࡫ࠫ↮")):
        config = {
            bstack1l111ll_opy_ (u"࠭ࡨࡦࡣࡧࡩࡷࡹࠧ↯"): cls.default_headers()
        }
        logger.debug(bstack1l111ll_opy_ (u"ࠢࡱࡱࡶࡸࡤࡪࡡࡵࡣ࠽ࠤࡘ࡫࡮ࡥ࡫ࡱ࡫ࠥࡪࡡࡵࡣࠣࡸࡴࠦࡴࡦࡵࡷ࡬ࡺࡨࠠࡧࡱࡵࠤࡪࡼࡥ࡯ࡶࡶࠤࢀࢃࠢ↰").format(bstack1l111ll_opy_ (u"ࠨ࠮ࠣࠫ↱").join([event[bstack1l111ll_opy_ (u"ࠩࡨࡺࡪࡴࡴࡠࡶࡼࡴࡪ࠭↲")] for event in bstack1l111lll_opy_])))
        response = bstack11l1lllll1_opy_(bstack1l111ll_opy_ (u"ࠪࡔࡔ࡙ࡔࠨ↳"), cls.request_url(event_url), bstack1l111lll_opy_, config)
        bstack1llll1l11ll1_opy_ = response.json()
    @classmethod
    def bstack1lll11l1_opy_(cls, bstack1l111lll_opy_, event_url=bstack1l111ll_opy_ (u"ࠫࡦࡶࡩ࠰ࡸ࠴࠳ࡧࡧࡴࡤࡪࠪ↴")):
        logger.debug(bstack1l111ll_opy_ (u"ࠧࡹࡥ࡯ࡦࡢࡨࡦࡺࡡ࠻ࠢࡄࡸࡹ࡫࡭ࡱࡶ࡬ࡲ࡬ࠦࡴࡰࠢࡤࡨࡩࠦࡤࡢࡶࡤࠤࡹࡵࠠࡣࡣࡷࡧ࡭ࠦࡷࡪࡶ࡫ࠤࡪࡼࡥ࡯ࡶࡢࡸࡾࡶࡥ࠻ࠢࡾࢁࠧ↵").format(bstack1l111lll_opy_[bstack1l111ll_opy_ (u"࠭ࡥࡷࡧࡱࡸࡤࡺࡹࡱࡧࠪ↶")]))
        if not bstack1l1111llll_opy_.bstack1llll11l1lll_opy_(bstack1l111lll_opy_[bstack1l111ll_opy_ (u"ࠧࡦࡸࡨࡲࡹࡥࡴࡺࡲࡨࠫ↷")]):
            logger.debug(bstack1l111ll_opy_ (u"ࠣࡵࡨࡲࡩࡥࡤࡢࡶࡤ࠾ࠥࡔ࡯ࡵࠢࡤࡨࡩ࡯࡮ࡨࠢࡧࡥࡹࡧࠠࡸ࡫ࡷ࡬ࠥ࡫ࡶࡦࡰࡷࡣࡹࡿࡰࡦ࠼ࠣࡿࢂࠨ↸").format(bstack1l111lll_opy_[bstack1l111ll_opy_ (u"ࠩࡨࡺࡪࡴࡴࡠࡶࡼࡴࡪ࠭↹")]))
            return
        bstack11lll1l11l_opy_ = bstack1l1111llll_opy_.bstack1llll1l11l11_opy_(bstack1l111lll_opy_[bstack1l111ll_opy_ (u"ࠪࡩࡻ࡫࡮ࡵࡡࡷࡽࡵ࡫ࠧ↺")], bstack1l111lll_opy_.get(bstack1l111ll_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡵࡹࡳ࠭↻")))
        if bstack11lll1l11l_opy_ != None:
            if bstack1l111lll_opy_.get(bstack1l111ll_opy_ (u"ࠬࡺࡥࡴࡶࡢࡶࡺࡴࠧ↼")) != None:
                bstack1l111lll_opy_[bstack1l111ll_opy_ (u"࠭ࡴࡦࡵࡷࡣࡷࡻ࡮ࠨ↽")][bstack1l111ll_opy_ (u"ࠧࡱࡴࡲࡨࡺࡩࡴࡠ࡯ࡤࡴࠬ↾")] = bstack11lll1l11l_opy_
            else:
                bstack1l111lll_opy_[bstack1l111ll_opy_ (u"ࠨࡲࡵࡳࡩࡻࡣࡵࡡࡰࡥࡵ࠭↿")] = bstack11lll1l11l_opy_
        if event_url == bstack1l111ll_opy_ (u"ࠩࡤࡴ࡮࠵ࡶ࠲࠱ࡥࡥࡹࡩࡨࠨ⇀"):
            cls.bstack1llll11l1111_opy_()
            logger.debug(bstack1l111ll_opy_ (u"ࠥࡷࡪࡴࡤࡠࡦࡤࡸࡦࡀࠠࡂࡦࡧ࡭ࡳ࡭ࠠࡥࡣࡷࡥࠥࡺ࡯ࠡࡤࡤࡸࡨ࡮ࠠࡸ࡫ࡷ࡬ࠥ࡫ࡶࡦࡰࡷࡣࡹࡿࡰࡦ࠼ࠣࡿࢂࠨ⇁").format(bstack1l111lll_opy_[bstack1l111ll_opy_ (u"ࠫࡪࡼࡥ࡯ࡶࡢࡸࡾࡶࡥࠨ⇂")]))
            cls.bstack11l111lllll_opy_.add(bstack1l111lll_opy_)
        elif event_url == bstack1l111ll_opy_ (u"ࠬࡧࡰࡪ࠱ࡹ࠵࠴ࡹࡣࡳࡧࡨࡲࡸ࡮࡯ࡵࡵࠪ⇃"):
            cls.post_data([bstack1l111lll_opy_], event_url)
    @classmethod
    @error_handler(class_method=True)
    def bstack1lll111l_opy_(cls, logs):
        for log in logs:
            bstack1llll1l11l1l_opy_ = {
                bstack1l111ll_opy_ (u"࠭࡫ࡪࡰࡧࠫ⇄"): bstack1l111ll_opy_ (u"ࠧࡕࡇࡖࡘࡤࡒࡏࡈࠩ⇅"),
                bstack1l111ll_opy_ (u"ࠨ࡮ࡨࡺࡪࡲࠧ⇆"): log[bstack1l111ll_opy_ (u"ࠩ࡯ࡩࡻ࡫࡬ࠨ⇇")],
                bstack1l111ll_opy_ (u"ࠪࡸ࡮ࡳࡥࡴࡶࡤࡱࡵ࠭⇈"): log[bstack1l111ll_opy_ (u"ࠫࡹ࡯࡭ࡦࡵࡷࡥࡲࡶࠧ⇉")],
                bstack1l111ll_opy_ (u"ࠬ࡮ࡴࡵࡲࡢࡶࡪࡹࡰࡰࡰࡶࡩࠬ⇊"): {},
                bstack1l111ll_opy_ (u"࠭࡭ࡦࡵࡶࡥ࡬࡫ࠧ⇋"): log[bstack1l111ll_opy_ (u"ࠧ࡮ࡧࡶࡷࡦ࡭ࡥࠨ⇌")],
            }
            if bstack1l111ll_opy_ (u"ࠨࡶࡨࡷࡹࡥࡲࡶࡰࡢࡹࡺ࡯ࡤࠨ⇍") in log:
                bstack1llll1l11l1l_opy_[bstack1l111ll_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡳࡷࡱࡣࡺࡻࡩࡥࠩ⇎")] = log[bstack1l111ll_opy_ (u"ࠪࡸࡪࡹࡴࡠࡴࡸࡲࡤࡻࡵࡪࡦࠪ⇏")]
            elif bstack1l111ll_opy_ (u"ࠫ࡭ࡵ࡯࡬ࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠫ⇐") in log:
                bstack1llll1l11l1l_opy_[bstack1l111ll_opy_ (u"ࠬ࡮࡯ࡰ࡭ࡢࡶࡺࡴ࡟ࡶࡷ࡬ࡨࠬ⇑")] = log[bstack1l111ll_opy_ (u"࠭ࡨࡰࡱ࡮ࡣࡷࡻ࡮ࡠࡷࡸ࡭ࡩ࠭⇒")]
            cls.bstack1lll11l1_opy_({
                bstack1l111ll_opy_ (u"ࠧࡦࡸࡨࡲࡹࡥࡴࡺࡲࡨࠫ⇓"): bstack1l111ll_opy_ (u"ࠨࡎࡲ࡫ࡈࡸࡥࡢࡶࡨࡨࠬ⇔"),
                bstack1l111ll_opy_ (u"ࠩ࡯ࡳ࡬ࡹࠧ⇕"): [bstack1llll1l11l1l_opy_]
            })
    @classmethod
    @error_handler(class_method=True)
    def bstack1llll11ll11l_opy_(cls, steps):
        bstack1llll1l1111l_opy_ = []
        for step in steps:
            bstack1llll11lllll_opy_ = {
                bstack1l111ll_opy_ (u"ࠪ࡯࡮ࡴࡤࠨ⇖"): bstack1l111ll_opy_ (u"࡙ࠫࡋࡓࡕࡡࡖࡘࡊࡖࠧ⇗"),
                bstack1l111ll_opy_ (u"ࠬࡲࡥࡷࡧ࡯ࠫ⇘"): step[bstack1l111ll_opy_ (u"࠭࡬ࡦࡸࡨࡰࠬ⇙")],
                bstack1l111ll_opy_ (u"ࠧࡵ࡫ࡰࡩࡸࡺࡡ࡮ࡲࠪ⇚"): step[bstack1l111ll_opy_ (u"ࠨࡶ࡬ࡱࡪࡹࡴࡢ࡯ࡳࠫ⇛")],
                bstack1l111ll_opy_ (u"ࠩࡰࡩࡸࡹࡡࡨࡧࠪ⇜"): step[bstack1l111ll_opy_ (u"ࠪࡱࡪࡹࡳࡢࡩࡨࠫ⇝")],
                bstack1l111ll_opy_ (u"ࠫࡩࡻࡲࡢࡶ࡬ࡳࡳ࠭⇞"): step[bstack1l111ll_opy_ (u"ࠬࡪࡵࡳࡣࡷ࡭ࡴࡴࠧ⇟")]
            }
            if bstack1l111ll_opy_ (u"࠭ࡴࡦࡵࡷࡣࡷࡻ࡮ࡠࡷࡸ࡭ࡩ࠭⇠") in step:
                bstack1llll11lllll_opy_[bstack1l111ll_opy_ (u"ࠧࡵࡧࡶࡸࡤࡸࡵ࡯ࡡࡸࡹ࡮ࡪࠧ⇡")] = step[bstack1l111ll_opy_ (u"ࠨࡶࡨࡷࡹࡥࡲࡶࡰࡢࡹࡺ࡯ࡤࠨ⇢")]
            elif bstack1l111ll_opy_ (u"ࠩ࡫ࡳࡴࡱ࡟ࡳࡷࡱࡣࡺࡻࡩࡥࠩ⇣") in step:
                bstack1llll11lllll_opy_[bstack1l111ll_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡠࡴࡸࡲࡤࡻࡵࡪࡦࠪ⇤")] = step[bstack1l111ll_opy_ (u"ࠫ࡭ࡵ࡯࡬ࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠫ⇥")]
            bstack1llll1l1111l_opy_.append(bstack1llll11lllll_opy_)
        cls.bstack1lll11l1_opy_({
            bstack1l111ll_opy_ (u"ࠬ࡫ࡶࡦࡰࡷࡣࡹࡿࡰࡦࠩ⇦"): bstack1l111ll_opy_ (u"࠭ࡌࡰࡩࡆࡶࡪࡧࡴࡦࡦࠪ⇧"),
            bstack1l111ll_opy_ (u"ࠧ࡭ࡱࡪࡷࠬ⇨"): bstack1llll1l1111l_opy_
        })
    @classmethod
    @error_handler(class_method=True)
    @measure(event_name=EVENTS.bstack11l11l1ll_opy_, stage=STAGE.bstack1ll11l111l_opy_)
    def bstack1l11l11l1_opy_(cls, screenshot):
        cls.bstack1lll11l1_opy_({
            bstack1l111ll_opy_ (u"ࠨࡧࡹࡩࡳࡺ࡟ࡵࡻࡳࡩࠬ⇩"): bstack1l111ll_opy_ (u"ࠩࡏࡳ࡬ࡉࡲࡦࡣࡷࡩࡩ࠭⇪"),
            bstack1l111ll_opy_ (u"ࠪࡰࡴ࡭ࡳࠨ⇫"): [{
                bstack1l111ll_opy_ (u"ࠫࡰ࡯࡮ࡥࠩ⇬"): bstack1l111ll_opy_ (u"࡚ࠬࡅࡔࡖࡢࡗࡈࡘࡅࡆࡐࡖࡌࡔ࡚ࠧ⇭"),
                bstack1l111ll_opy_ (u"࠭ࡴࡪ࡯ࡨࡷࡹࡧ࡭ࡱࠩ⇮"): datetime.datetime.utcnow().isoformat() + bstack1l111ll_opy_ (u"࡛ࠧࠩ⇯"),
                bstack1l111ll_opy_ (u"ࠨ࡯ࡨࡷࡸࡧࡧࡦࠩ⇰"): screenshot[bstack1l111ll_opy_ (u"ࠩ࡬ࡱࡦ࡭ࡥࠨ⇱")],
                bstack1l111ll_opy_ (u"ࠪࡸࡪࡹࡴࡠࡴࡸࡲࡤࡻࡵࡪࡦࠪ⇲"): screenshot[bstack1l111ll_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠫ⇳")]
            }]
        }, event_url=bstack1l111ll_opy_ (u"ࠬࡧࡰࡪ࠱ࡹ࠵࠴ࡹࡣࡳࡧࡨࡲࡸ࡮࡯ࡵࡵࠪ⇴"))
    @classmethod
    @error_handler(class_method=True)
    def bstack1ll111l11_opy_(cls, driver):
        current_test_uuid = cls.current_test_uuid()
        if not current_test_uuid:
            return
        cls.bstack1lll11l1_opy_({
            bstack1l111ll_opy_ (u"࠭ࡥࡷࡧࡱࡸࡤࡺࡹࡱࡧࠪ⇵"): bstack1l111ll_opy_ (u"ࠧࡄࡄࡗࡗࡪࡹࡳࡪࡱࡱࡇࡷ࡫ࡡࡵࡧࡧࠫ⇶"),
            bstack1l111ll_opy_ (u"ࠨࡶࡨࡷࡹࡥࡲࡶࡰࠪ⇷"): {
                bstack1l111ll_opy_ (u"ࠤࡸࡹ࡮ࡪࠢ⇸"): cls.current_test_uuid(),
                bstack1l111ll_opy_ (u"ࠥ࡭ࡳࡺࡥࡨࡴࡤࡸ࡮ࡵ࡮ࡴࠤ⇹"): cls.bstack1l1l1l1l_opy_(driver)
            }
        })
    @classmethod
    def bstack1llll111_opy_(cls, event: str, bstack1l111lll_opy_: bstack11lll1l1_opy_):
        bstack1l111l1l_opy_ = {
            bstack1l111ll_opy_ (u"ࠫࡪࡼࡥ࡯ࡶࡢࡸࡾࡶࡥࠨ⇺"): event,
            bstack1l111lll_opy_.event_key(): bstack1l111lll_opy_.bstack1llll1ll_opy_(event)
        }
        cls.bstack1lll11l1_opy_(bstack1l111l1l_opy_)
        result = getattr(bstack1l111lll_opy_, bstack1l111ll_opy_ (u"ࠬࡸࡥࡴࡷ࡯ࡸࠬ⇻"), None)
        if event == bstack1l111ll_opy_ (u"࠭ࡔࡦࡵࡷࡖࡺࡴࡓࡵࡣࡵࡸࡪࡪࠧ⇼"):
            threading.current_thread().bstackTestMeta = {bstack1l111ll_opy_ (u"ࠧࡴࡶࡤࡸࡺࡹࠧ⇽"): bstack1l111ll_opy_ (u"ࠨࡲࡨࡲࡩ࡯࡮ࡨࠩ⇾")}
        elif event == bstack1l111ll_opy_ (u"ࠩࡗࡩࡸࡺࡒࡶࡰࡉ࡭ࡳ࡯ࡳࡩࡧࡧࠫ⇿"):
            threading.current_thread().bstackTestMeta = {bstack1l111ll_opy_ (u"ࠪࡷࡹࡧࡴࡶࡵࠪ∀"): getattr(result, bstack1l111ll_opy_ (u"ࠫࡷ࡫ࡳࡶ࡮ࡷࠫ∁"), bstack1l111ll_opy_ (u"ࠬ࠭∂"))}
    @classmethod
    def on(cls):
        if (os.environ.get(bstack1l111ll_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡊࡘࡖࠪ∃"), None) is None or os.environ[bstack1l111ll_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡋ࡙ࡗࠫ∄")] == bstack1l111ll_opy_ (u"ࠣࡰࡸࡰࡱࠨ∅")) and (os.environ.get(bstack1l111ll_opy_ (u"ࠩࡅࡗࡤࡇ࠱࠲࡛ࡢࡎ࡜࡚ࠧ∆"), None) is None or os.environ[bstack1l111ll_opy_ (u"ࠪࡆࡘࡥࡁ࠲࠳࡜ࡣࡏ࡝ࡔࠨ∇")] == bstack1l111ll_opy_ (u"ࠦࡳࡻ࡬࡭ࠤ∈")):
            return False
        return True
    @staticmethod
    def bstack1llll111lll1_opy_(func):
        def wrap(*args, **kwargs):
            if bstack1lll1l11_opy_.on():
                return func(*args, **kwargs)
            return
        return wrap
    @staticmethod
    def default_headers():
        headers = {
            bstack1l111ll_opy_ (u"ࠬࡉ࡯࡯ࡶࡨࡲࡹ࠳ࡔࡺࡲࡨࠫ∉"): bstack1l111ll_opy_ (u"࠭ࡡࡱࡲ࡯࡭ࡨࡧࡴࡪࡱࡱ࠳࡯ࡹ࡯࡯ࠩ∊"),
            bstack1l111ll_opy_ (u"࡙ࠧ࠯ࡅࡗ࡙ࡇࡃࡌ࠯ࡗࡉࡘ࡚ࡏࡑࡕࠪ∋"): bstack1l111ll_opy_ (u"ࠨࡶࡵࡹࡪ࠭∌")
        }
        if os.environ.get(bstack1l111ll_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡎࡕࡃࡡࡍ࡛࡙࠭∍"), None):
            headers[bstack1l111ll_opy_ (u"ࠪࡅࡺࡺࡨࡰࡴ࡬ࡾࡦࡺࡩࡰࡰࠪ∎")] = bstack1l111ll_opy_ (u"ࠫࡇ࡫ࡡࡳࡧࡵࠤࢀࢃࠧ∏").format(os.environ[bstack1l111ll_opy_ (u"ࠧࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡊࡘࡆࡤࡐࡗࡕࠤ∐")])
        return headers
    @staticmethod
    def request_url(url):
        return bstack1l111ll_opy_ (u"࠭ࡻࡾ࠱ࡾࢁࠬ∑").format(bstack1llll1l111ll_opy_, url)
    @staticmethod
    def current_test_uuid():
        return getattr(threading.current_thread(), bstack1l111ll_opy_ (u"ࠧࡤࡷࡵࡶࡪࡴࡴࡠࡶࡨࡷࡹࡥࡵࡶ࡫ࡧࠫ−"), None)
    @staticmethod
    def bstack1l1l1l1l_opy_(driver):
        return {
            bstack111l1ll1lll_opy_(): bstack1111l1l1111_opy_(driver)
        }
    @staticmethod
    def bstack1llll11l111l_opy_(exception_info, report):
        return [{bstack1l111ll_opy_ (u"ࠨࡤࡤࡧࡰࡺࡲࡢࡥࡨࠫ∓"): [exception_info.exconly(), report.longreprtext]}]
    @staticmethod
    def bstack1111111l1l_opy_(typename):
        if bstack1l111ll_opy_ (u"ࠤࡄࡷࡸ࡫ࡲࡵ࡫ࡲࡲࠧ∔") in typename:
            return bstack1l111ll_opy_ (u"ࠥࡅࡸࡹࡥࡳࡶ࡬ࡳࡳࡋࡲࡳࡱࡵࠦ∕")
        return bstack1l111ll_opy_ (u"࡚ࠦࡴࡨࡢࡰࡧࡰࡪࡪࡅࡳࡴࡲࡶࠧ∖")