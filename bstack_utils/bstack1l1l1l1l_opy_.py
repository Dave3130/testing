# coding: UTF-8
import sys
bstack1111l1_opy_ = sys.version_info [0] == 2
bstack1l1ll11_opy_ = 2048
bstack11l11l_opy_ = 7
def bstack11111_opy_ (bstack11lll_opy_):
    global bstack111l1l1_opy_
    bstack1l1l1_opy_ = ord (bstack11lll_opy_ [-1])
    bstack1l111ll_opy_ = bstack11lll_opy_ [:-1]
    bstack1l1l11_opy_ = bstack1l1l1_opy_ % len (bstack1l111ll_opy_)
    bstack1l11l11_opy_ = bstack1l111ll_opy_ [:bstack1l1l11_opy_] + bstack1l111ll_opy_ [bstack1l1l11_opy_:]
    if bstack1111l1_opy_:
        bstack1llll11_opy_ = unicode () .join ([unichr (ord (char) - bstack1l1ll11_opy_ - (bstack1111ll1_opy_ + bstack1l1l1_opy_) % bstack11l11l_opy_) for bstack1111ll1_opy_, char in enumerate (bstack1l11l11_opy_)])
    else:
        bstack1llll11_opy_ = str () .join ([chr (ord (char) - bstack1l1ll11_opy_ - (bstack1111ll1_opy_ + bstack1l1l1_opy_) % bstack11l11l_opy_) for bstack1111ll1_opy_, char in enumerate (bstack1l11l11_opy_)])
    return eval (bstack1llll11_opy_)
import json
import logging
import os
import datetime
import threading
from bstack_utils.constants import EVENTS, STAGE
from bstack_utils.helper import bstack111l1l1111l_opy_, bstack11111llllll_opy_, bstack1111ll1lll_opy_, error_handler, bstack111l11llll1_opy_, bstack1111ll1lll1_opy_, bstack1111ll1ll11_opy_, bstack1l1lll11_opy_, bstack1lll1lll_opy_
from bstack_utils.measure import measure
from bstack_utils.bstack11l111ll11l_opy_ import bstack111l1lll1ll_opy_
import bstack_utils.bstack11l111l1l_opy_ as bstack1lll11llll_opy_
from bstack_utils.bstack1l1ll111_opy_ import bstack1l11lll1_opy_
import bstack_utils.accessibility as bstack111111l1_opy_
from bstack_utils.bstack11l1lll1l_opy_ import bstack11l1lll1l_opy_
from bstack_utils.bstack1ll1l11l_opy_ import bstack1llll11l_opy_
from bstack_utils.constants import bstack1l11111l11_opy_
bstack1llll111llll_opy_ = bstack11111_opy_ (u"ࠩ࡫ࡸࡹࡶࡳ࠻࠱࠲ࡧࡴࡲ࡬ࡦࡥࡷࡳࡷ࠳࡯ࡣࡵࡨࡶࡻࡧࡢࡪ࡮࡬ࡸࡾ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡩ࡯࡮ࠩ⅐")
logger = logging.getLogger(__name__)
class bstack11lllll1_opy_:
    bstack11l111ll11l_opy_ = None
    bs_config = None
    bstack1ll11llll1_opy_ = None
    @classmethod
    @error_handler(class_method=True)
    @measure(event_name=EVENTS.bstack11l1l111l1l_opy_, stage=STAGE.bstack111l1l11l_opy_)
    def launch(cls, bs_config, bstack1ll11llll1_opy_):
        cls.bs_config = bs_config
        cls.bstack1ll11llll1_opy_ = bstack1ll11llll1_opy_
        try:
            cls.bstack1llll11l111l_opy_()
            bstack1llll1ll1lll_opy_ = bstack111l1l1111l_opy_(bs_config)
            bstack1llll1l1llll_opy_ = bstack11111llllll_opy_(bs_config)
            data = bstack1lll11llll_opy_.bstack1llll11llll1_opy_(bs_config, bstack1ll11llll1_opy_)
            config = {
                bstack11111_opy_ (u"ࠪࡥࡺࡺࡨࠨ⅑"): (bstack1llll1ll1lll_opy_, bstack1llll1l1llll_opy_),
                bstack11111_opy_ (u"ࠫ࡭࡫ࡡࡥࡧࡵࡷࠬ⅒"): cls.default_headers()
            }
            response = bstack1111ll1lll_opy_(bstack11111_opy_ (u"ࠬࡖࡏࡔࡖࠪ⅓"), cls.request_url(bstack11111_opy_ (u"࠭ࡡࡱ࡫࠲ࡺ࠷࠵ࡢࡶ࡫࡯ࡨࡸ࠭⅔")), data, config)
            if response.status_code != 200:
                bstack11lll11l11_opy_ = response.json()
                if bstack11lll11l11_opy_[bstack11111_opy_ (u"ࠧࡴࡷࡦࡧࡪࡹࡳࠨ⅕")] == False:
                    cls.bstack1llll111l1l1_opy_(bstack11lll11l11_opy_)
                    return
                cls.bstack1llll11ll1l1_opy_(bstack11lll11l11_opy_[bstack11111_opy_ (u"ࠨࡱࡥࡷࡪࡸࡶࡢࡤ࡬ࡰ࡮ࡺࡹࠨ⅖")])
                cls.bstack1llll11lll1l_opy_(bstack11lll11l11_opy_[bstack11111_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠩ⅗")])
                return None
            bstack1llll111l111_opy_ = cls.bstack1llll11l1111_opy_(response)
            return bstack1llll111l111_opy_, response.json()
        except Exception as error:
            logger.error(bstack11111_opy_ (u"ࠥࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡷࡩ࡫࡯ࡩࠥࡩࡲࡦࡣࡷ࡭ࡳ࡭ࠠࡣࡷ࡬ࡰࡩࠦࡦࡰࡴࠣࡘࡪࡹࡴࡉࡷࡥ࠾ࠥࢁࡽࠣ⅘").format(str(error)))
            return None
    @classmethod
    @error_handler(class_method=True)
    def stop(cls, bstack1llll111l11l_opy_=None):
        if not bstack1l11lll1_opy_.on() and not bstack111111l1_opy_.on():
            return
        if os.environ.get(bstack11111_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡉࡗࡅࡣࡏ࡝ࡔࠨ⅙")) == bstack11111_opy_ (u"ࠧࡴࡵ࡭࡮ࠥ⅚") or os.environ.get(bstack11111_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡕࡖࡋࡇࠫ⅛")) == bstack11111_opy_ (u"ࠢ࡯ࡷ࡯ࡰࠧ⅜"):
            logger.error(bstack11111_opy_ (u"ࠨࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡴࡶࡲࡴࠥࡨࡵࡪ࡮ࡧࠤࡷ࡫ࡱࡶࡧࡶࡸࠥࡺ࡯ࠡࡖࡨࡷࡹࡎࡵࡣ࠼ࠣࡑ࡮ࡹࡳࡪࡰࡪࠤࡦࡻࡴࡩࡧࡱࡸ࡮ࡩࡡࡵ࡫ࡲࡲࠥࡺ࡯࡬ࡧࡱࠫ⅝"))
            return {
                bstack11111_opy_ (u"ࠩࡶࡸࡦࡺࡵࡴࠩ⅞"): bstack11111_opy_ (u"ࠪࡩࡷࡸ࡯ࡳࠩ⅟"),
                bstack11111_opy_ (u"ࠫࡲ࡫ࡳࡴࡣࡪࡩࠬⅠ"): bstack11111_opy_ (u"࡚ࠬ࡯࡬ࡧࡱ࠳ࡧࡻࡩ࡭ࡦࡌࡈࠥ࡯ࡳࠡࡷࡱࡨࡪ࡬ࡩ࡯ࡧࡧ࠰ࠥࡨࡵࡪ࡮ࡧࠤࡨࡸࡥࡢࡶ࡬ࡳࡳࠦ࡭ࡪࡩ࡫ࡸࠥ࡮ࡡࡷࡧࠣࡪࡦ࡯࡬ࡦࡦࠪⅡ")
            }
        try:
            cls.bstack11l111ll11l_opy_.shutdown()
            data = {
                bstack11111_opy_ (u"࠭ࡦࡪࡰ࡬ࡷ࡭࡫ࡤࡠࡣࡷࠫⅢ"): bstack1l1lll11_opy_()
            }
            if not bstack1llll111l11l_opy_ is None:
                data[bstack11111_opy_ (u"ࠧࡧ࡫ࡱ࡭ࡸ࡮ࡥࡥࡡࡰࡩࡹࡧࡤࡢࡶࡤࠫⅣ")] = [{
                    bstack11111_opy_ (u"ࠨࡴࡨࡥࡸࡵ࡮ࠨⅤ"): bstack11111_opy_ (u"ࠩࡸࡷࡪࡸ࡟࡬࡫࡯ࡰࡪࡪࠧⅥ"),
                    bstack11111_opy_ (u"ࠪࡷ࡮࡭࡮ࡢ࡮ࠪⅦ"): bstack1llll111l11l_opy_
                }]
            config = {
                bstack11111_opy_ (u"ࠫ࡭࡫ࡡࡥࡧࡵࡷࠬⅧ"): cls.default_headers()
            }
            bstack11ll111l11l_opy_ = bstack11111_opy_ (u"ࠬࡧࡰࡪ࠱ࡹ࠵࠴ࡨࡵࡪ࡮ࡧࡷ࠴ࢁࡽ࠰ࡵࡷࡳࡵ࠭Ⅸ").format(os.environ[bstack11111_opy_ (u"ࠨࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡕࡖࡋࡇࠦⅩ")])
            bstack1llll1111lll_opy_ = cls.request_url(bstack11ll111l11l_opy_)
            response = bstack1111ll1lll_opy_(bstack11111_opy_ (u"ࠧࡑࡗࡗࠫⅪ"), bstack1llll1111lll_opy_, data, config)
            if not response.ok:
                raise Exception(bstack11111_opy_ (u"ࠣࡕࡷࡳࡵࠦࡲࡦࡳࡸࡩࡸࡺࠠ࡯ࡱࡷࠤࡴࡱࠢⅫ"))
        except Exception as error:
            logger.error(bstack11111_opy_ (u"ࠤࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࡯࡮ࠡࡵࡷࡳࡵࠦࡢࡶ࡫࡯ࡨࠥࡸࡥࡲࡷࡨࡷࡹࠦࡴࡰࠢࡗࡩࡸࡺࡈࡶࡤ࠽࠾ࠥࠨⅬ") + str(error))
            return {
                bstack11111_opy_ (u"ࠪࡷࡹࡧࡴࡶࡵࠪⅭ"): bstack11111_opy_ (u"ࠫࡪࡸࡲࡰࡴࠪⅮ"),
                bstack11111_opy_ (u"ࠬࡳࡥࡴࡵࡤ࡫ࡪ࠭Ⅿ"): str(error)
            }
    @classmethod
    @error_handler(class_method=True)
    def bstack1llll11l1111_opy_(cls, response):
        bstack11lll11l11_opy_ = response.json() if not isinstance(response, dict) else response
        bstack1llll111l111_opy_ = {}
        if bstack11lll11l11_opy_.get(bstack11111_opy_ (u"࠭ࡪࡸࡶࠪⅰ")) is None:
            os.environ[bstack11111_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡋ࡙ࡗࠫⅱ")] = bstack11111_opy_ (u"ࠨࡰࡸࡰࡱ࠭ⅲ")
        else:
            os.environ[bstack11111_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡎࡕࡃࡡࡍ࡛࡙࠭ⅳ")] = bstack11lll11l11_opy_.get(bstack11111_opy_ (u"ࠪ࡮ࡼࡺࠧⅴ"), bstack11111_opy_ (u"ࠫࡳࡻ࡬࡭ࠩⅵ"))
        os.environ[bstack11111_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡊࡘࡆࡤ࡛ࡕࡊࡆࠪⅶ")] = bstack11lll11l11_opy_.get(bstack11111_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡤ࡮ࡡࡴࡪࡨࡨࡤ࡯ࡤࠨⅷ"), bstack11111_opy_ (u"ࠧ࡯ࡷ࡯ࡰࠬⅸ"))
        logger.info(bstack11111_opy_ (u"ࠨࡖࡨࡷࡹ࡮ࡵࡣࠢࡶࡸࡦࡸࡴࡦࡦࠣࡻ࡮ࡺࡨࠡ࡫ࡧ࠾ࠥ࠭ⅹ") + os.getenv(bstack11111_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡎࡕࡃࡡࡘ࡙ࡎࡊࠧⅺ")));
        if bstack1l11lll1_opy_.bstack11l111ll1l1_opy_(cls.bs_config, cls.bstack1ll11llll1_opy_.get(bstack11111_opy_ (u"ࠪࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡥࡵࡴࡧࡧࠫⅻ"), bstack11111_opy_ (u"ࠫࠬⅼ"))) is True:
            bstack11ll111111l_opy_, build_hashed_id, bstack1llll11ll11l_opy_ = cls.bstack1llll11l11l1_opy_(bstack11lll11l11_opy_)
            if bstack11ll111111l_opy_ != None and build_hashed_id != None:
                bstack1llll111l111_opy_[bstack11111_opy_ (u"ࠬࡵࡢࡴࡧࡵࡺࡦࡨࡩ࡭࡫ࡷࡽࠬⅽ")] = {
                    bstack11111_opy_ (u"࠭ࡪࡸࡶࡢࡸࡴࡱࡥ࡯ࠩⅾ"): bstack11ll111111l_opy_,
                    bstack11111_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡥࡨࡢࡵ࡫ࡩࡩࡥࡩࡥࠩⅿ"): build_hashed_id,
                    bstack11111_opy_ (u"ࠨࡣ࡯ࡰࡴࡽ࡟ࡴࡥࡵࡩࡪࡴࡳࡩࡱࡷࡷࠬↀ"): bstack1llll11ll11l_opy_
                }
            else:
                bstack1llll111l111_opy_[bstack11111_opy_ (u"ࠩࡲࡦࡸ࡫ࡲࡷࡣࡥ࡭ࡱ࡯ࡴࡺࠩↁ")] = {}
        else:
            bstack1llll111l111_opy_[bstack11111_opy_ (u"ࠪࡳࡧࡹࡥࡳࡸࡤࡦ࡮ࡲࡩࡵࡻࠪↂ")] = {}
        bstack1llll111lll1_opy_, build_hashed_id = cls.bstack1llll11ll111_opy_(bstack11lll11l11_opy_)
        if bstack1llll111lll1_opy_ != None and build_hashed_id != None:
            bstack1llll111l111_opy_[bstack11111_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠫↃ")] = {
                bstack11111_opy_ (u"ࠬࡧࡵࡵࡪࡢࡸࡴࡱࡥ࡯ࠩↄ"): bstack1llll111lll1_opy_,
                bstack11111_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡤ࡮ࡡࡴࡪࡨࡨࡤ࡯ࡤࠨↅ"): build_hashed_id,
            }
        else:
            bstack1llll111l111_opy_[bstack11111_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠧↆ")] = {}
        if bstack1llll111l111_opy_[bstack11111_opy_ (u"ࠨࡱࡥࡷࡪࡸࡶࡢࡤ࡬ࡰ࡮ࡺࡹࠨↇ")].get(bstack11111_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡠࡪࡤࡷ࡭࡫ࡤࡠ࡫ࡧࠫↈ")) != None or bstack1llll111l111_opy_[bstack11111_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠪ↉")].get(bstack11111_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡢ࡬ࡦࡹࡨࡦࡦࡢ࡭ࡩ࠭↊")) != None:
            cls.bstack1llll111l1ll_opy_(bstack11lll11l11_opy_.get(bstack11111_opy_ (u"ࠬࡰࡷࡵࠩ↋")), bstack11lll11l11_opy_.get(bstack11111_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡤ࡮ࡡࡴࡪࡨࡨࡤ࡯ࡤࠨ↌")))
        return bstack1llll111l111_opy_
    @classmethod
    def bstack1llll11l11l1_opy_(cls, bstack11lll11l11_opy_):
        if bstack11lll11l11_opy_.get(bstack11111_opy_ (u"ࠧࡰࡤࡶࡩࡷࡼࡡࡣ࡫࡯࡭ࡹࡿࠧ↍")) == None:
            cls.bstack1llll11ll1l1_opy_()
            return [None, None, None]
        if bstack11lll11l11_opy_[bstack11111_opy_ (u"ࠨࡱࡥࡷࡪࡸࡶࡢࡤ࡬ࡰ࡮ࡺࡹࠨ↎")][bstack11111_opy_ (u"ࠩࡶࡹࡨࡩࡥࡴࡵࠪ↏")] != True:
            cls.bstack1llll11ll1l1_opy_(bstack11lll11l11_opy_[bstack11111_opy_ (u"ࠪࡳࡧࡹࡥࡳࡸࡤࡦ࡮ࡲࡩࡵࡻࠪ←")])
            return [None, None, None]
        logger.debug(bstack11111_opy_ (u"ࠫࢀࢃࠠࡃࡷ࡬ࡰࡩࠦࡣࡳࡧࡤࡸ࡮ࡵ࡮ࠡࡕࡸࡧࡨ࡫ࡳࡴࡨࡸࡰࠦ࠭↑").format(bstack1l11111l11_opy_))
        os.environ[bstack11111_opy_ (u"ࠬࡈࡓࡠࡖࡈࡗ࡙ࡕࡐࡔࡡࡅ࡙ࡎࡒࡄࡠࡅࡒࡑࡕࡒࡅࡕࡇࡇࠫ→")] = bstack11111_opy_ (u"࠭ࡴࡳࡷࡨࠫ↓")
        if bstack11lll11l11_opy_.get(bstack11111_opy_ (u"ࠧ࡫ࡹࡷࠫ↔")):
            os.environ[bstack11111_opy_ (u"ࠨࡅࡕࡉࡉࡋࡎࡕࡋࡄࡐࡘࡥࡆࡐࡔࡢࡇࡗࡇࡓࡉࡡࡕࡉࡕࡕࡒࡕࡋࡑࡋࠬ↕")] = json.dumps({
                bstack11111_opy_ (u"ࠩࡸࡷࡪࡸ࡮ࡢ࡯ࡨࠫ↖"): bstack111l1l1111l_opy_(cls.bs_config),
                bstack11111_opy_ (u"ࠪࡴࡦࡹࡳࡸࡱࡵࡨࠬ↗"): bstack11111llllll_opy_(cls.bs_config)
            })
        if bstack11lll11l11_opy_.get(bstack11111_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡢ࡬ࡦࡹࡨࡦࡦࡢ࡭ࡩ࠭↘")):
            os.environ[bstack11111_opy_ (u"ࠬࡈࡓࡠࡖࡈࡗ࡙ࡕࡐࡔࡡࡅ࡙ࡎࡒࡄࡠࡊࡄࡗࡍࡋࡄࡠࡋࡇࠫ↙")] = bstack11lll11l11_opy_[bstack11111_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡤ࡮ࡡࡴࡪࡨࡨࡤ࡯ࡤࠨ↚")]
        if bstack11lll11l11_opy_[bstack11111_opy_ (u"ࠧࡰࡤࡶࡩࡷࡼࡡࡣ࡫࡯࡭ࡹࡿࠧ↛")].get(bstack11111_opy_ (u"ࠨࡱࡳࡸ࡮ࡵ࡮ࡴࠩ↜"), {}).get(bstack11111_opy_ (u"ࠩࡤࡰࡱࡵࡷࡠࡵࡦࡶࡪ࡫࡮ࡴࡪࡲࡸࡸ࠭↝")):
            os.environ[bstack11111_opy_ (u"ࠪࡆࡘࡥࡔࡆࡕࡗࡓࡕ࡙࡟ࡂࡎࡏࡓ࡜ࡥࡓࡄࡔࡈࡉࡓ࡙ࡈࡐࡖࡖࠫ↞")] = str(bstack11lll11l11_opy_[bstack11111_opy_ (u"ࠫࡴࡨࡳࡦࡴࡹࡥࡧ࡯࡬ࡪࡶࡼࠫ↟")][bstack11111_opy_ (u"ࠬࡵࡰࡵ࡫ࡲࡲࡸ࠭↠")][bstack11111_opy_ (u"࠭ࡡ࡭࡮ࡲࡻࡤࡹࡣࡳࡧࡨࡲࡸ࡮࡯ࡵࡵࠪ↡")])
        else:
            os.environ[bstack11111_opy_ (u"ࠧࡃࡕࡢࡘࡊ࡙ࡔࡐࡒࡖࡣࡆࡒࡌࡐ࡙ࡢࡗࡈࡘࡅࡆࡐࡖࡌࡔ࡚ࡓࠨ↢")] = bstack11111_opy_ (u"ࠣࡰࡸࡰࡱࠨ↣")
        return [bstack11lll11l11_opy_[bstack11111_opy_ (u"ࠩ࡭ࡻࡹ࠭↤")], bstack11lll11l11_opy_[bstack11111_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡡ࡫ࡥࡸ࡮ࡥࡥࡡ࡬ࡨࠬ↥")], os.environ[bstack11111_opy_ (u"ࠫࡇ࡙࡟ࡕࡇࡖࡘࡔࡖࡓࡠࡃࡏࡐࡔ࡝࡟ࡔࡅࡕࡉࡊࡔࡓࡉࡑࡗࡗࠬ↦")]]
    @classmethod
    def bstack1llll11ll111_opy_(cls, bstack11lll11l11_opy_):
        if bstack11lll11l11_opy_.get(bstack11111_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠬ↧")) == None:
            cls.bstack1llll11lll1l_opy_()
            return [None, None]
        if bstack11lll11l11_opy_[bstack11111_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾ࠭↨")][bstack11111_opy_ (u"ࠧࡴࡷࡦࡧࡪࡹࡳࠨ↩")] != True:
            cls.bstack1llll11lll1l_opy_(bstack11lll11l11_opy_[bstack11111_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠨ↪")])
            return [None, None]
        if bstack11lll11l11_opy_[bstack11111_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠩ↫")].get(bstack11111_opy_ (u"ࠪࡳࡵࡺࡩࡰࡰࡶࠫ↬")):
            logger.debug(bstack11111_opy_ (u"࡙ࠫ࡫ࡳࡵࠢࡄࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡅࡹ࡮ࡲࡤࠡࡥࡵࡩࡦࡺࡩࡰࡰࠣࡗࡺࡩࡣࡦࡵࡶࡪࡺࡲࠡࠨ↭"))
            parsed = json.loads(os.getenv(bstack11111_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡡࡄࡇࡈࡋࡓࡔࡋࡅࡍࡑࡏࡔ࡚ࡡࡆࡓࡓࡌࡉࡈࡗࡕࡅ࡙ࡏࡏࡏࡡ࡜ࡑࡑ࠭↮"), bstack11111_opy_ (u"࠭ࡻࡾࠩ↯")))
            capabilities = bstack1lll11llll_opy_.bstack1llll11l1l1l_opy_(bstack11lll11l11_opy_[bstack11111_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠧ↰")][bstack11111_opy_ (u"ࠨࡱࡳࡸ࡮ࡵ࡮ࡴࠩ↱")][bstack11111_opy_ (u"ࠩࡦࡥࡵࡧࡢࡪ࡮࡬ࡸ࡮࡫ࡳࠨ↲")], bstack11111_opy_ (u"ࠪࡲࡦࡳࡥࠨ↳"), bstack11111_opy_ (u"ࠫࡻࡧ࡬ࡶࡧࠪ↴"))
            bstack1llll111lll1_opy_ = capabilities[bstack11111_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽ࡙ࡵ࡫ࡦࡰࠪ↵")]
            os.environ[bstack11111_opy_ (u"࠭ࡂࡔࡡࡄ࠵࠶࡟࡟ࡋ࡙ࡗࠫ↶")] = bstack1llll111lll1_opy_
            if bstack11111_opy_ (u"ࠢࡢࡷࡷࡳࡲࡧࡴࡦࠤ↷") in bstack11lll11l11_opy_ and bstack11lll11l11_opy_.get(bstack11111_opy_ (u"ࠣࡣࡳࡴࡤࡧࡵࡵࡱࡰࡥࡹ࡫ࠢ↸")) is None:
                parsed[bstack11111_opy_ (u"ࠩࡶࡧࡦࡴ࡮ࡦࡴ࡙ࡩࡷࡹࡩࡰࡰࠪ↹")] = capabilities[bstack11111_opy_ (u"ࠪࡷࡨࡧ࡮࡯ࡧࡵ࡚ࡪࡸࡳࡪࡱࡱࠫ↺")]
            os.environ[bstack11111_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡠࡃࡆࡇࡊ࡙ࡓࡊࡄࡌࡐࡎ࡚࡙ࡠࡅࡒࡒࡋࡏࡇࡖࡔࡄࡘࡎࡕࡎࡠ࡛ࡐࡐࠬ↻")] = json.dumps(parsed)
            scripts = bstack1lll11llll_opy_.bstack1llll11l1l1l_opy_(bstack11lll11l11_opy_[bstack11111_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠬ↼")][bstack11111_opy_ (u"࠭࡯ࡱࡶ࡬ࡳࡳࡹࠧ↽")][bstack11111_opy_ (u"ࠧࡴࡥࡵ࡭ࡵࡺࡳࠨ↾")], bstack11111_opy_ (u"ࠨࡰࡤࡱࡪ࠭↿"), bstack11111_opy_ (u"ࠩࡦࡳࡲࡳࡡ࡯ࡦࠪ⇀"))
            bstack11l1lll1l_opy_.bstack1l1lll11l_opy_(scripts)
            commands = bstack11lll11l11_opy_[bstack11111_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠪ⇁")][bstack11111_opy_ (u"ࠫࡴࡶࡴࡪࡱࡱࡷࠬ⇂")][bstack11111_opy_ (u"ࠬࡩ࡯࡮࡯ࡤࡲࡩࡹࡔࡰ࡙ࡵࡥࡵ࠭⇃")].get(bstack11111_opy_ (u"࠭ࡣࡰ࡯ࡰࡥࡳࡪࡳࠨ⇄"))
            bstack11l1lll1l_opy_.bstack1lllll11111l_opy_(commands)
            bstack1lllll1111ll_opy_ = capabilities.get(bstack11111_opy_ (u"ࠧࡨࡱࡲ࡫࠿ࡩࡨࡳࡱࡰࡩࡔࡶࡴࡪࡱࡱࡷࠬ⇅"))
            bstack11l1lll1l_opy_.bstack1llll1llll11_opy_(bstack1lllll1111ll_opy_)
            bstack11l1lll1l_opy_.store()
        return [bstack1llll111lll1_opy_, bstack11lll11l11_opy_[bstack11111_opy_ (u"ࠨࡤࡸ࡭ࡱࡪ࡟ࡩࡣࡶ࡬ࡪࡪ࡟ࡪࡦࠪ⇆")]]
    @classmethod
    def bstack1llll11ll1l1_opy_(cls, response=None):
        os.environ[bstack11111_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡎࡕࡃࡡࡘ࡙ࡎࡊࠧ⇇")] = bstack11111_opy_ (u"ࠪࡲࡺࡲ࡬ࠨ⇈")
        os.environ[bstack11111_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡉࡗࡅࡣࡏ࡝ࡔࠨ⇉")] = bstack11111_opy_ (u"ࠬࡴࡵ࡭࡮ࠪ⇊")
        os.environ[bstack11111_opy_ (u"࠭ࡂࡔࡡࡗࡉࡘ࡚ࡏࡑࡕࡢࡆ࡚ࡏࡌࡅࡡࡆࡓࡒࡖࡌࡆࡖࡈࡈࠬ⇋")] = bstack11111_opy_ (u"ࠧࡧࡣ࡯ࡷࡪ࠭⇌")
        os.environ[bstack11111_opy_ (u"ࠨࡄࡖࡣ࡙ࡋࡓࡕࡑࡓࡗࡤࡈࡕࡊࡎࡇࡣࡍࡇࡓࡉࡇࡇࡣࡎࡊࠧ⇍")] = bstack11111_opy_ (u"ࠤࡱࡹࡱࡲࠢ⇎")
        os.environ[bstack11111_opy_ (u"ࠪࡆࡘࡥࡔࡆࡕࡗࡓࡕ࡙࡟ࡂࡎࡏࡓ࡜ࡥࡓࡄࡔࡈࡉࡓ࡙ࡈࡐࡖࡖࠫ⇏")] = bstack11111_opy_ (u"ࠦࡳࡻ࡬࡭ࠤ⇐")
        cls.bstack1llll111l1l1_opy_(response, bstack11111_opy_ (u"ࠧࡵࡢࡴࡧࡵࡺࡦࡨࡩ࡭࡫ࡷࡽࠧ⇑"))
        return [None, None, None]
    @classmethod
    def bstack1llll11lll1l_opy_(cls, response=None):
        os.environ[bstack11111_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡕࡖࡋࡇࠫ⇒")] = bstack11111_opy_ (u"ࠧ࡯ࡷ࡯ࡰࠬ⇓")
        os.environ[bstack11111_opy_ (u"ࠨࡄࡖࡣࡆ࠷࠱࡚ࡡࡍ࡛࡙࠭⇔")] = bstack11111_opy_ (u"ࠩࡱࡹࡱࡲࠧ⇕")
        os.environ[bstack11111_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚ࡈࡖࡄࡢࡎ࡜࡚ࠧ⇖")] = bstack11111_opy_ (u"ࠫࡳࡻ࡬࡭ࠩ⇗")
        cls.bstack1llll111l1l1_opy_(response, bstack11111_opy_ (u"ࠧࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠧ⇘"))
        return [None, None, None]
    @classmethod
    def bstack1llll111l1ll_opy_(cls, jwt, build_hashed_id):
        os.environ[bstack11111_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡊࡘࡖࠪ⇙")] = jwt
        os.environ[bstack11111_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡖࡗࡌࡈࠬ⇚")] = build_hashed_id
    @classmethod
    def bstack1llll111l1l1_opy_(cls, response=None, product=bstack11111_opy_ (u"ࠣࠤ⇛")):
        if response == None or response.get(bstack11111_opy_ (u"ࠩࡨࡶࡷࡵࡲࡴࠩ⇜")) == None:
            logger.error(product + bstack11111_opy_ (u"ࠥࠤࡇࡻࡩ࡭ࡦࠣࡧࡷ࡫ࡡࡵ࡫ࡲࡲࠥ࡬ࡡࡪ࡮ࡨࡨࠧ⇝"))
            return
        for error in response[bstack11111_opy_ (u"ࠫࡪࡸࡲࡰࡴࡶࠫ⇞")]:
            bstack1111llll111_opy_ = error[bstack11111_opy_ (u"ࠬࡱࡥࡺࠩ⇟")]
            error_message = error[bstack11111_opy_ (u"࠭࡭ࡦࡵࡶࡥ࡬࡫ࠧ⇠")]
            if error_message:
                if bstack1111llll111_opy_ == bstack11111_opy_ (u"ࠢࡆࡔࡕࡓࡗࡥࡁࡄࡅࡈࡗࡘࡥࡄࡆࡐࡌࡉࡉࠨ⇡"):
                    logger.info(error_message)
                else:
                    logger.error(error_message)
            else:
                logger.error(bstack11111_opy_ (u"ࠣࡆࡤࡸࡦࠦࡵࡱ࡮ࡲࡥࡩࠦࡴࡰࠢࡅࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࠡࠤ⇢") + product + bstack11111_opy_ (u"ࠤࠣࡪࡦ࡯࡬ࡦࡦࠣࡨࡺ࡫ࠠࡵࡱࠣࡷࡴࡳࡥࠡࡧࡵࡶࡴࡸࠢ⇣"))
    @classmethod
    def bstack1llll11l111l_opy_(cls):
        if cls.bstack11l111ll11l_opy_ is not None:
            return
        cls.bstack11l111ll11l_opy_ = bstack111l1lll1ll_opy_(cls.post_data)
        cls.bstack11l111ll11l_opy_.start()
    @classmethod
    def bstack1lll1111_opy_(cls):
        if cls.bstack11l111ll11l_opy_ is None:
            return
        cls.bstack11l111ll11l_opy_.shutdown()
    @classmethod
    @error_handler(class_method=True)
    def post_data(cls, bstack1l111111_opy_, event_url=bstack11111_opy_ (u"ࠪࡥࡵ࡯࠯ࡷ࠳࠲ࡦࡦࡺࡣࡩࠩ⇤")):
        config = {
            bstack11111_opy_ (u"ࠫ࡭࡫ࡡࡥࡧࡵࡷࠬ⇥"): cls.default_headers()
        }
        logger.debug(bstack11111_opy_ (u"ࠧࡶ࡯ࡴࡶࡢࡨࡦࡺࡡ࠻ࠢࡖࡩࡳࡪࡩ࡯ࡩࠣࡨࡦࡺࡡࠡࡶࡲࠤࡹ࡫ࡳࡵࡪࡸࡦࠥ࡬࡯ࡳࠢࡨࡺࡪࡴࡴࡴࠢࡾࢁࠧ⇦").format(bstack11111_opy_ (u"࠭ࠬࠡࠩ⇧").join([event[bstack11111_opy_ (u"ࠧࡦࡸࡨࡲࡹࡥࡴࡺࡲࡨࠫ⇨")] for event in bstack1l111111_opy_])))
        response = bstack1111ll1lll_opy_(bstack11111_opy_ (u"ࠨࡒࡒࡗ࡙࠭⇩"), cls.request_url(event_url), bstack1l111111_opy_, config)
        bstack1llll1lll111_opy_ = response.json()
    @classmethod
    def bstack1l1l1l11_opy_(cls, bstack1l111111_opy_, event_url=bstack11111_opy_ (u"ࠩࡤࡴ࡮࠵ࡶ࠲࠱ࡥࡥࡹࡩࡨࠨ⇪")):
        logger.debug(bstack11111_opy_ (u"ࠥࡷࡪࡴࡤࡠࡦࡤࡸࡦࡀࠠࡂࡶࡷࡩࡲࡶࡴࡪࡰࡪࠤࡹࡵࠠࡢࡦࡧࠤࡩࡧࡴࡢࠢࡷࡳࠥࡨࡡࡵࡥ࡫ࠤࡼ࡯ࡴࡩࠢࡨࡺࡪࡴࡴࡠࡶࡼࡴࡪࡀࠠࡼࡿࠥ⇫").format(bstack1l111111_opy_[bstack11111_opy_ (u"ࠫࡪࡼࡥ࡯ࡶࡢࡸࡾࡶࡥࠨ⇬")]))
        if not bstack1lll11llll_opy_.bstack1llll11l1l11_opy_(bstack1l111111_opy_[bstack11111_opy_ (u"ࠬ࡫ࡶࡦࡰࡷࡣࡹࡿࡰࡦࠩ⇭")]):
            logger.debug(bstack11111_opy_ (u"ࠨࡳࡦࡰࡧࡣࡩࡧࡴࡢ࠼ࠣࡒࡴࡺࠠࡢࡦࡧ࡭ࡳ࡭ࠠࡥࡣࡷࡥࠥࡽࡩࡵࡪࠣࡩࡻ࡫࡮ࡵࡡࡷࡽࡵ࡫࠺ࠡࡽࢀࠦ⇮").format(bstack1l111111_opy_[bstack11111_opy_ (u"ࠧࡦࡸࡨࡲࡹࡥࡴࡺࡲࡨࠫ⇯")]))
            return
        bstack1l11ll1ll1_opy_ = bstack1lll11llll_opy_.bstack1llll111ll11_opy_(bstack1l111111_opy_[bstack11111_opy_ (u"ࠨࡧࡹࡩࡳࡺ࡟ࡵࡻࡳࡩࠬ⇰")], bstack1l111111_opy_.get(bstack11111_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡳࡷࡱࠫ⇱")))
        if bstack1l11ll1ll1_opy_ != None:
            if bstack1l111111_opy_.get(bstack11111_opy_ (u"ࠪࡸࡪࡹࡴࡠࡴࡸࡲࠬ⇲")) != None:
                bstack1l111111_opy_[bstack11111_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡵࡹࡳ࠭⇳")][bstack11111_opy_ (u"ࠬࡶࡲࡰࡦࡸࡧࡹࡥ࡭ࡢࡲࠪ⇴")] = bstack1l11ll1ll1_opy_
            else:
                bstack1l111111_opy_[bstack11111_opy_ (u"࠭ࡰࡳࡱࡧࡹࡨࡺ࡟࡮ࡣࡳࠫ⇵")] = bstack1l11ll1ll1_opy_
        if event_url == bstack11111_opy_ (u"ࠧࡢࡲ࡬࠳ࡻ࠷࠯ࡣࡣࡷࡧ࡭࠭⇶"):
            cls.bstack1llll11l111l_opy_()
            logger.debug(bstack11111_opy_ (u"ࠣࡵࡨࡲࡩࡥࡤࡢࡶࡤ࠾ࠥࡇࡤࡥ࡫ࡱ࡫ࠥࡪࡡࡵࡣࠣࡸࡴࠦࡢࡢࡶࡦ࡬ࠥࡽࡩࡵࡪࠣࡩࡻ࡫࡮ࡵࡡࡷࡽࡵ࡫࠺ࠡࡽࢀࠦ⇷").format(bstack1l111111_opy_[bstack11111_opy_ (u"ࠩࡨࡺࡪࡴࡴࡠࡶࡼࡴࡪ࠭⇸")]))
            cls.bstack11l111ll11l_opy_.add(bstack1l111111_opy_)
        elif event_url == bstack11111_opy_ (u"ࠪࡥࡵ࡯࠯ࡷ࠳࠲ࡷࡨࡸࡥࡦࡰࡶ࡬ࡴࡺࡳࠨ⇹"):
            cls.post_data([bstack1l111111_opy_], event_url)
    @classmethod
    @error_handler(class_method=True)
    def bstack1l11l1ll_opy_(cls, logs):
        for log in logs:
            bstack1llll11l1ll1_opy_ = {
                bstack11111_opy_ (u"ࠫࡰ࡯࡮ࡥࠩ⇺"): bstack11111_opy_ (u"࡚ࠬࡅࡔࡖࡢࡐࡔࡍࠧ⇻"),
                bstack11111_opy_ (u"࠭࡬ࡦࡸࡨࡰࠬ⇼"): log[bstack11111_opy_ (u"ࠧ࡭ࡧࡹࡩࡱ࠭⇽")],
                bstack11111_opy_ (u"ࠨࡶ࡬ࡱࡪࡹࡴࡢ࡯ࡳࠫ⇾"): log[bstack11111_opy_ (u"ࠩࡷ࡭ࡲ࡫ࡳࡵࡣࡰࡴࠬ⇿")],
                bstack11111_opy_ (u"ࠪ࡬ࡹࡺࡰࡠࡴࡨࡷࡵࡵ࡮ࡴࡧࠪ∀"): {},
                bstack11111_opy_ (u"ࠫࡲ࡫ࡳࡴࡣࡪࡩࠬ∁"): log[bstack11111_opy_ (u"ࠬࡳࡥࡴࡵࡤ࡫ࡪ࠭∂")],
            }
            if bstack11111_opy_ (u"࠭ࡴࡦࡵࡷࡣࡷࡻ࡮ࡠࡷࡸ࡭ࡩ࠭∃") in log:
                bstack1llll11l1ll1_opy_[bstack11111_opy_ (u"ࠧࡵࡧࡶࡸࡤࡸࡵ࡯ࡡࡸࡹ࡮ࡪࠧ∄")] = log[bstack11111_opy_ (u"ࠨࡶࡨࡷࡹࡥࡲࡶࡰࡢࡹࡺ࡯ࡤࠨ∅")]
            elif bstack11111_opy_ (u"ࠩ࡫ࡳࡴࡱ࡟ࡳࡷࡱࡣࡺࡻࡩࡥࠩ∆") in log:
                bstack1llll11l1ll1_opy_[bstack11111_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡠࡴࡸࡲࡤࡻࡵࡪࡦࠪ∇")] = log[bstack11111_opy_ (u"ࠫ࡭ࡵ࡯࡬ࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠫ∈")]
            cls.bstack1l1l1l11_opy_({
                bstack11111_opy_ (u"ࠬ࡫ࡶࡦࡰࡷࡣࡹࡿࡰࡦࠩ∉"): bstack11111_opy_ (u"࠭ࡌࡰࡩࡆࡶࡪࡧࡴࡦࡦࠪ∊"),
                bstack11111_opy_ (u"ࠧ࡭ࡱࡪࡷࠬ∋"): [bstack1llll11l1ll1_opy_]
            })
    @classmethod
    @error_handler(class_method=True)
    def bstack1llll11l1lll_opy_(cls, steps):
        bstack1llll111ll1l_opy_ = []
        for step in steps:
            bstack1llll11lll11_opy_ = {
                bstack11111_opy_ (u"ࠨ࡭࡬ࡲࡩ࠭∌"): bstack11111_opy_ (u"ࠩࡗࡉࡘ࡚࡟ࡔࡖࡈࡔࠬ∍"),
                bstack11111_opy_ (u"ࠪࡰࡪࡼࡥ࡭ࠩ∎"): step[bstack11111_opy_ (u"ࠫࡱ࡫ࡶࡦ࡮ࠪ∏")],
                bstack11111_opy_ (u"ࠬࡺࡩ࡮ࡧࡶࡸࡦࡳࡰࠨ∐"): step[bstack11111_opy_ (u"࠭ࡴࡪ࡯ࡨࡷࡹࡧ࡭ࡱࠩ∑")],
                bstack11111_opy_ (u"ࠧ࡮ࡧࡶࡷࡦ࡭ࡥࠨ−"): step[bstack11111_opy_ (u"ࠨ࡯ࡨࡷࡸࡧࡧࡦࠩ∓")],
                bstack11111_opy_ (u"ࠩࡧࡹࡷࡧࡴࡪࡱࡱࠫ∔"): step[bstack11111_opy_ (u"ࠪࡨࡺࡸࡡࡵ࡫ࡲࡲࠬ∕")]
            }
            if bstack11111_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠫ∖") in step:
                bstack1llll11lll11_opy_[bstack11111_opy_ (u"ࠬࡺࡥࡴࡶࡢࡶࡺࡴ࡟ࡶࡷ࡬ࡨࠬ∗")] = step[bstack11111_opy_ (u"࠭ࡴࡦࡵࡷࡣࡷࡻ࡮ࡠࡷࡸ࡭ࡩ࠭∘")]
            elif bstack11111_opy_ (u"ࠧࡩࡱࡲ࡯ࡤࡸࡵ࡯ࡡࡸࡹ࡮ࡪࠧ∙") in step:
                bstack1llll11lll11_opy_[bstack11111_opy_ (u"ࠨࡪࡲࡳࡰࡥࡲࡶࡰࡢࡹࡺ࡯ࡤࠨ√")] = step[bstack11111_opy_ (u"ࠩ࡫ࡳࡴࡱ࡟ࡳࡷࡱࡣࡺࡻࡩࡥࠩ∛")]
            bstack1llll111ll1l_opy_.append(bstack1llll11lll11_opy_)
        cls.bstack1l1l1l11_opy_({
            bstack11111_opy_ (u"ࠪࡩࡻ࡫࡮ࡵࡡࡷࡽࡵ࡫ࠧ∜"): bstack11111_opy_ (u"ࠫࡑࡵࡧࡄࡴࡨࡥࡹ࡫ࡤࠨ∝"),
            bstack11111_opy_ (u"ࠬࡲ࡯ࡨࡵࠪ∞"): bstack1llll111ll1l_opy_
        })
    @classmethod
    @error_handler(class_method=True)
    @measure(event_name=EVENTS.bstack1111l11ll1_opy_, stage=STAGE.bstack111l1l11l_opy_)
    def bstack1l11l1l1l_opy_(cls, screenshot):
        cls.bstack1l1l1l11_opy_({
            bstack11111_opy_ (u"࠭ࡥࡷࡧࡱࡸࡤࡺࡹࡱࡧࠪ∟"): bstack11111_opy_ (u"ࠧࡍࡱࡪࡇࡷ࡫ࡡࡵࡧࡧࠫ∠"),
            bstack11111_opy_ (u"ࠨ࡮ࡲ࡫ࡸ࠭∡"): [{
                bstack11111_opy_ (u"ࠩ࡮࡭ࡳࡪࠧ∢"): bstack11111_opy_ (u"ࠪࡘࡊ࡙ࡔࡠࡕࡆࡖࡊࡋࡎࡔࡊࡒࡘࠬ∣"),
                bstack11111_opy_ (u"ࠫࡹ࡯࡭ࡦࡵࡷࡥࡲࡶࠧ∤"): datetime.datetime.utcnow().isoformat() + bstack11111_opy_ (u"ࠬࡠࠧ∥"),
                bstack11111_opy_ (u"࠭࡭ࡦࡵࡶࡥ࡬࡫ࠧ∦"): screenshot[bstack11111_opy_ (u"ࠧࡪ࡯ࡤ࡫ࡪ࠭∧")],
                bstack11111_opy_ (u"ࠨࡶࡨࡷࡹࡥࡲࡶࡰࡢࡹࡺ࡯ࡤࠨ∨"): screenshot[bstack11111_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡳࡷࡱࡣࡺࡻࡩࡥࠩ∩")]
            }]
        }, event_url=bstack11111_opy_ (u"ࠪࡥࡵ࡯࠯ࡷ࠳࠲ࡷࡨࡸࡥࡦࡰࡶ࡬ࡴࡺࡳࠨ∪"))
    @classmethod
    @error_handler(class_method=True)
    def bstack111ll1ll11_opy_(cls, driver):
        current_test_uuid = cls.current_test_uuid()
        if not current_test_uuid:
            return
        cls.bstack1l1l1l11_opy_({
            bstack11111_opy_ (u"ࠫࡪࡼࡥ࡯ࡶࡢࡸࡾࡶࡥࠨ∫"): bstack11111_opy_ (u"ࠬࡉࡂࡕࡕࡨࡷࡸ࡯࡯࡯ࡅࡵࡩࡦࡺࡥࡥࠩ∬"),
            bstack11111_opy_ (u"࠭ࡴࡦࡵࡷࡣࡷࡻ࡮ࠨ∭"): {
                bstack11111_opy_ (u"ࠢࡶࡷ࡬ࡨࠧ∮"): cls.current_test_uuid(),
                bstack11111_opy_ (u"ࠣ࡫ࡱࡸࡪ࡭ࡲࡢࡶ࡬ࡳࡳࡹࠢ∯"): cls.bstack1lll1ll1_opy_(driver)
            }
        })
    @classmethod
    def bstack1l1l11ll_opy_(cls, event: str, bstack1l111111_opy_: bstack1llll11l_opy_):
        bstack1l1l1lll_opy_ = {
            bstack11111_opy_ (u"ࠩࡨࡺࡪࡴࡴࡠࡶࡼࡴࡪ࠭∰"): event,
            bstack1l111111_opy_.event_key(): bstack1l111111_opy_.bstack1ll1l1ll_opy_(event)
        }
        cls.bstack1l1l1l11_opy_(bstack1l1l1lll_opy_)
        result = getattr(bstack1l111111_opy_, bstack11111_opy_ (u"ࠪࡶࡪࡹࡵ࡭ࡶࠪ∱"), None)
        if event == bstack11111_opy_ (u"࡙ࠫ࡫ࡳࡵࡔࡸࡲࡘࡺࡡࡳࡶࡨࡨࠬ∲"):
            threading.current_thread().bstackTestMeta = {bstack11111_opy_ (u"ࠬࡹࡴࡢࡶࡸࡷࠬ∳"): bstack11111_opy_ (u"࠭ࡰࡦࡰࡧ࡭ࡳ࡭ࠧ∴")}
        elif event == bstack11111_opy_ (u"ࠧࡕࡧࡶࡸࡗࡻ࡮ࡇ࡫ࡱ࡭ࡸ࡮ࡥࡥࠩ∵"):
            threading.current_thread().bstackTestMeta = {bstack11111_opy_ (u"ࠨࡵࡷࡥࡹࡻࡳࠨ∶"): getattr(result, bstack11111_opy_ (u"ࠩࡵࡩࡸࡻ࡬ࡵࠩ∷"), bstack11111_opy_ (u"ࠪࠫ∸"))}
    @classmethod
    def on(cls):
        if (os.environ.get(bstack11111_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡉࡗࡅࡣࡏ࡝ࡔࠨ∹"), None) is None or os.environ[bstack11111_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡊࡘࡆࡤࡐࡗࡕࠩ∺")] == bstack11111_opy_ (u"ࠨ࡮ࡶ࡮࡯ࠦ∻")) and (os.environ.get(bstack11111_opy_ (u"ࠧࡃࡕࡢࡅ࠶࠷࡙ࡠࡌ࡚ࡘࠬ∼"), None) is None or os.environ[bstack11111_opy_ (u"ࠨࡄࡖࡣࡆ࠷࠱࡚ࡡࡍ࡛࡙࠭∽")] == bstack11111_opy_ (u"ࠤࡱࡹࡱࡲࠢ∾")):
            return False
        return True
    @staticmethod
    def bstack1llll11l11ll_opy_(func):
        def wrap(*args, **kwargs):
            if bstack11lllll1_opy_.on():
                return func(*args, **kwargs)
            return
        return wrap
    @staticmethod
    def default_headers():
        headers = {
            bstack11111_opy_ (u"ࠪࡇࡴࡴࡴࡦࡰࡷ࠱࡙ࡿࡰࡦࠩ∿"): bstack11111_opy_ (u"ࠫࡦࡶࡰ࡭࡫ࡦࡥࡹ࡯࡯࡯࠱࡭ࡷࡴࡴࠧ≀"),
            bstack11111_opy_ (u"ࠬ࡞࠭ࡃࡕࡗࡅࡈࡑ࠭ࡕࡇࡖࡘࡔࡖࡓࠨ≁"): bstack11111_opy_ (u"࠭ࡴࡳࡷࡨࠫ≂")
        }
        if os.environ.get(bstack11111_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡋ࡙ࡗࠫ≃"), None):
            headers[bstack11111_opy_ (u"ࠨࡃࡸࡸ࡭ࡵࡲࡪࡼࡤࡸ࡮ࡵ࡮ࠨ≄")] = bstack11111_opy_ (u"ࠩࡅࡩࡦࡸࡥࡳࠢࡾࢁࠬ≅").format(os.environ[bstack11111_opy_ (u"ࠥࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚ࡈࡖࡄࡢࡎ࡜࡚ࠢ≆")])
        return headers
    @staticmethod
    def request_url(url):
        return bstack11111_opy_ (u"ࠫࢀࢃ࠯ࡼࡿࠪ≇").format(bstack1llll111llll_opy_, url)
    @staticmethod
    def current_test_uuid():
        return getattr(threading.current_thread(), bstack11111_opy_ (u"ࠬࡩࡵࡳࡴࡨࡲࡹࡥࡴࡦࡵࡷࡣࡺࡻࡩࡥࠩ≈"), None)
    @staticmethod
    def bstack1lll1ll1_opy_(driver):
        return {
            bstack111l11llll1_opy_(): bstack1111ll1lll1_opy_(driver)
        }
    @staticmethod
    def bstack1llll11ll1ll_opy_(exception_info, report):
        return [{bstack11111_opy_ (u"࠭ࡢࡢࡥ࡮ࡸࡷࡧࡣࡦࠩ≉"): [exception_info.exconly(), report.longreprtext]}]
    @staticmethod
    def bstack11111111ll_opy_(typename):
        if bstack11111_opy_ (u"ࠢࡂࡵࡶࡩࡷࡺࡩࡰࡰࠥ≊") in typename:
            return bstack11111_opy_ (u"ࠣࡃࡶࡷࡪࡸࡴࡪࡱࡱࡉࡷࡸ࡯ࡳࠤ≋")
        return bstack11111_opy_ (u"ࠤࡘࡲ࡭ࡧ࡮ࡥ࡮ࡨࡨࡊࡸࡲࡰࡴࠥ≌")