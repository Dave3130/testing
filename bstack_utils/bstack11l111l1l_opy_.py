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
import os
import json
import logging
import datetime
import threading
from bstack_utils.helper import bstack1111l11l1ll_opy_, bstack111l1ll11_opy_, get_host_info, bstack1111l1ll11l_opy_, \
 bstack1l1lll1ll_opy_, bstack1lll1lll_opy_, error_handler, bstack1111ll1ll11_opy_, bstack1l1lll11_opy_
import bstack_utils.accessibility as bstack111111l1_opy_
from bstack_utils.bstack1lll1ll11_opy_ import bstack111l11ll_opy_
from bstack_utils.bstack1l1ll111_opy_ import bstack1l11lll1_opy_
from bstack_utils.percy import bstack111ll1lll1_opy_
from bstack_utils.config import Config
bstack111lll11_opy_ = Config.bstack1111llll_opy_()
logger = logging.getLogger(__name__)
percy = bstack111ll1lll1_opy_()
@error_handler(class_method=False)
def bstack1llll11llll1_opy_(bs_config, bstack1ll11llll1_opy_):
  try:
    data = {
        bstack11111_opy_ (u"ࠪࡪࡴࡸ࡭ࡢࡶࠪ≍"): bstack11111_opy_ (u"ࠫ࡯ࡹ࡯࡯ࠩ≎"),
        bstack11111_opy_ (u"ࠬࡶࡲࡰ࡬ࡨࡧࡹࡥ࡮ࡢ࡯ࡨࠫ≏"): bs_config.get(bstack11111_opy_ (u"࠭ࡰࡳࡱ࡭ࡩࡨࡺࡎࡢ࡯ࡨࠫ≐"), bstack11111_opy_ (u"ࠧࠨ≑")),
        bstack11111_opy_ (u"ࠨࡰࡤࡱࡪ࠭≒"): bs_config.get(bstack11111_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡏࡣࡰࡩࠬ≓"), os.path.basename(os.path.abspath(os.getcwd()))),
        bstack11111_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡡ࡬ࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭≔"): bs_config.get(bstack11111_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭≕")),
        bstack11111_opy_ (u"ࠬࡪࡥࡴࡥࡵ࡭ࡵࡺࡩࡰࡰࠪ≖"): bs_config.get(bstack11111_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡉ࡫ࡳࡤࡴ࡬ࡴࡹ࡯࡯࡯ࠩ≗"), bstack11111_opy_ (u"ࠧࠨ≘")),
        bstack11111_opy_ (u"ࠨࡵࡷࡥࡷࡺࡥࡥࡡࡤࡸࠬ≙"): bstack1l1lll11_opy_(),
        bstack11111_opy_ (u"ࠩࡷࡥ࡬ࡹࠧ≚"): bstack1111l1ll11l_opy_(bs_config),
        bstack11111_opy_ (u"ࠪ࡬ࡴࡹࡴࡠ࡫ࡱࡪࡴ࠭≛"): get_host_info(),
        bstack11111_opy_ (u"ࠫࡨ࡯࡟ࡪࡰࡩࡳࠬ≜"): bstack111l1ll11_opy_(),
        bstack11111_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡣࡷࡻ࡮ࡠ࡫ࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬ≝"): os.environ.get(bstack11111_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡈࡕࡊࡎࡇࡣࡗ࡛ࡎࡠࡋࡇࡉࡓ࡚ࡉࡇࡋࡈࡖࠬ≞")),
        bstack11111_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪ࡟ࡵࡧࡶࡸࡸࡥࡲࡦࡴࡸࡲࠬ≟"): os.environ.get(bstack11111_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡓࡇࡕ࡙ࡓ࠭≠"), False),
        bstack11111_opy_ (u"ࠩࡹࡩࡷࡹࡩࡰࡰࡢࡧࡴࡴࡴࡳࡱ࡯ࠫ≡"): bstack1111l11l1ll_opy_(),
        bstack11111_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠪ≢"): bstack1llll1111l11_opy_(bs_config),
        bstack11111_opy_ (u"ࠫ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟ࡥࡧࡷࡥ࡮ࡲࡳࠨ≣"): bstack1llll1111ll1_opy_(bstack1ll11llll1_opy_),
        bstack11111_opy_ (u"ࠬࡶࡲࡰࡦࡸࡧࡹࡥ࡭ࡢࡲࠪ≤"): bstack1llll11111ll_opy_(bs_config, bstack1ll11llll1_opy_.get(bstack11111_opy_ (u"࠭ࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡸࡷࡪࡪࠧ≥"), bstack11111_opy_ (u"ࠧࠨ≦"))),
        bstack11111_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡁࡶࡶࡲࡱࡦࡺࡩࡰࡰࠪ≧"): bstack1l1lll1ll_opy_(bs_config),
        bstack11111_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡰࡴࡦ࡬ࡪࡹࡴࡳࡣࡷ࡭ࡴࡴࠧ≨"): bstack1lll1llll1ll_opy_(bs_config)
    }
    return data
  except Exception as error:
    logger.error(bstack11111_opy_ (u"ࠥࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡷࡩ࡫࡯ࡩࠥࡩࡲࡦࡣࡷ࡭ࡳ࡭ࠠࡱࡣࡼࡰࡴࡧࡤࠡࡨࡲࡶ࡚ࠥࡥࡴࡶࡋࡹࡧࡀࠠࠡࡽࢀࠦ≩").format(str(error)))
    return None
def bstack1llll1111ll1_opy_(framework):
  return {
    bstack11111_opy_ (u"ࠫ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱࡎࡢ࡯ࡨࠫ≪"): framework.get(bstack11111_opy_ (u"ࠬ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡰࡤࡱࡪ࠭≫"), bstack11111_opy_ (u"࠭ࡐࡺࡶࡨࡷࡹ࠭≬")),
    bstack11111_opy_ (u"ࠧࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭࡙ࡩࡷࡹࡩࡰࡰࠪ≭"): framework.get(bstack11111_opy_ (u"ࠨࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠬ≮")),
    bstack11111_opy_ (u"ࠩࡶࡨࡰ࡜ࡥࡳࡵ࡬ࡳࡳ࠭≯"): framework.get(bstack11111_opy_ (u"ࠪࡷࡩࡱ࡟ࡷࡧࡵࡷ࡮ࡵ࡮ࠨ≰")),
    bstack11111_opy_ (u"ࠫࡱࡧ࡮ࡨࡷࡤ࡫ࡪ࠭≱"): bstack11111_opy_ (u"ࠬࡶࡹࡵࡪࡲࡲࠬ≲"),
    bstack11111_opy_ (u"࠭ࡴࡦࡵࡷࡊࡷࡧ࡭ࡦࡹࡲࡶࡰ࠭≳"): framework.get(bstack11111_opy_ (u"ࠧࡵࡧࡶࡸࡋࡸࡡ࡮ࡧࡺࡳࡷࡱࠧ≴"))
  }
def bstack1lll1llll1ll_opy_(bs_config):
  bstack11111_opy_ (u"ࠣࠤࠥࠎࠥࠦࡒࡦࡶࡸࡶࡳࡹࠠࡵࡪࡨࠤࡹ࡫ࡳࡵࠢࡲࡶࡨ࡮ࡥࡴࡶࡵࡥࡹ࡯࡯࡯ࠢࡧࡥࡹࡧࠠࡧࡱࡵࠤࡧࡻࡩ࡭ࡦࠣࡷࡹࡧࡲࡵ࠰ࠍࠤࠥࠨࠢࠣ≵")
  if not bs_config:
    return {}
  bstack111lll11lll_opy_ = bstack111l11ll_opy_(bs_config).bstack111llll1ll1_opy_(bs_config)
  return bstack111lll11lll_opy_
def bstack1l1l11111l_opy_(bs_config, framework):
  bstack1l111llll1_opy_ = False
  bstack11l11ll1ll_opy_ = False
  bstack1llll1111111_opy_ = False
  if bstack11111_opy_ (u"ࠩࡷࡹࡷࡨ࡯ࡔࡥࡤࡰࡪ࠭≶") in bs_config:
    bstack1llll1111111_opy_ = True
  elif bstack11111_opy_ (u"ࠪࡥࡵࡶࠧ≷") in bs_config:
    bstack1l111llll1_opy_ = True
  else:
    bstack11l11ll1ll_opy_ = True
  bstack1l11ll1ll1_opy_ = {
    bstack11111_opy_ (u"ࠫࡴࡨࡳࡦࡴࡹࡥࡧ࡯࡬ࡪࡶࡼࠫ≸"): bstack1l11lll1_opy_.bstack11l111l1lll_opy_(bs_config, framework),
    bstack11111_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠬ≹"): bstack111111l1_opy_.bstack111111l1l1_opy_(bs_config),
    bstack11111_opy_ (u"࠭ࡰࡦࡴࡦࡽࠬ≺"): bs_config.get(bstack11111_opy_ (u"ࠧࡱࡧࡵࡧࡾ࠭≻"), False),
    bstack11111_opy_ (u"ࠨࡣࡸࡸࡴࡳࡡࡵࡧࠪ≼"): bstack11l11ll1ll_opy_,
    bstack11111_opy_ (u"ࠩࡤࡴࡵࡥࡡࡶࡶࡲࡱࡦࡺࡥࠨ≽"): bstack1l111llll1_opy_,
    bstack11111_opy_ (u"ࠪࡸࡺࡸࡢࡰࡵࡦࡥࡱ࡫ࠧ≾"): bstack1llll1111111_opy_
  }
  return bstack1l11ll1ll1_opy_
@error_handler(class_method=False)
def bstack1llll1111l11_opy_(bs_config):
  try:
    bstack1llll111111l_opy_ = json.loads(os.getenv(bstack11111_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡠࡃࡆࡇࡊ࡙ࡓࡊࡄࡌࡐࡎ࡚࡙ࡠࡅࡒࡒࡋࡏࡇࡖࡔࡄࡘࡎࡕࡎࡠ࡛ࡐࡐࠬ≿"), bstack11111_opy_ (u"ࠬࢁࡽࠨ⊀")))
    bstack1llll111111l_opy_ = bstack1lll1lllll11_opy_(bs_config, bstack1llll111111l_opy_)
    return {
        bstack11111_opy_ (u"࠭ࡳࡦࡶࡷ࡭ࡳ࡭ࡳࠨ⊁"): bstack1llll111111l_opy_
    }
  except Exception as error:
    logger.error(bstack11111_opy_ (u"ࠢࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣࡻ࡭࡯࡬ࡦࠢࡦࡶࡪࡧࡴࡪࡰࡪࠤ࡬࡫ࡴࡠࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࡠࡵࡨࡸࡹ࡯࡮ࡨࡵࠣࡪࡴࡸࠠࡕࡧࡶࡸࡍࡻࡢ࠻ࠢࠣࡿࢂࠨ⊂").format(str(error)))
    return {}
def bstack1lll1lllll11_opy_(bs_config, bstack1llll111111l_opy_):
  if ((bstack11111_opy_ (u"ࠨࡶࡸࡶࡧࡵࡓࡤࡣ࡯ࡩࠬ⊃") in bs_config or not bstack1l1lll1ll_opy_(bs_config)) and bstack111111l1_opy_.bstack111111l1l1_opy_(bs_config)):
    bstack1llll111111l_opy_[bstack11111_opy_ (u"ࠤ࡬ࡲࡨࡲࡵࡥࡧࡈࡲࡨࡵࡤࡦࡦࡈࡼࡹ࡫࡮ࡴ࡫ࡲࡲࠧ⊄")] = True
  return bstack1llll111111l_opy_
def bstack1llll11l1l1l_opy_(array, bstack1lll1lllllll_opy_, bstack1llll11111l1_opy_):
  result = {}
  for o in array:
    key = o[bstack1lll1lllllll_opy_]
    result[key] = o[bstack1llll11111l1_opy_]
  return result
def bstack1llll11l1l11_opy_(bstack1l11111l1l_opy_=bstack11111_opy_ (u"ࠪࠫ⊅")):
  bstack1lll1llllll1_opy_ = bstack111111l1_opy_.on()
  bstack1llll1111l1l_opy_ = bstack1l11lll1_opy_.on()
  bstack1lll1llll1l1_opy_ = percy.bstack11l1l1l1l1_opy_()
  if bstack1lll1llll1l1_opy_ and not bstack1llll1111l1l_opy_ and not bstack1lll1llllll1_opy_:
    return bstack1l11111l1l_opy_ not in [bstack11111_opy_ (u"ࠫࡈࡈࡔࡔࡧࡶࡷ࡮ࡵ࡮ࡄࡴࡨࡥࡹ࡫ࡤࠨ⊆"), bstack11111_opy_ (u"ࠬࡒ࡯ࡨࡅࡵࡩࡦࡺࡥࡥࠩ⊇")]
  elif bstack1lll1llllll1_opy_ and not bstack1llll1111l1l_opy_:
    return bstack1l11111l1l_opy_ not in [bstack11111_opy_ (u"࠭ࡈࡰࡱ࡮ࡖࡺࡴࡓࡵࡣࡵࡸࡪࡪࠧ⊈"), bstack11111_opy_ (u"ࠧࡉࡱࡲ࡯ࡗࡻ࡮ࡇ࡫ࡱ࡭ࡸ࡮ࡥࡥࠩ⊉"), bstack11111_opy_ (u"ࠨࡎࡲ࡫ࡈࡸࡥࡢࡶࡨࡨࠬ⊊")]
  return bstack1lll1llllll1_opy_ or bstack1llll1111l1l_opy_ or bstack1lll1llll1l1_opy_
@error_handler(class_method=False)
def bstack1llll111ll11_opy_(bstack1l11111l1l_opy_, test=None):
  bstack1lll1lllll1l_opy_ = bstack111111l1_opy_.on()
  if not bstack1lll1lllll1l_opy_ or bstack1l11111l1l_opy_ not in [bstack11111_opy_ (u"ࠩࡗࡩࡸࡺࡒࡶࡰࡉ࡭ࡳ࡯ࡳࡩࡧࡧࠫ⊋")] or test == None:
    return None
  return {
    bstack11111_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠪ⊌"): bstack1lll1lllll1l_opy_ and bstack1lll1lll_opy_(threading.current_thread(), bstack11111_opy_ (u"ࠫࡦ࠷࠱ࡺࡒ࡯ࡥࡹ࡬࡯ࡳ࡯ࠪ⊍"), None) == True and bstack111111l1_opy_.bstack1llll1ll11_opy_(test[bstack11111_opy_ (u"ࠬࡺࡡࡨࡵࠪ⊎")])
  }
def bstack1llll11111ll_opy_(bs_config, framework):
  bstack1l111llll1_opy_ = False
  bstack11l11ll1ll_opy_ = False
  bstack1llll1111111_opy_ = False
  if bstack11111_opy_ (u"࠭ࡴࡶࡴࡥࡳࡘࡩࡡ࡭ࡧࠪ⊏") in bs_config:
    bstack1llll1111111_opy_ = True
  elif bstack11111_opy_ (u"ࠧࡢࡲࡳࠫ⊐") in bs_config:
    bstack1l111llll1_opy_ = True
  else:
    bstack11l11ll1ll_opy_ = True
  bstack1l11ll1ll1_opy_ = {
    bstack11111_opy_ (u"ࠨࡱࡥࡷࡪࡸࡶࡢࡤ࡬ࡰ࡮ࡺࡹࠨ⊑"): bstack1l11lll1_opy_.bstack11l111l1lll_opy_(bs_config, framework),
    bstack11111_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠩ⊒"): bstack111111l1_opy_.bstack11l1l11ll1_opy_(bs_config),
    bstack11111_opy_ (u"ࠪࡴࡪࡸࡣࡺࠩ⊓"): bs_config.get(bstack11111_opy_ (u"ࠫࡵ࡫ࡲࡤࡻࠪ⊔"), False),
    bstack11111_opy_ (u"ࠬࡧࡵࡵࡱࡰࡥࡹ࡫ࠧ⊕"): bstack11l11ll1ll_opy_,
    bstack11111_opy_ (u"࠭ࡡࡱࡲࡢࡥࡺࡺ࡯࡮ࡣࡷࡩࠬ⊖"): bstack1l111llll1_opy_,
    bstack11111_opy_ (u"ࠧࡵࡷࡵࡦࡴࡹࡣࡢ࡮ࡨࠫ⊗"): bstack1llll1111111_opy_
  }
  return bstack1l11ll1ll1_opy_