# coding: UTF-8
import sys
bstack1l1lll_opy_ = sys.version_info [0] == 2
bstack1l1l1ll_opy_ = 2048
bstack1lllllll_opy_ = 7
def bstack1ll1l_opy_ (bstack1ll1l1l_opy_):
    global bstack11ll1l_opy_
    bstack111l111_opy_ = ord (bstack1ll1l1l_opy_ [-1])
    bstack1l111ll_opy_ = bstack1ll1l1l_opy_ [:-1]
    bstack1ll_opy_ = bstack111l111_opy_ % len (bstack1l111ll_opy_)
    bstack111l_opy_ = bstack1l111ll_opy_ [:bstack1ll_opy_] + bstack1l111ll_opy_ [bstack1ll_opy_:]
    if bstack1l1lll_opy_:
        bstack1lll1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack1l1l1ll_opy_ - (bstack1111lll_opy_ + bstack111l111_opy_) % bstack1lllllll_opy_) for bstack1111lll_opy_, char in enumerate (bstack111l_opy_)])
    else:
        bstack1lll1ll_opy_ = str () .join ([chr (ord (char) - bstack1l1l1ll_opy_ - (bstack1111lll_opy_ + bstack111l111_opy_) % bstack1lllllll_opy_) for bstack1111lll_opy_, char in enumerate (bstack111l_opy_)])
    return eval (bstack1lll1ll_opy_)
import os
import json
import logging
import datetime
import threading
from bstack_utils.helper import bstack1111l1ll1ll_opy_, bstack1ll1l11l1_opy_, get_host_info, bstack1111l1lll1l_opy_, \
 bstack11l11ll11_opy_, bstack1l1l1l1l_opy_, error_handler, bstack1111ll1l1l1_opy_, bstack1l1l1lll_opy_
import bstack_utils.accessibility as bstack1lllllll1_opy_
from bstack_utils.bstack1111llll_opy_ import bstack11111l1l_opy_
from bstack_utils.bstack11llll1l_opy_ import bstack1l11llll_opy_
from bstack_utils.percy import bstack1ll1llll1_opy_
from bstack_utils.config import Config
bstack111111ll_opy_ = Config.bstack111l1ll1_opy_()
logger = logging.getLogger(__name__)
percy = bstack1ll1llll1_opy_()
@error_handler(class_method=False)
def bstack1llll1l1111l_opy_(bs_config, bstack1lll11ll1l_opy_):
  try:
    data = {
        bstack1ll1l_opy_ (u"ࠬ࡬࡯ࡳ࡯ࡤࡸࠬ⇴"): bstack1ll1l_opy_ (u"࠭ࡪࡴࡱࡱࠫ⇵"),
        bstack1ll1l_opy_ (u"ࠧࡱࡴࡲ࡮ࡪࡩࡴࡠࡰࡤࡱࡪ࠭⇶"): bs_config.get(bstack1ll1l_opy_ (u"ࠨࡲࡵࡳ࡯࡫ࡣࡵࡐࡤࡱࡪ࠭⇷"), bstack1ll1l_opy_ (u"ࠩࠪ⇸")),
        bstack1ll1l_opy_ (u"ࠪࡲࡦࡳࡥࠨ⇹"): bs_config.get(bstack1ll1l_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡑࡥࡲ࡫ࠧ⇺"), os.path.basename(os.path.abspath(os.getcwd()))),
        bstack1ll1l_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡣ࡮ࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨ⇻"): bs_config.get(bstack1ll1l_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨ⇼")),
        bstack1ll1l_opy_ (u"ࠧࡥࡧࡶࡧࡷ࡯ࡰࡵ࡫ࡲࡲࠬ⇽"): bs_config.get(bstack1ll1l_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡄࡦࡵࡦࡶ࡮ࡶࡴࡪࡱࡱࠫ⇾"), bstack1ll1l_opy_ (u"ࠩࠪ⇿")),
        bstack1ll1l_opy_ (u"ࠪࡷࡹࡧࡲࡵࡧࡧࡣࡦࡺࠧ∀"): bstack1l1l1lll_opy_(),
        bstack1ll1l_opy_ (u"ࠫࡹࡧࡧࡴࠩ∁"): bstack1111l1lll1l_opy_(bs_config),
        bstack1ll1l_opy_ (u"ࠬ࡮࡯ࡴࡶࡢ࡭ࡳ࡬࡯ࠨ∂"): get_host_info(),
        bstack1ll1l_opy_ (u"࠭ࡣࡪࡡ࡬ࡲ࡫ࡵࠧ∃"): bstack1ll1l11l1_opy_(),
        bstack1ll1l_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡥࡲࡶࡰࡢ࡭ࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧ∄"): os.environ.get(bstack1ll1l_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡃࡗࡌࡐࡉࡥࡒࡖࡐࡢࡍࡉࡋࡎࡕࡋࡉࡍࡊࡘࠧ∅")),
        bstack1ll1l_opy_ (u"ࠩࡩࡥ࡮ࡲࡥࡥࡡࡷࡩࡸࡺࡳࡠࡴࡨࡶࡺࡴࠧ∆"): os.environ.get(bstack1ll1l_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡕࡉࡗ࡛ࡎࠨ∇"), False),
        bstack1ll1l_opy_ (u"ࠫࡻ࡫ࡲࡴ࡫ࡲࡲࡤࡩ࡯࡯ࡶࡵࡳࡱ࠭∈"): bstack1111l1ll1ll_opy_(),
        bstack1ll1l_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠬ∉"): bstack1llll11ll11l_opy_(bs_config),
        bstack1ll1l_opy_ (u"࠭ࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡧࡩࡹࡧࡩ࡭ࡵࠪ∊"): bstack1llll111llll_opy_(bstack1lll11ll1l_opy_),
        bstack1ll1l_opy_ (u"ࠧࡱࡴࡲࡨࡺࡩࡴࡠ࡯ࡤࡴࠬ∋"): bstack1llll11l1l11_opy_(bs_config, bstack1lll11ll1l_opy_.get(bstack1ll1l_opy_ (u"ࠨࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡺࡹࡥࡥࠩ∌"), bstack1ll1l_opy_ (u"ࠩࠪ∍"))),
        bstack1ll1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡃࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࠬ∎"): bstack11l11ll11_opy_(bs_config),
        bstack1ll1l_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡲࡶࡨ࡮ࡥࡴࡶࡵࡥࡹ࡯࡯࡯ࠩ∏"): bstack1llll11l11ll_opy_(bs_config)
    }
    return data
  except Exception as error:
    logger.error(bstack1ll1l_opy_ (u"ࠧࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡࡹ࡫࡭ࡱ࡫ࠠࡤࡴࡨࡥࡹ࡯࡮ࡨࠢࡳࡥࡾࡲ࡯ࡢࡦࠣࡪࡴࡸࠠࡕࡧࡶࡸࡍࡻࡢ࠻ࠢࠣࡿࢂࠨ∐").format(str(error)))
    return None
def bstack1llll111llll_opy_(framework):
  return {
    bstack1ll1l_opy_ (u"࠭ࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡐࡤࡱࡪ࠭∑"): framework.get(bstack1ll1l_opy_ (u"ࠧࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡲࡦࡳࡥࠨ−"), bstack1ll1l_opy_ (u"ࠨࡒࡼࡸࡪࡹࡴࠨ∓")),
    bstack1ll1l_opy_ (u"ࠩࡩࡶࡦࡳࡥࡸࡱࡵ࡯࡛࡫ࡲࡴ࡫ࡲࡲࠬ∔"): framework.get(bstack1ll1l_opy_ (u"ࠪࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡥࡶࡦࡴࡶ࡭ࡴࡴࠧ∕")),
    bstack1ll1l_opy_ (u"ࠫࡸࡪ࡫ࡗࡧࡵࡷ࡮ࡵ࡮ࠨ∖"): framework.get(bstack1ll1l_opy_ (u"ࠬࡹࡤ࡬ࡡࡹࡩࡷࡹࡩࡰࡰࠪ∗")),
    bstack1ll1l_opy_ (u"࠭࡬ࡢࡰࡪࡹࡦ࡭ࡥࠨ∘"): bstack1ll1l_opy_ (u"ࠧࡱࡻࡷ࡬ࡴࡴࠧ∙"),
    bstack1ll1l_opy_ (u"ࠨࡶࡨࡷࡹࡌࡲࡢ࡯ࡨࡻࡴࡸ࡫ࠨ√"): framework.get(bstack1ll1l_opy_ (u"ࠩࡷࡩࡸࡺࡆࡳࡣࡰࡩࡼࡵࡲ࡬ࠩ∛"))
  }
def bstack1llll11l11ll_opy_(bs_config):
  bstack1ll1l_opy_ (u"ࠥࠦࠧࠐࠠࠡࡔࡨࡸࡺࡸ࡮ࡴࠢࡷ࡬ࡪࠦࡴࡦࡵࡷࠤࡴࡸࡣࡩࡧࡶࡸࡷࡧࡴࡪࡱࡱࠤࡩࡧࡴࡢࠢࡩࡳࡷࠦࡢࡶ࡫࡯ࡨࠥࡹࡴࡢࡴࡷ࠲ࠏࠦࠠࠣࠤࠥ∜")
  if not bs_config:
    return {}
  bstack11l11111lll_opy_ = bstack11111l1l_opy_(bs_config).bstack111lllll1ll_opy_(bs_config)
  return bstack11l11111lll_opy_
def bstack111l111ll_opy_(bs_config, framework):
  bstack1l111ll1l1_opy_ = False
  bstack1l1ll1l1l_opy_ = False
  bstack1llll11l1ll1_opy_ = False
  if bstack1ll1l_opy_ (u"ࠫࡹࡻࡲࡣࡱࡖࡧࡦࡲࡥࠨ∝") in bs_config:
    bstack1llll11l1ll1_opy_ = True
  elif bstack1ll1l_opy_ (u"ࠬࡧࡰࡱࠩ∞") in bs_config:
    bstack1l111ll1l1_opy_ = True
  else:
    bstack1l1ll1l1l_opy_ = True
  bstack11ll1ll11l_opy_ = {
    bstack1ll1l_opy_ (u"࠭࡯ࡣࡵࡨࡶࡻࡧࡢࡪ࡮࡬ࡸࡾ࠭∟"): bstack1l11llll_opy_.bstack11l11l1ll1l_opy_(bs_config, framework),
    bstack1ll1l_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠧ∠"): bstack1lllllll1_opy_.bstack111ll11ll1_opy_(bs_config),
    bstack1ll1l_opy_ (u"ࠨࡲࡨࡶࡨࡿࠧ∡"): bs_config.get(bstack1ll1l_opy_ (u"ࠩࡳࡩࡷࡩࡹࠨ∢"), False),
    bstack1ll1l_opy_ (u"ࠪࡥࡺࡺ࡯࡮ࡣࡷࡩࠬ∣"): bstack1l1ll1l1l_opy_,
    bstack1ll1l_opy_ (u"ࠫࡦࡶࡰࡠࡣࡸࡸࡴࡳࡡࡵࡧࠪ∤"): bstack1l111ll1l1_opy_,
    bstack1ll1l_opy_ (u"ࠬࡺࡵࡳࡤࡲࡷࡨࡧ࡬ࡦࠩ∥"): bstack1llll11l1ll1_opy_
  }
  return bstack11ll1ll11l_opy_
@error_handler(class_method=False)
def bstack1llll11ll11l_opy_(bs_config):
  try:
    bstack1llll111ll1l_opy_ = json.loads(os.getenv(bstack1ll1l_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡢࡅࡈࡉࡅࡔࡕࡌࡆࡎࡒࡉࡕ࡛ࡢࡇࡔࡔࡆࡊࡉࡘࡖࡆ࡚ࡉࡐࡐࡢ࡝ࡒࡒࠧ∦"), bstack1ll1l_opy_ (u"ࠧࡼࡿࠪ∧")))
    bstack1llll111ll1l_opy_ = bstack1llll11l1lll_opy_(bs_config, bstack1llll111ll1l_opy_)
    return {
        bstack1ll1l_opy_ (u"ࠨࡵࡨࡸࡹ࡯࡮ࡨࡵࠪ∨"): bstack1llll111ll1l_opy_
    }
  except Exception as error:
    logger.error(bstack1ll1l_opy_ (u"ࠤࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥࡽࡨࡪ࡮ࡨࠤࡨࡸࡥࡢࡶ࡬ࡲ࡬ࠦࡧࡦࡶࡢࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࡢࡷࡪࡺࡴࡪࡰࡪࡷࠥ࡬࡯ࡳࠢࡗࡩࡸࡺࡈࡶࡤ࠽ࠤࠥࢁࡽࠣ∩").format(str(error)))
    return {}
def bstack1llll11l1lll_opy_(bs_config, bstack1llll111ll1l_opy_):
  if ((bstack1ll1l_opy_ (u"ࠪࡸࡺࡸࡢࡰࡕࡦࡥࡱ࡫ࠧ∪") in bs_config or not bstack11l11ll11_opy_(bs_config)) and bstack1lllllll1_opy_.bstack111ll11ll1_opy_(bs_config)):
    bstack1llll111ll1l_opy_[bstack1ll1l_opy_ (u"ࠦ࡮ࡴࡣ࡭ࡷࡧࡩࡊࡴࡣࡰࡦࡨࡨࡊࡾࡴࡦࡰࡶ࡭ࡴࡴࠢ∫")] = True
  return bstack1llll111ll1l_opy_
def bstack1llll1l11lll_opy_(array, bstack1llll11l111l_opy_, bstack1llll11l1l1l_opy_):
  result = {}
  for o in array:
    key = o[bstack1llll11l111l_opy_]
    result[key] = o[bstack1llll11l1l1l_opy_]
  return result
def bstack1llll1l111ll_opy_(bstack11llll1ll1_opy_=bstack1ll1l_opy_ (u"ࠬ࠭∬")):
  bstack1llll11l11l1_opy_ = bstack1lllllll1_opy_.on()
  bstack1llll111lll1_opy_ = bstack1l11llll_opy_.on()
  bstack1llll11ll111_opy_ = percy.bstack11llll11l_opy_()
  if bstack1llll11ll111_opy_ and not bstack1llll111lll1_opy_ and not bstack1llll11l11l1_opy_:
    return bstack11llll1ll1_opy_ not in [bstack1ll1l_opy_ (u"࠭ࡃࡃࡖࡖࡩࡸࡹࡩࡰࡰࡆࡶࡪࡧࡴࡦࡦࠪ∭"), bstack1ll1l_opy_ (u"ࠧࡍࡱࡪࡇࡷ࡫ࡡࡵࡧࡧࠫ∮")]
  elif bstack1llll11l11l1_opy_ and not bstack1llll111lll1_opy_:
    return bstack11llll1ll1_opy_ not in [bstack1ll1l_opy_ (u"ࠨࡊࡲࡳࡰࡘࡵ࡯ࡕࡷࡥࡷࡺࡥࡥࠩ∯"), bstack1ll1l_opy_ (u"ࠩࡋࡳࡴࡱࡒࡶࡰࡉ࡭ࡳ࡯ࡳࡩࡧࡧࠫ∰"), bstack1ll1l_opy_ (u"ࠪࡐࡴ࡭ࡃࡳࡧࡤࡸࡪࡪࠧ∱")]
  return bstack1llll11l11l1_opy_ or bstack1llll111lll1_opy_ or bstack1llll11ll111_opy_
@error_handler(class_method=False)
def bstack1llll11ll1l1_opy_(bstack11llll1ll1_opy_, test=None):
  bstack1llll11l1111_opy_ = bstack1lllllll1_opy_.on()
  if not bstack1llll11l1111_opy_ or bstack11llll1ll1_opy_ not in [bstack1ll1l_opy_ (u"࡙ࠫ࡫ࡳࡵࡔࡸࡲࡋ࡯࡮ࡪࡵ࡫ࡩࡩ࠭∲")] or test == None:
    return None
  return {
    bstack1ll1l_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠬ∳"): bstack1llll11l1111_opy_ and bstack1l1l1l1l_opy_(threading.current_thread(), bstack1ll1l_opy_ (u"࠭ࡡ࠲࠳ࡼࡔࡱࡧࡴࡧࡱࡵࡱࠬ∴"), None) == True and bstack1lllllll1_opy_.bstack1l11l1llll_opy_(test[bstack1ll1l_opy_ (u"ࠧࡵࡣࡪࡷࠬ∵")])
  }
def bstack1llll11l1l11_opy_(bs_config, framework):
  bstack1l111ll1l1_opy_ = False
  bstack1l1ll1l1l_opy_ = False
  bstack1llll11l1ll1_opy_ = False
  if bstack1ll1l_opy_ (u"ࠨࡶࡸࡶࡧࡵࡓࡤࡣ࡯ࡩࠬ∶") in bs_config:
    bstack1llll11l1ll1_opy_ = True
  elif bstack1ll1l_opy_ (u"ࠩࡤࡴࡵ࠭∷") in bs_config:
    bstack1l111ll1l1_opy_ = True
  else:
    bstack1l1ll1l1l_opy_ = True
  bstack11ll1ll11l_opy_ = {
    bstack1ll1l_opy_ (u"ࠪࡳࡧࡹࡥࡳࡸࡤࡦ࡮ࡲࡩࡵࡻࠪ∸"): bstack1l11llll_opy_.bstack11l11l1ll1l_opy_(bs_config, framework),
    bstack1ll1l_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠫ∹"): bstack1lllllll1_opy_.bstack11l11lll1_opy_(bs_config),
    bstack1ll1l_opy_ (u"ࠬࡶࡥࡳࡥࡼࠫ∺"): bs_config.get(bstack1ll1l_opy_ (u"࠭ࡰࡦࡴࡦࡽࠬ∻"), False),
    bstack1ll1l_opy_ (u"ࠧࡢࡷࡷࡳࡲࡧࡴࡦࠩ∼"): bstack1l1ll1l1l_opy_,
    bstack1ll1l_opy_ (u"ࠨࡣࡳࡴࡤࡧࡵࡵࡱࡰࡥࡹ࡫ࠧ∽"): bstack1l111ll1l1_opy_,
    bstack1ll1l_opy_ (u"ࠩࡷࡹࡷࡨ࡯ࡴࡥࡤࡰࡪ࠭∾"): bstack1llll11l1ll1_opy_
  }
  return bstack11ll1ll11l_opy_