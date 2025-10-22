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
import json
import logging
import os
import datetime
import threading
from bstack_utils.constants import EVENTS, STAGE
from bstack_utils.helper import bstack111l1ll111l_opy_, bstack111l11l1l1l_opy_, bstack11llll111_opy_, error_handler, bstack111l1ll1111_opy_, bstack1111l1ll11l_opy_, bstack1111lllll11_opy_, bstack1lllll11_opy_, bstack1l11l1ll_opy_
from bstack_utils.measure import measure
from bstack_utils.bstack11l11l11111_opy_ import bstack111ll1111l1_opy_
import bstack_utils.bstack11ll11111_opy_ as bstack11lll111l1_opy_
from bstack_utils.bstack1llll111_opy_ import bstack1lll1111_opy_
import bstack_utils.accessibility as bstack1lll11ll1_opy_
from bstack_utils.bstack111ll11l11_opy_ import bstack111ll11l11_opy_
from bstack_utils.bstack1l1l11ll_opy_ import bstack11lll1ll_opy_
from bstack_utils.constants import bstack1111lll1l1_opy_
bstack1llll1l1111l_opy_ = bstack111l1l_opy_ (u"ࠫ࡭ࡺࡴࡱࡵ࠽࠳࠴ࡩ࡯࡭࡮ࡨࡧࡹࡵࡲ࠮ࡱࡥࡷࡪࡸࡶࡢࡤ࡬ࡰ࡮ࡺࡹ࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡤࡱࡰࠫℚ")
logger = logging.getLogger(__name__)
class bstack1l1l1111_opy_:
    bstack11l11l11111_opy_ = None
    bs_config = None
    bstack1l11l11l1l_opy_ = None
    @classmethod
    @error_handler(class_method=True)
    @measure(event_name=EVENTS.bstack11l11lll11l_opy_, stage=STAGE.bstack1ll1ll111_opy_)
    def launch(cls, bs_config, bstack1l11l11l1l_opy_):
        cls.bs_config = bs_config
        cls.bstack1l11l11l1l_opy_ = bstack1l11l11l1l_opy_
        try:
            cls.bstack1llll11ll1l1_opy_()
            bstack1llll1l1l11l_opy_ = bstack111l1ll111l_opy_(bs_config)
            bstack1llll1llll11_opy_ = bstack111l11l1l1l_opy_(bs_config)
            data = bstack11lll111l1_opy_.bstack1llll11ll1ll_opy_(bs_config, bstack1l11l11l1l_opy_)
            config = {
                bstack111l1l_opy_ (u"ࠬࡧࡵࡵࡪࠪℛ"): (bstack1llll1l1l11l_opy_, bstack1llll1llll11_opy_),
                bstack111l1l_opy_ (u"࠭ࡨࡦࡣࡧࡩࡷࡹࠧℜ"): cls.default_headers()
            }
            response = bstack11llll111_opy_(bstack111l1l_opy_ (u"ࠧࡑࡑࡖࡘࠬℝ"), cls.request_url(bstack111l1l_opy_ (u"ࠨࡣࡳ࡭࠴ࡼ࠲࠰ࡤࡸ࡭ࡱࡪࡳࠨ℞")), data, config)
            if response.status_code != 200:
                bstack111ll1ll11_opy_ = response.json()
                if bstack111ll1ll11_opy_[bstack111l1l_opy_ (u"ࠩࡶࡹࡨࡩࡥࡴࡵࠪ℟")] == False:
                    cls.bstack1llll1l111ll_opy_(bstack111ll1ll11_opy_)
                    return
                cls.bstack1llll11l111l_opy_(bstack111ll1ll11_opy_[bstack111l1l_opy_ (u"ࠪࡳࡧࡹࡥࡳࡸࡤࡦ࡮ࡲࡩࡵࡻࠪ℠")])
                cls.bstack1llll1l11l1l_opy_(bstack111ll1ll11_opy_[bstack111l1l_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠫ℡")])
                return None
            bstack1llll111lll1_opy_ = cls.bstack1llll11ll111_opy_(response)
            return bstack1llll111lll1_opy_, response.json()
        except Exception as error:
            logger.error(bstack111l1l_opy_ (u"ࠧࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡࡹ࡫࡭ࡱ࡫ࠠࡤࡴࡨࡥࡹ࡯࡮ࡨࠢࡥࡹ࡮ࡲࡤࠡࡨࡲࡶ࡚ࠥࡥࡴࡶࡋࡹࡧࡀࠠࡼࡿࠥ™").format(str(error)))
            return None
    @classmethod
    @error_handler(class_method=True)
    def stop(cls, bstack1llll11l1lll_opy_=None):
        if not bstack1lll1111_opy_.on() and not bstack1lll11ll1_opy_.on():
            return
        if os.environ.get(bstack111l1l_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡊࡘࡖࠪ℣")) == bstack111l1l_opy_ (u"ࠢ࡯ࡷ࡯ࡰࠧℤ") or os.environ.get(bstack111l1l_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡍ࡛ࡂࡠࡗࡘࡍࡉ࠭℥")) == bstack111l1l_opy_ (u"ࠤࡱࡹࡱࡲࠢΩ"):
            logger.error(bstack111l1l_opy_ (u"ࠪࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩ࡯ࠢࡶࡸࡴࡶࠠࡣࡷ࡬ࡰࡩࠦࡲࡦࡳࡸࡩࡸࡺࠠࡵࡱࠣࡘࡪࡹࡴࡉࡷࡥ࠾ࠥࡓࡩࡴࡵ࡬ࡲ࡬ࠦࡡࡶࡶ࡫ࡩࡳࡺࡩࡤࡣࡷ࡭ࡴࡴࠠࡵࡱ࡮ࡩࡳ࠭℧"))
            return {
                bstack111l1l_opy_ (u"ࠫࡸࡺࡡࡵࡷࡶࠫℨ"): bstack111l1l_opy_ (u"ࠬ࡫ࡲࡳࡱࡵࠫ℩"),
                bstack111l1l_opy_ (u"࠭࡭ࡦࡵࡶࡥ࡬࡫ࠧK"): bstack111l1l_opy_ (u"ࠧࡕࡱ࡮ࡩࡳ࠵ࡢࡶ࡫࡯ࡨࡎࡊࠠࡪࡵࠣࡹࡳࡪࡥࡧ࡫ࡱࡩࡩ࠲ࠠࡣࡷ࡬ࡰࡩࠦࡣࡳࡧࡤࡸ࡮ࡵ࡮ࠡ࡯࡬࡫࡭ࡺࠠࡩࡣࡹࡩࠥ࡬ࡡࡪ࡮ࡨࡨࠬÅ")
            }
        try:
            cls.bstack11l11l11111_opy_.shutdown()
            data = {
                bstack111l1l_opy_ (u"ࠨࡨ࡬ࡲ࡮ࡹࡨࡦࡦࡢࡥࡹ࠭ℬ"): bstack1lllll11_opy_()
            }
            if not bstack1llll11l1lll_opy_ is None:
                data[bstack111l1l_opy_ (u"ࠩࡩ࡭ࡳ࡯ࡳࡩࡧࡧࡣࡲ࡫ࡴࡢࡦࡤࡸࡦ࠭ℭ")] = [{
                    bstack111l1l_opy_ (u"ࠪࡶࡪࡧࡳࡰࡰࠪ℮"): bstack111l1l_opy_ (u"ࠫࡺࡹࡥࡳࡡ࡮࡭ࡱࡲࡥࡥࠩℯ"),
                    bstack111l1l_opy_ (u"ࠬࡹࡩࡨࡰࡤࡰࠬℰ"): bstack1llll11l1lll_opy_
                }]
            config = {
                bstack111l1l_opy_ (u"࠭ࡨࡦࡣࡧࡩࡷࡹࠧℱ"): cls.default_headers()
            }
            bstack11ll111l1ll_opy_ = bstack111l1l_opy_ (u"ࠧࡢࡲ࡬࠳ࡻ࠷࠯ࡣࡷ࡬ࡰࡩࡹ࠯ࡼࡿ࠲ࡷࡹࡵࡰࠨℲ").format(os.environ[bstack111l1l_opy_ (u"ࠣࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡍ࡛ࡂࡠࡗࡘࡍࡉࠨℳ")])
            bstack1llll111llll_opy_ = cls.request_url(bstack11ll111l1ll_opy_)
            response = bstack11llll111_opy_(bstack111l1l_opy_ (u"ࠩࡓ࡙࡙࠭ℴ"), bstack1llll111llll_opy_, data, config)
            if not response.ok:
                raise Exception(bstack111l1l_opy_ (u"ࠥࡗࡹࡵࡰࠡࡴࡨࡵࡺ࡫ࡳࡵࠢࡱࡳࡹࠦ࡯࡬ࠤℵ"))
        except Exception as error:
            logger.error(bstack111l1l_opy_ (u"ࠦࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣࡷࡹࡵࡰࠡࡤࡸ࡭ࡱࡪࠠࡳࡧࡴࡹࡪࡹࡴࠡࡶࡲࠤ࡙࡫ࡳࡵࡊࡸࡦ࠿ࡀࠠࠣℶ") + str(error))
            return {
                bstack111l1l_opy_ (u"ࠬࡹࡴࡢࡶࡸࡷࠬℷ"): bstack111l1l_opy_ (u"࠭ࡥࡳࡴࡲࡶࠬℸ"),
                bstack111l1l_opy_ (u"ࠧ࡮ࡧࡶࡷࡦ࡭ࡥࠨℹ"): str(error)
            }
    @classmethod
    @error_handler(class_method=True)
    def bstack1llll11ll111_opy_(cls, response):
        bstack111ll1ll11_opy_ = response.json() if not isinstance(response, dict) else response
        bstack1llll111lll1_opy_ = {}
        if bstack111ll1ll11_opy_.get(bstack111l1l_opy_ (u"ࠨ࡬ࡺࡸࠬ℺")) is None:
            os.environ[bstack111l1l_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡎࡕࡃࡡࡍ࡛࡙࠭℻")] = bstack111l1l_opy_ (u"ࠪࡲࡺࡲ࡬ࠨℼ")
        else:
            os.environ[bstack111l1l_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡉࡗࡅࡣࡏ࡝ࡔࠨℽ")] = bstack111ll1ll11_opy_.get(bstack111l1l_opy_ (u"ࠬࡰࡷࡵࠩℾ"), bstack111l1l_opy_ (u"࠭࡮ࡶ࡮࡯ࠫℿ"))
        os.environ[bstack111l1l_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡖࡗࡌࡈࠬ⅀")] = bstack111ll1ll11_opy_.get(bstack111l1l_opy_ (u"ࠨࡤࡸ࡭ࡱࡪ࡟ࡩࡣࡶ࡬ࡪࡪ࡟ࡪࡦࠪ⅁"), bstack111l1l_opy_ (u"ࠩࡱࡹࡱࡲࠧ⅂"))
        logger.info(bstack111l1l_opy_ (u"ࠪࡘࡪࡹࡴࡩࡷࡥࠤࡸࡺࡡࡳࡶࡨࡨࠥࡽࡩࡵࡪࠣ࡭ࡩࡀࠠࠨ⅃") + os.getenv(bstack111l1l_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡉࡗࡅࡣ࡚࡛ࡉࡅࠩ⅄")));
        if bstack1lll1111_opy_.bstack11l111lllll_opy_(cls.bs_config, cls.bstack1l11l11l1l_opy_.get(bstack111l1l_opy_ (u"ࠬ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡷࡶࡩࡩ࠭ⅅ"), bstack111l1l_opy_ (u"࠭ࠧⅆ"))) is True:
            bstack11ll11l111l_opy_, build_hashed_id, bstack1llll11lll11_opy_ = cls.bstack1llll11ll11l_opy_(bstack111ll1ll11_opy_)
            if bstack11ll11l111l_opy_ != None and build_hashed_id != None:
                bstack1llll111lll1_opy_[bstack111l1l_opy_ (u"ࠧࡰࡤࡶࡩࡷࡼࡡࡣ࡫࡯࡭ࡹࡿࠧⅇ")] = {
                    bstack111l1l_opy_ (u"ࠨ࡬ࡺࡸࡤࡺ࡯࡬ࡧࡱࠫⅈ"): bstack11ll11l111l_opy_,
                    bstack111l1l_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡠࡪࡤࡷ࡭࡫ࡤࡠ࡫ࡧࠫⅉ"): build_hashed_id,
                    bstack111l1l_opy_ (u"ࠪࡥࡱࡲ࡯ࡸࡡࡶࡧࡷ࡫ࡥ࡯ࡵ࡫ࡳࡹࡹࠧ⅊"): bstack1llll11lll11_opy_
                }
            else:
                bstack1llll111lll1_opy_[bstack111l1l_opy_ (u"ࠫࡴࡨࡳࡦࡴࡹࡥࡧ࡯࡬ࡪࡶࡼࠫ⅋")] = {}
        else:
            bstack1llll111lll1_opy_[bstack111l1l_opy_ (u"ࠬࡵࡢࡴࡧࡵࡺࡦࡨࡩ࡭࡫ࡷࡽࠬ⅌")] = {}
        bstack1llll1l11l11_opy_, build_hashed_id = cls.bstack1llll1l11111_opy_(bstack111ll1ll11_opy_)
        if bstack1llll1l11l11_opy_ != None and build_hashed_id != None:
            bstack1llll111lll1_opy_[bstack111l1l_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾ࠭⅍")] = {
                bstack111l1l_opy_ (u"ࠧࡢࡷࡷ࡬ࡤࡺ࡯࡬ࡧࡱࠫⅎ"): bstack1llll1l11l11_opy_,
                bstack111l1l_opy_ (u"ࠨࡤࡸ࡭ࡱࡪ࡟ࡩࡣࡶ࡬ࡪࡪ࡟ࡪࡦࠪ⅏"): build_hashed_id,
            }
        else:
            bstack1llll111lll1_opy_[bstack111l1l_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠩ⅐")] = {}
        if bstack1llll111lll1_opy_[bstack111l1l_opy_ (u"ࠪࡳࡧࡹࡥࡳࡸࡤࡦ࡮ࡲࡩࡵࡻࠪ⅑")].get(bstack111l1l_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡢ࡬ࡦࡹࡨࡦࡦࡢ࡭ࡩ࠭⅒")) != None or bstack1llll111lll1_opy_[bstack111l1l_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠬ⅓")].get(bstack111l1l_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡤ࡮ࡡࡴࡪࡨࡨࡤ࡯ࡤࠨ⅔")) != None:
            cls.bstack1llll1l111l1_opy_(bstack111ll1ll11_opy_.get(bstack111l1l_opy_ (u"ࠧ࡫ࡹࡷࠫ⅕")), bstack111ll1ll11_opy_.get(bstack111l1l_opy_ (u"ࠨࡤࡸ࡭ࡱࡪ࡟ࡩࡣࡶ࡬ࡪࡪ࡟ࡪࡦࠪ⅖")))
        return bstack1llll111lll1_opy_
    @classmethod
    def bstack1llll11ll11l_opy_(cls, bstack111ll1ll11_opy_):
        if bstack111ll1ll11_opy_.get(bstack111l1l_opy_ (u"ࠩࡲࡦࡸ࡫ࡲࡷࡣࡥ࡭ࡱ࡯ࡴࡺࠩ⅗")) == None:
            cls.bstack1llll11l111l_opy_()
            return [None, None, None]
        if bstack111ll1ll11_opy_[bstack111l1l_opy_ (u"ࠪࡳࡧࡹࡥࡳࡸࡤࡦ࡮ࡲࡩࡵࡻࠪ⅘")][bstack111l1l_opy_ (u"ࠫࡸࡻࡣࡤࡧࡶࡷࠬ⅙")] != True:
            cls.bstack1llll11l111l_opy_(bstack111ll1ll11_opy_[bstack111l1l_opy_ (u"ࠬࡵࡢࡴࡧࡵࡺࡦࡨࡩ࡭࡫ࡷࡽࠬ⅚")])
            return [None, None, None]
        logger.debug(bstack111l1l_opy_ (u"࠭ࡻࡾࠢࡅࡹ࡮ࡲࡤࠡࡥࡵࡩࡦࡺࡩࡰࡰࠣࡗࡺࡩࡣࡦࡵࡶࡪࡺࡲࠡࠨ⅛").format(bstack1111lll1l1_opy_))
        os.environ[bstack111l1l_opy_ (u"ࠧࡃࡕࡢࡘࡊ࡙ࡔࡐࡒࡖࡣࡇ࡛ࡉࡍࡆࡢࡇࡔࡓࡐࡍࡇࡗࡉࡉ࠭⅜")] = bstack111l1l_opy_ (u"ࠨࡶࡵࡹࡪ࠭⅝")
        if bstack111ll1ll11_opy_.get(bstack111l1l_opy_ (u"ࠩ࡭ࡻࡹ࠭⅞")):
            os.environ[bstack111l1l_opy_ (u"ࠪࡇࡗࡋࡄࡆࡐࡗࡍࡆࡒࡓࡠࡈࡒࡖࡤࡉࡒࡂࡕࡋࡣࡗࡋࡐࡐࡔࡗࡍࡓࡍࠧ⅟")] = json.dumps({
                bstack111l1l_opy_ (u"ࠫࡺࡹࡥࡳࡰࡤࡱࡪ࠭Ⅰ"): bstack111l1ll111l_opy_(cls.bs_config),
                bstack111l1l_opy_ (u"ࠬࡶࡡࡴࡵࡺࡳࡷࡪࠧⅡ"): bstack111l11l1l1l_opy_(cls.bs_config)
            })
        if bstack111ll1ll11_opy_.get(bstack111l1l_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡤ࡮ࡡࡴࡪࡨࡨࡤ࡯ࡤࠨⅢ")):
            os.environ[bstack111l1l_opy_ (u"ࠧࡃࡕࡢࡘࡊ࡙ࡔࡐࡒࡖࡣࡇ࡛ࡉࡍࡆࡢࡌࡆ࡙ࡈࡆࡆࡢࡍࡉ࠭Ⅳ")] = bstack111ll1ll11_opy_[bstack111l1l_opy_ (u"ࠨࡤࡸ࡭ࡱࡪ࡟ࡩࡣࡶ࡬ࡪࡪ࡟ࡪࡦࠪⅤ")]
        if bstack111ll1ll11_opy_[bstack111l1l_opy_ (u"ࠩࡲࡦࡸ࡫ࡲࡷࡣࡥ࡭ࡱ࡯ࡴࡺࠩⅥ")].get(bstack111l1l_opy_ (u"ࠪࡳࡵࡺࡩࡰࡰࡶࠫⅦ"), {}).get(bstack111l1l_opy_ (u"ࠫࡦࡲ࡬ࡰࡹࡢࡷࡨࡸࡥࡦࡰࡶ࡬ࡴࡺࡳࠨⅧ")):
            os.environ[bstack111l1l_opy_ (u"ࠬࡈࡓࡠࡖࡈࡗ࡙ࡕࡐࡔࡡࡄࡐࡑࡕࡗࡠࡕࡆࡖࡊࡋࡎࡔࡊࡒࡘࡘ࠭Ⅸ")] = str(bstack111ll1ll11_opy_[bstack111l1l_opy_ (u"࠭࡯ࡣࡵࡨࡶࡻࡧࡢࡪ࡮࡬ࡸࡾ࠭Ⅹ")][bstack111l1l_opy_ (u"ࠧࡰࡲࡷ࡭ࡴࡴࡳࠨⅪ")][bstack111l1l_opy_ (u"ࠨࡣ࡯ࡰࡴࡽ࡟ࡴࡥࡵࡩࡪࡴࡳࡩࡱࡷࡷࠬⅫ")])
        else:
            os.environ[bstack111l1l_opy_ (u"ࠩࡅࡗࡤ࡚ࡅࡔࡖࡒࡔࡘࡥࡁࡍࡎࡒ࡛ࡤ࡙ࡃࡓࡇࡈࡒࡘࡎࡏࡕࡕࠪⅬ")] = bstack111l1l_opy_ (u"ࠥࡲࡺࡲ࡬ࠣⅭ")
        return [bstack111ll1ll11_opy_[bstack111l1l_opy_ (u"ࠫ࡯ࡽࡴࠨⅮ")], bstack111ll1ll11_opy_[bstack111l1l_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡣ࡭ࡧࡳࡩࡧࡧࡣ࡮ࡪࠧⅯ")], os.environ[bstack111l1l_opy_ (u"࠭ࡂࡔࡡࡗࡉࡘ࡚ࡏࡑࡕࡢࡅࡑࡒࡏࡘࡡࡖࡇࡗࡋࡅࡏࡕࡋࡓ࡙࡙ࠧⅰ")]]
    @classmethod
    def bstack1llll1l11111_opy_(cls, bstack111ll1ll11_opy_):
        if bstack111ll1ll11_opy_.get(bstack111l1l_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠧⅱ")) == None:
            cls.bstack1llll1l11l1l_opy_()
            return [None, None]
        if bstack111ll1ll11_opy_[bstack111l1l_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠨⅲ")][bstack111l1l_opy_ (u"ࠩࡶࡹࡨࡩࡥࡴࡵࠪⅳ")] != True:
            cls.bstack1llll1l11l1l_opy_(bstack111ll1ll11_opy_[bstack111l1l_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠪⅴ")])
            return [None, None]
        if bstack111ll1ll11_opy_[bstack111l1l_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠫⅵ")].get(bstack111l1l_opy_ (u"ࠬࡵࡰࡵ࡫ࡲࡲࡸ࠭ⅶ")):
            logger.debug(bstack111l1l_opy_ (u"࠭ࡔࡦࡵࡷࠤࡆࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡇࡻࡩ࡭ࡦࠣࡧࡷ࡫ࡡࡵ࡫ࡲࡲ࡙ࠥࡵࡤࡥࡨࡷࡸ࡬ࡵ࡭ࠣࠪⅷ"))
            parsed = json.loads(os.getenv(bstack111l1l_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡣࡆࡉࡃࡆࡕࡖࡍࡇࡏࡌࡊࡖ࡜ࡣࡈࡕࡎࡇࡋࡊ࡙ࡗࡇࡔࡊࡑࡑࡣ࡞ࡓࡌࠨⅸ"), bstack111l1l_opy_ (u"ࠨࡽࢀࠫⅹ")))
            capabilities = bstack11lll111l1_opy_.bstack1llll11l1l1l_opy_(bstack111ll1ll11_opy_[bstack111l1l_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠩⅺ")][bstack111l1l_opy_ (u"ࠪࡳࡵࡺࡩࡰࡰࡶࠫⅻ")][bstack111l1l_opy_ (u"ࠫࡨࡧࡰࡢࡤ࡬ࡰ࡮ࡺࡩࡦࡵࠪⅼ")], bstack111l1l_opy_ (u"ࠬࡴࡡ࡮ࡧࠪⅽ"), bstack111l1l_opy_ (u"࠭ࡶࡢ࡮ࡸࡩࠬⅾ"))
            bstack1llll1l11l11_opy_ = capabilities[bstack111l1l_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࡔࡰ࡭ࡨࡲࠬⅿ")]
            os.environ[bstack111l1l_opy_ (u"ࠨࡄࡖࡣࡆ࠷࠱࡚ࡡࡍ࡛࡙࠭ↀ")] = bstack1llll1l11l11_opy_
            if bstack111l1l_opy_ (u"ࠤࡤࡹࡹࡵ࡭ࡢࡶࡨࠦↁ") in bstack111ll1ll11_opy_ and bstack111ll1ll11_opy_.get(bstack111l1l_opy_ (u"ࠥࡥࡵࡶ࡟ࡢࡷࡷࡳࡲࡧࡴࡦࠤↂ")) is None:
                parsed[bstack111l1l_opy_ (u"ࠫࡸࡩࡡ࡯ࡰࡨࡶ࡛࡫ࡲࡴ࡫ࡲࡲࠬↃ")] = capabilities[bstack111l1l_opy_ (u"ࠬࡹࡣࡢࡰࡱࡩࡷ࡜ࡥࡳࡵ࡬ࡳࡳ࠭ↄ")]
            os.environ[bstack111l1l_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡢࡅࡈࡉࡅࡔࡕࡌࡆࡎࡒࡉࡕ࡛ࡢࡇࡔࡔࡆࡊࡉࡘࡖࡆ࡚ࡉࡐࡐࡢ࡝ࡒࡒࠧↅ")] = json.dumps(parsed)
            scripts = bstack11lll111l1_opy_.bstack1llll11l1l1l_opy_(bstack111ll1ll11_opy_[bstack111l1l_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠧↆ")][bstack111l1l_opy_ (u"ࠨࡱࡳࡸ࡮ࡵ࡮ࡴࠩↇ")][bstack111l1l_opy_ (u"ࠩࡶࡧࡷ࡯ࡰࡵࡵࠪↈ")], bstack111l1l_opy_ (u"ࠪࡲࡦࡳࡥࠨ↉"), bstack111l1l_opy_ (u"ࠫࡨࡵ࡭࡮ࡣࡱࡨࠬ↊"))
            bstack111ll11l11_opy_.bstack11llll11l_opy_(scripts)
            commands = bstack111ll1ll11_opy_[bstack111l1l_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠬ↋")][bstack111l1l_opy_ (u"࠭࡯ࡱࡶ࡬ࡳࡳࡹࠧ↌")][bstack111l1l_opy_ (u"ࠧࡤࡱࡰࡱࡦࡴࡤࡴࡖࡲ࡛ࡷࡧࡰࠨ↍")].get(bstack111l1l_opy_ (u"ࠨࡥࡲࡱࡲࡧ࡮ࡥࡵࠪ↎"))
            bstack111ll11l11_opy_.bstack1lllll11l11l_opy_(commands)
            bstack1lllll111l11_opy_ = capabilities.get(bstack111l1l_opy_ (u"ࠩࡪࡳࡴ࡭࠺ࡤࡪࡵࡳࡲ࡫ࡏࡱࡶ࡬ࡳࡳࡹࠧ↏"))
            bstack111ll11l11_opy_.bstack1lllll111ll1_opy_(bstack1lllll111l11_opy_)
            bstack111ll11l11_opy_.store()
        return [bstack1llll1l11l11_opy_, bstack111ll1ll11_opy_[bstack111l1l_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡡ࡫ࡥࡸ࡮ࡥࡥࡡ࡬ࡨࠬ←")]]
    @classmethod
    def bstack1llll11l111l_opy_(cls, response=None):
        os.environ[bstack111l1l_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡉࡗࡅࡣ࡚࡛ࡉࡅࠩ↑")] = bstack111l1l_opy_ (u"ࠬࡴࡵ࡭࡮ࠪ→")
        os.environ[bstack111l1l_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡊࡘࡖࠪ↓")] = bstack111l1l_opy_ (u"ࠧ࡯ࡷ࡯ࡰࠬ↔")
        os.environ[bstack111l1l_opy_ (u"ࠨࡄࡖࡣ࡙ࡋࡓࡕࡑࡓࡗࡤࡈࡕࡊࡎࡇࡣࡈࡕࡍࡑࡎࡈࡘࡊࡊࠧ↕")] = bstack111l1l_opy_ (u"ࠩࡩࡥࡱࡹࡥࠨ↖")
        os.environ[bstack111l1l_opy_ (u"ࠪࡆࡘࡥࡔࡆࡕࡗࡓࡕ࡙࡟ࡃࡗࡌࡐࡉࡥࡈࡂࡕࡋࡉࡉࡥࡉࡅࠩ↗")] = bstack111l1l_opy_ (u"ࠦࡳࡻ࡬࡭ࠤ↘")
        os.environ[bstack111l1l_opy_ (u"ࠬࡈࡓࡠࡖࡈࡗ࡙ࡕࡐࡔࡡࡄࡐࡑࡕࡗࡠࡕࡆࡖࡊࡋࡎࡔࡊࡒࡘࡘ࠭↙")] = bstack111l1l_opy_ (u"ࠨ࡮ࡶ࡮࡯ࠦ↚")
        cls.bstack1llll1l111ll_opy_(response, bstack111l1l_opy_ (u"ࠢࡰࡤࡶࡩࡷࡼࡡࡣ࡫࡯࡭ࡹࡿࠢ↛"))
        return [None, None, None]
    @classmethod
    def bstack1llll1l11l1l_opy_(cls, response=None):
        os.environ[bstack111l1l_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡍ࡛ࡂࡠࡗࡘࡍࡉ࠭↜")] = bstack111l1l_opy_ (u"ࠩࡱࡹࡱࡲࠧ↝")
        os.environ[bstack111l1l_opy_ (u"ࠪࡆࡘࡥࡁ࠲࠳࡜ࡣࡏ࡝ࡔࠨ↞")] = bstack111l1l_opy_ (u"ࠫࡳࡻ࡬࡭ࠩ↟")
        os.environ[bstack111l1l_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡊࡘࡆࡤࡐࡗࡕࠩ↠")] = bstack111l1l_opy_ (u"࠭࡮ࡶ࡮࡯ࠫ↡")
        cls.bstack1llll1l111ll_opy_(response, bstack111l1l_opy_ (u"ࠢࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠢ↢"))
        return [None, None, None]
    @classmethod
    def bstack1llll1l111l1_opy_(cls, jwt, build_hashed_id):
        os.environ[bstack111l1l_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡍ࡛ࡂࡠࡌ࡚ࡘࠬ↣")] = jwt
        os.environ[bstack111l1l_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡎࡕࡃࡡࡘ࡙ࡎࡊࠧ↤")] = build_hashed_id
    @classmethod
    def bstack1llll1l111ll_opy_(cls, response=None, product=bstack111l1l_opy_ (u"ࠥࠦ↥")):
        if response == None or response.get(bstack111l1l_opy_ (u"ࠫࡪࡸࡲࡰࡴࡶࠫ↦")) == None:
            logger.error(product + bstack111l1l_opy_ (u"ࠧࠦࡂࡶ࡫࡯ࡨࠥࡩࡲࡦࡣࡷ࡭ࡴࡴࠠࡧࡣ࡬ࡰࡪࡪࠢ↧"))
            return
        for error in response[bstack111l1l_opy_ (u"࠭ࡥࡳࡴࡲࡶࡸ࠭↨")]:
            bstack1111l1l11l1_opy_ = error[bstack111l1l_opy_ (u"ࠧ࡬ࡧࡼࠫ↩")]
            error_message = error[bstack111l1l_opy_ (u"ࠨ࡯ࡨࡷࡸࡧࡧࡦࠩ↪")]
            if error_message:
                if bstack1111l1l11l1_opy_ == bstack111l1l_opy_ (u"ࠤࡈࡖࡗࡕࡒࡠࡃࡆࡇࡊ࡙ࡓࡠࡆࡈࡒࡎࡋࡄࠣ↫"):
                    logger.info(error_message)
                else:
                    logger.error(error_message)
            else:
                logger.error(bstack111l1l_opy_ (u"ࠥࡈࡦࡺࡡࠡࡷࡳࡰࡴࡧࡤࠡࡶࡲࠤࡇࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࠣࠦ↬") + product + bstack111l1l_opy_ (u"ࠦࠥ࡬ࡡࡪ࡮ࡨࡨࠥࡪࡵࡦࠢࡷࡳࠥࡹ࡯࡮ࡧࠣࡩࡷࡸ࡯ࡳࠤ↭"))
    @classmethod
    def bstack1llll11ll1l1_opy_(cls):
        if cls.bstack11l11l11111_opy_ is not None:
            return
        cls.bstack11l11l11111_opy_ = bstack111ll1111l1_opy_(cls.post_data)
        cls.bstack11l11l11111_opy_.start()
    @classmethod
    def bstack1l1l1lll_opy_(cls):
        if cls.bstack11l11l11111_opy_ is None:
            return
        cls.bstack11l11l11111_opy_.shutdown()
    @classmethod
    @error_handler(class_method=True)
    def post_data(cls, bstack1l1ll1l1_opy_, event_url=bstack111l1l_opy_ (u"ࠬࡧࡰࡪ࠱ࡹ࠵࠴ࡨࡡࡵࡥ࡫ࠫ↮")):
        config = {
            bstack111l1l_opy_ (u"࠭ࡨࡦࡣࡧࡩࡷࡹࠧ↯"): cls.default_headers()
        }
        logger.debug(bstack111l1l_opy_ (u"ࠢࡱࡱࡶࡸࡤࡪࡡࡵࡣ࠽ࠤࡘ࡫࡮ࡥ࡫ࡱ࡫ࠥࡪࡡࡵࡣࠣࡸࡴࠦࡴࡦࡵࡷ࡬ࡺࡨࠠࡧࡱࡵࠤࡪࡼࡥ࡯ࡶࡶࠤࢀࢃࠢ↰").format(bstack111l1l_opy_ (u"ࠨ࠮ࠣࠫ↱").join([event[bstack111l1l_opy_ (u"ࠩࡨࡺࡪࡴࡴࡠࡶࡼࡴࡪ࠭↲")] for event in bstack1l1ll1l1_opy_])))
        response = bstack11llll111_opy_(bstack111l1l_opy_ (u"ࠪࡔࡔ࡙ࡔࠨ↳"), cls.request_url(event_url), bstack1l1ll1l1_opy_, config)
        bstack1llll1ll1ll1_opy_ = response.json()
    @classmethod
    def bstack1lll1l1l_opy_(cls, bstack1l1ll1l1_opy_, event_url=bstack111l1l_opy_ (u"ࠫࡦࡶࡩ࠰ࡸ࠴࠳ࡧࡧࡴࡤࡪࠪ↴")):
        logger.debug(bstack111l1l_opy_ (u"ࠧࡹࡥ࡯ࡦࡢࡨࡦࡺࡡ࠻ࠢࡄࡸࡹ࡫࡭ࡱࡶ࡬ࡲ࡬ࠦࡴࡰࠢࡤࡨࡩࠦࡤࡢࡶࡤࠤࡹࡵࠠࡣࡣࡷࡧ࡭ࠦࡷࡪࡶ࡫ࠤࡪࡼࡥ࡯ࡶࡢࡸࡾࡶࡥ࠻ࠢࡾࢁࠧ↵").format(bstack1l1ll1l1_opy_[bstack111l1l_opy_ (u"࠭ࡥࡷࡧࡱࡸࡤࡺࡹࡱࡧࠪ↶")]))
        if not bstack11lll111l1_opy_.bstack1llll11lll1l_opy_(bstack1l1ll1l1_opy_[bstack111l1l_opy_ (u"ࠧࡦࡸࡨࡲࡹࡥࡴࡺࡲࡨࠫ↷")]):
            logger.debug(bstack111l1l_opy_ (u"ࠣࡵࡨࡲࡩࡥࡤࡢࡶࡤ࠾ࠥࡔ࡯ࡵࠢࡤࡨࡩ࡯࡮ࡨࠢࡧࡥࡹࡧࠠࡸ࡫ࡷ࡬ࠥ࡫ࡶࡦࡰࡷࡣࡹࡿࡰࡦ࠼ࠣࡿࢂࠨ↸").format(bstack1l1ll1l1_opy_[bstack111l1l_opy_ (u"ࠩࡨࡺࡪࡴࡴࡠࡶࡼࡴࡪ࠭↹")]))
            return
        bstack11llll11l1_opy_ = bstack11lll111l1_opy_.bstack1llll11l1ll1_opy_(bstack1l1ll1l1_opy_[bstack111l1l_opy_ (u"ࠪࡩࡻ࡫࡮ࡵࡡࡷࡽࡵ࡫ࠧ↺")], bstack1l1ll1l1_opy_.get(bstack111l1l_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡵࡹࡳ࠭↻")))
        if bstack11llll11l1_opy_ != None:
            if bstack1l1ll1l1_opy_.get(bstack111l1l_opy_ (u"ࠬࡺࡥࡴࡶࡢࡶࡺࡴࠧ↼")) != None:
                bstack1l1ll1l1_opy_[bstack111l1l_opy_ (u"࠭ࡴࡦࡵࡷࡣࡷࡻ࡮ࠨ↽")][bstack111l1l_opy_ (u"ࠧࡱࡴࡲࡨࡺࡩࡴࡠ࡯ࡤࡴࠬ↾")] = bstack11llll11l1_opy_
            else:
                bstack1l1ll1l1_opy_[bstack111l1l_opy_ (u"ࠨࡲࡵࡳࡩࡻࡣࡵࡡࡰࡥࡵ࠭↿")] = bstack11llll11l1_opy_
        if event_url == bstack111l1l_opy_ (u"ࠩࡤࡴ࡮࠵ࡶ࠲࠱ࡥࡥࡹࡩࡨࠨ⇀"):
            cls.bstack1llll11ll1l1_opy_()
            logger.debug(bstack111l1l_opy_ (u"ࠥࡷࡪࡴࡤࡠࡦࡤࡸࡦࡀࠠࡂࡦࡧ࡭ࡳ࡭ࠠࡥࡣࡷࡥࠥࡺ࡯ࠡࡤࡤࡸࡨ࡮ࠠࡸ࡫ࡷ࡬ࠥ࡫ࡶࡦࡰࡷࡣࡹࡿࡰࡦ࠼ࠣࡿࢂࠨ⇁").format(bstack1l1ll1l1_opy_[bstack111l1l_opy_ (u"ࠫࡪࡼࡥ࡯ࡶࡢࡸࡾࡶࡥࠨ⇂")]))
            cls.bstack11l11l11111_opy_.add(bstack1l1ll1l1_opy_)
        elif event_url == bstack111l1l_opy_ (u"ࠬࡧࡰࡪ࠱ࡹ࠵࠴ࡹࡣࡳࡧࡨࡲࡸ࡮࡯ࡵࡵࠪ⇃"):
            cls.post_data([bstack1l1ll1l1_opy_], event_url)
    @classmethod
    @error_handler(class_method=True)
    def bstack1ll1111l_opy_(cls, logs):
        for log in logs:
            bstack1llll11l11ll_opy_ = {
                bstack111l1l_opy_ (u"࠭࡫ࡪࡰࡧࠫ⇄"): bstack111l1l_opy_ (u"ࠧࡕࡇࡖࡘࡤࡒࡏࡈࠩ⇅"),
                bstack111l1l_opy_ (u"ࠨ࡮ࡨࡺࡪࡲࠧ⇆"): log[bstack111l1l_opy_ (u"ࠩ࡯ࡩࡻ࡫࡬ࠨ⇇")],
                bstack111l1l_opy_ (u"ࠪࡸ࡮ࡳࡥࡴࡶࡤࡱࡵ࠭⇈"): log[bstack111l1l_opy_ (u"ࠫࡹ࡯࡭ࡦࡵࡷࡥࡲࡶࠧ⇉")],
                bstack111l1l_opy_ (u"ࠬ࡮ࡴࡵࡲࡢࡶࡪࡹࡰࡰࡰࡶࡩࠬ⇊"): {},
                bstack111l1l_opy_ (u"࠭࡭ࡦࡵࡶࡥ࡬࡫ࠧ⇋"): log[bstack111l1l_opy_ (u"ࠧ࡮ࡧࡶࡷࡦ࡭ࡥࠨ⇌")],
            }
            if bstack111l1l_opy_ (u"ࠨࡶࡨࡷࡹࡥࡲࡶࡰࡢࡹࡺ࡯ࡤࠨ⇍") in log:
                bstack1llll11l11ll_opy_[bstack111l1l_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡳࡷࡱࡣࡺࡻࡩࡥࠩ⇎")] = log[bstack111l1l_opy_ (u"ࠪࡸࡪࡹࡴࡠࡴࡸࡲࡤࡻࡵࡪࡦࠪ⇏")]
            elif bstack111l1l_opy_ (u"ࠫ࡭ࡵ࡯࡬ࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠫ⇐") in log:
                bstack1llll11l11ll_opy_[bstack111l1l_opy_ (u"ࠬ࡮࡯ࡰ࡭ࡢࡶࡺࡴ࡟ࡶࡷ࡬ࡨࠬ⇑")] = log[bstack111l1l_opy_ (u"࠭ࡨࡰࡱ࡮ࡣࡷࡻ࡮ࡠࡷࡸ࡭ࡩ࠭⇒")]
            cls.bstack1lll1l1l_opy_({
                bstack111l1l_opy_ (u"ࠧࡦࡸࡨࡲࡹࡥࡴࡺࡲࡨࠫ⇓"): bstack111l1l_opy_ (u"ࠨࡎࡲ࡫ࡈࡸࡥࡢࡶࡨࡨࠬ⇔"),
                bstack111l1l_opy_ (u"ࠩ࡯ࡳ࡬ࡹࠧ⇕"): [bstack1llll11l11ll_opy_]
            })
    @classmethod
    @error_handler(class_method=True)
    def bstack1llll11l1l11_opy_(cls, steps):
        bstack1llll11lllll_opy_ = []
        for step in steps:
            bstack1llll11l11l1_opy_ = {
                bstack111l1l_opy_ (u"ࠪ࡯࡮ࡴࡤࠨ⇖"): bstack111l1l_opy_ (u"࡙ࠫࡋࡓࡕࡡࡖࡘࡊࡖࠧ⇗"),
                bstack111l1l_opy_ (u"ࠬࡲࡥࡷࡧ࡯ࠫ⇘"): step[bstack111l1l_opy_ (u"࠭࡬ࡦࡸࡨࡰࠬ⇙")],
                bstack111l1l_opy_ (u"ࠧࡵ࡫ࡰࡩࡸࡺࡡ࡮ࡲࠪ⇚"): step[bstack111l1l_opy_ (u"ࠨࡶ࡬ࡱࡪࡹࡴࡢ࡯ࡳࠫ⇛")],
                bstack111l1l_opy_ (u"ࠩࡰࡩࡸࡹࡡࡨࡧࠪ⇜"): step[bstack111l1l_opy_ (u"ࠪࡱࡪࡹࡳࡢࡩࡨࠫ⇝")],
                bstack111l1l_opy_ (u"ࠫࡩࡻࡲࡢࡶ࡬ࡳࡳ࠭⇞"): step[bstack111l1l_opy_ (u"ࠬࡪࡵࡳࡣࡷ࡭ࡴࡴࠧ⇟")]
            }
            if bstack111l1l_opy_ (u"࠭ࡴࡦࡵࡷࡣࡷࡻ࡮ࡠࡷࡸ࡭ࡩ࠭⇠") in step:
                bstack1llll11l11l1_opy_[bstack111l1l_opy_ (u"ࠧࡵࡧࡶࡸࡤࡸࡵ࡯ࡡࡸࡹ࡮ࡪࠧ⇡")] = step[bstack111l1l_opy_ (u"ࠨࡶࡨࡷࡹࡥࡲࡶࡰࡢࡹࡺ࡯ࡤࠨ⇢")]
            elif bstack111l1l_opy_ (u"ࠩ࡫ࡳࡴࡱ࡟ࡳࡷࡱࡣࡺࡻࡩࡥࠩ⇣") in step:
                bstack1llll11l11l1_opy_[bstack111l1l_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡠࡴࡸࡲࡤࡻࡵࡪࡦࠪ⇤")] = step[bstack111l1l_opy_ (u"ࠫ࡭ࡵ࡯࡬ࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠫ⇥")]
            bstack1llll11lllll_opy_.append(bstack1llll11l11l1_opy_)
        cls.bstack1lll1l1l_opy_({
            bstack111l1l_opy_ (u"ࠬ࡫ࡶࡦࡰࡷࡣࡹࡿࡰࡦࠩ⇦"): bstack111l1l_opy_ (u"࠭ࡌࡰࡩࡆࡶࡪࡧࡴࡦࡦࠪ⇧"),
            bstack111l1l_opy_ (u"ࠧ࡭ࡱࡪࡷࠬ⇨"): bstack1llll11lllll_opy_
        })
    @classmethod
    @error_handler(class_method=True)
    @measure(event_name=EVENTS.bstack11llll1111_opy_, stage=STAGE.bstack1ll1ll111_opy_)
    def bstack11111l1ll_opy_(cls, screenshot):
        cls.bstack1lll1l1l_opy_({
            bstack111l1l_opy_ (u"ࠨࡧࡹࡩࡳࡺ࡟ࡵࡻࡳࡩࠬ⇩"): bstack111l1l_opy_ (u"ࠩࡏࡳ࡬ࡉࡲࡦࡣࡷࡩࡩ࠭⇪"),
            bstack111l1l_opy_ (u"ࠪࡰࡴ࡭ࡳࠨ⇫"): [{
                bstack111l1l_opy_ (u"ࠫࡰ࡯࡮ࡥࠩ⇬"): bstack111l1l_opy_ (u"࡚ࠬࡅࡔࡖࡢࡗࡈࡘࡅࡆࡐࡖࡌࡔ࡚ࠧ⇭"),
                bstack111l1l_opy_ (u"࠭ࡴࡪ࡯ࡨࡷࡹࡧ࡭ࡱࠩ⇮"): datetime.datetime.utcnow().isoformat() + bstack111l1l_opy_ (u"࡛ࠧࠩ⇯"),
                bstack111l1l_opy_ (u"ࠨ࡯ࡨࡷࡸࡧࡧࡦࠩ⇰"): screenshot[bstack111l1l_opy_ (u"ࠩ࡬ࡱࡦ࡭ࡥࠨ⇱")],
                bstack111l1l_opy_ (u"ࠪࡸࡪࡹࡴࡠࡴࡸࡲࡤࡻࡵࡪࡦࠪ⇲"): screenshot[bstack111l1l_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠫ⇳")]
            }]
        }, event_url=bstack111l1l_opy_ (u"ࠬࡧࡰࡪ࠱ࡹ࠵࠴ࡹࡣࡳࡧࡨࡲࡸ࡮࡯ࡵࡵࠪ⇴"))
    @classmethod
    @error_handler(class_method=True)
    def bstack1l1l1111l1_opy_(cls, driver):
        current_test_uuid = cls.current_test_uuid()
        if not current_test_uuid:
            return
        cls.bstack1lll1l1l_opy_({
            bstack111l1l_opy_ (u"࠭ࡥࡷࡧࡱࡸࡤࡺࡹࡱࡧࠪ⇵"): bstack111l1l_opy_ (u"ࠧࡄࡄࡗࡗࡪࡹࡳࡪࡱࡱࡇࡷ࡫ࡡࡵࡧࡧࠫ⇶"),
            bstack111l1l_opy_ (u"ࠨࡶࡨࡷࡹࡥࡲࡶࡰࠪ⇷"): {
                bstack111l1l_opy_ (u"ࠤࡸࡹ࡮ࡪࠢ⇸"): cls.current_test_uuid(),
                bstack111l1l_opy_ (u"ࠥ࡭ࡳࡺࡥࡨࡴࡤࡸ࡮ࡵ࡮ࡴࠤ⇹"): cls.bstack1ll1l1ll_opy_(driver)
            }
        })
    @classmethod
    def bstack1l1l111l_opy_(cls, event: str, bstack1l1ll1l1_opy_: bstack11lll1ll_opy_):
        bstack1l111lll_opy_ = {
            bstack111l1l_opy_ (u"ࠫࡪࡼࡥ࡯ࡶࡢࡸࡾࡶࡥࠨ⇺"): event,
            bstack1l1ll1l1_opy_.event_key(): bstack1l1ll1l1_opy_.bstack11llll11_opy_(event)
        }
        cls.bstack1lll1l1l_opy_(bstack1l111lll_opy_)
        result = getattr(bstack1l1ll1l1_opy_, bstack111l1l_opy_ (u"ࠬࡸࡥࡴࡷ࡯ࡸࠬ⇻"), None)
        if event == bstack111l1l_opy_ (u"࠭ࡔࡦࡵࡷࡖࡺࡴࡓࡵࡣࡵࡸࡪࡪࠧ⇼"):
            threading.current_thread().bstackTestMeta = {bstack111l1l_opy_ (u"ࠧࡴࡶࡤࡸࡺࡹࠧ⇽"): bstack111l1l_opy_ (u"ࠨࡲࡨࡲࡩ࡯࡮ࡨࠩ⇾")}
        elif event == bstack111l1l_opy_ (u"ࠩࡗࡩࡸࡺࡒࡶࡰࡉ࡭ࡳ࡯ࡳࡩࡧࡧࠫ⇿"):
            threading.current_thread().bstackTestMeta = {bstack111l1l_opy_ (u"ࠪࡷࡹࡧࡴࡶࡵࠪ∀"): getattr(result, bstack111l1l_opy_ (u"ࠫࡷ࡫ࡳࡶ࡮ࡷࠫ∁"), bstack111l1l_opy_ (u"ࠬ࠭∂"))}
    @classmethod
    def on(cls):
        if (os.environ.get(bstack111l1l_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡊࡘࡖࠪ∃"), None) is None or os.environ[bstack111l1l_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡋ࡙ࡗࠫ∄")] == bstack111l1l_opy_ (u"ࠣࡰࡸࡰࡱࠨ∅")) and (os.environ.get(bstack111l1l_opy_ (u"ࠩࡅࡗࡤࡇ࠱࠲࡛ࡢࡎ࡜࡚ࠧ∆"), None) is None or os.environ[bstack111l1l_opy_ (u"ࠪࡆࡘࡥࡁ࠲࠳࡜ࡣࡏ࡝ࡔࠨ∇")] == bstack111l1l_opy_ (u"ࠦࡳࡻ࡬࡭ࠤ∈")):
            return False
        return True
    @staticmethod
    def bstack1llll11llll1_opy_(func):
        def wrap(*args, **kwargs):
            if bstack1l1l1111_opy_.on():
                return func(*args, **kwargs)
            return
        return wrap
    @staticmethod
    def default_headers():
        headers = {
            bstack111l1l_opy_ (u"ࠬࡉ࡯࡯ࡶࡨࡲࡹ࠳ࡔࡺࡲࡨࠫ∉"): bstack111l1l_opy_ (u"࠭ࡡࡱࡲ࡯࡭ࡨࡧࡴࡪࡱࡱ࠳࡯ࡹ࡯࡯ࠩ∊"),
            bstack111l1l_opy_ (u"࡙ࠧ࠯ࡅࡗ࡙ࡇࡃࡌ࠯ࡗࡉࡘ࡚ࡏࡑࡕࠪ∋"): bstack111l1l_opy_ (u"ࠨࡶࡵࡹࡪ࠭∌")
        }
        if os.environ.get(bstack111l1l_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡎࡕࡃࡡࡍ࡛࡙࠭∍"), None):
            headers[bstack111l1l_opy_ (u"ࠪࡅࡺࡺࡨࡰࡴ࡬ࡾࡦࡺࡩࡰࡰࠪ∎")] = bstack111l1l_opy_ (u"ࠫࡇ࡫ࡡࡳࡧࡵࠤࢀࢃࠧ∏").format(os.environ[bstack111l1l_opy_ (u"ࠧࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡊࡘࡆࡤࡐࡗࡕࠤ∐")])
        return headers
    @staticmethod
    def request_url(url):
        return bstack111l1l_opy_ (u"࠭ࡻࡾ࠱ࡾࢁࠬ∑").format(bstack1llll1l1111l_opy_, url)
    @staticmethod
    def current_test_uuid():
        return getattr(threading.current_thread(), bstack111l1l_opy_ (u"ࠧࡤࡷࡵࡶࡪࡴࡴࡠࡶࡨࡷࡹࡥࡵࡶ࡫ࡧࠫ−"), None)
    @staticmethod
    def bstack1ll1l1ll_opy_(driver):
        return {
            bstack111l1ll1111_opy_(): bstack1111l1ll11l_opy_(driver)
        }
    @staticmethod
    def bstack1llll11l1111_opy_(exception_info, report):
        return [{bstack111l1l_opy_ (u"ࠨࡤࡤࡧࡰࡺࡲࡢࡥࡨࠫ∓"): [exception_info.exconly(), report.longreprtext]}]
    @staticmethod
    def bstack1111111l1l_opy_(typename):
        if bstack111l1l_opy_ (u"ࠤࡄࡷࡸ࡫ࡲࡵ࡫ࡲࡲࠧ∔") in typename:
            return bstack111l1l_opy_ (u"ࠥࡅࡸࡹࡥࡳࡶ࡬ࡳࡳࡋࡲࡳࡱࡵࠦ∕")
        return bstack111l1l_opy_ (u"࡚ࠦࡴࡨࡢࡰࡧࡰࡪࡪࡅࡳࡴࡲࡶࠧ∖")