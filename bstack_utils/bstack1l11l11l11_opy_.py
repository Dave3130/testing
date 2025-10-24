# coding: UTF-8
import sys
bstack1lllll1_opy_ = sys.version_info [0] == 2
bstack11lll1l_opy_ = 2048
bstack1lll1l_opy_ = 7
def bstack11l11l1_opy_ (bstack111l1ll_opy_):
    global bstack1ll1l_opy_
    bstack1l1l1ll_opy_ = ord (bstack111l1ll_opy_ [-1])
    bstack1l11l_opy_ = bstack111l1ll_opy_ [:-1]
    bstack1lllll1l_opy_ = bstack1l1l1ll_opy_ % len (bstack1l11l_opy_)
    bstack11ll1l1_opy_ = bstack1l11l_opy_ [:bstack1lllll1l_opy_] + bstack1l11l_opy_ [bstack1lllll1l_opy_:]
    if bstack1lllll1_opy_:
        bstack1lll_opy_ = unicode () .join ([unichr (ord (char) - bstack11lll1l_opy_ - (bstack1l1ll11_opy_ + bstack1l1l1ll_opy_) % bstack1lll1l_opy_) for bstack1l1ll11_opy_, char in enumerate (bstack11ll1l1_opy_)])
    else:
        bstack1lll_opy_ = str () .join ([chr (ord (char) - bstack11lll1l_opy_ - (bstack1l1ll11_opy_ + bstack1l1l1ll_opy_) % bstack1lll1l_opy_) for bstack1l1ll11_opy_, char in enumerate (bstack11ll1l1_opy_)])
    return eval (bstack1lll_opy_)
import os
import json
import logging
import datetime
import threading
from bstack_utils.helper import bstack1111l11ll11_opy_, bstack11lll11l1_opy_, get_host_info, bstack1111lll11l1_opy_, \
 bstack1ll11lll11_opy_, bstack1ll11l1l_opy_, error_handler, bstack1111llll11l_opy_, bstack1l11ll1l_opy_
import bstack_utils.accessibility as bstack111llll1_opy_
from bstack_utils.bstack111lll1l_opy_ import bstack1lll11ll1_opy_
from bstack_utils.bstack1ll1ll1l_opy_ import bstack1ll1l1l1_opy_
from bstack_utils.percy import bstack1ll1l11l1_opy_
from bstack_utils.config import Config
bstack11111111_opy_ = Config.bstack1llll1ll1_opy_()
logger = logging.getLogger(__name__)
percy = bstack1ll1l11l1_opy_()
@error_handler(class_method=False)
def bstack1llll11llll1_opy_(bs_config, bstack111llllll1_opy_):
  try:
    data = {
        bstack11l11l1_opy_ (u"ࠬ࡬࡯ࡳ࡯ࡤࡸࠬ∐"): bstack11l11l1_opy_ (u"࠭ࡪࡴࡱࡱࠫ∑"),
        bstack11l11l1_opy_ (u"ࠧࡱࡴࡲ࡮ࡪࡩࡴࡠࡰࡤࡱࡪ࠭−"): bs_config.get(bstack11l11l1_opy_ (u"ࠨࡲࡵࡳ࡯࡫ࡣࡵࡐࡤࡱࡪ࠭∓"), bstack11l11l1_opy_ (u"ࠩࠪ∔")),
        bstack11l11l1_opy_ (u"ࠪࡲࡦࡳࡥࠨ∕"): bs_config.get(bstack11l11l1_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡑࡥࡲ࡫ࠧ∖"), os.path.basename(os.path.abspath(os.getcwd()))),
        bstack11l11l1_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡣ࡮ࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨ∗"): bs_config.get(bstack11l11l1_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨ∘")),
        bstack11l11l1_opy_ (u"ࠧࡥࡧࡶࡧࡷ࡯ࡰࡵ࡫ࡲࡲࠬ∙"): bs_config.get(bstack11l11l1_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡄࡦࡵࡦࡶ࡮ࡶࡴࡪࡱࡱࠫ√"), bstack11l11l1_opy_ (u"ࠩࠪ∛")),
        bstack11l11l1_opy_ (u"ࠪࡷࡹࡧࡲࡵࡧࡧࡣࡦࡺࠧ∜"): bstack1l11ll1l_opy_(),
        bstack11l11l1_opy_ (u"ࠫࡹࡧࡧࡴࠩ∝"): bstack1111lll11l1_opy_(bs_config),
        bstack11l11l1_opy_ (u"ࠬ࡮࡯ࡴࡶࡢ࡭ࡳ࡬࡯ࠨ∞"): get_host_info(),
        bstack11l11l1_opy_ (u"࠭ࡣࡪࡡ࡬ࡲ࡫ࡵࠧ∟"): bstack11lll11l1_opy_(),
        bstack11l11l1_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡥࡲࡶࡰࡢ࡭ࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧ∠"): os.environ.get(bstack11l11l1_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡃࡗࡌࡐࡉࡥࡒࡖࡐࡢࡍࡉࡋࡎࡕࡋࡉࡍࡊࡘࠧ∡")),
        bstack11l11l1_opy_ (u"ࠩࡩࡥ࡮ࡲࡥࡥࡡࡷࡩࡸࡺࡳࡠࡴࡨࡶࡺࡴࠧ∢"): os.environ.get(bstack11l11l1_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡕࡉࡗ࡛ࡎࠨ∣"), False),
        bstack11l11l1_opy_ (u"ࠫࡻ࡫ࡲࡴ࡫ࡲࡲࡤࡩ࡯࡯ࡶࡵࡳࡱ࠭∤"): bstack1111l11ll11_opy_(),
        bstack11l11l1_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠬ∥"): bstack1llll111llll_opy_(bs_config),
        bstack11l11l1_opy_ (u"࠭ࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡧࡩࡹࡧࡩ࡭ࡵࠪ∦"): bstack1llll111ll11_opy_(bstack111llllll1_opy_),
        bstack11l11l1_opy_ (u"ࠧࡱࡴࡲࡨࡺࡩࡴࡠ࡯ࡤࡴࠬ∧"): bstack1llll111l1ll_opy_(bs_config, bstack111llllll1_opy_.get(bstack11l11l1_opy_ (u"ࠨࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡺࡹࡥࡥࠩ∨"), bstack11l11l1_opy_ (u"ࠩࠪ∩"))),
        bstack11l11l1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡃࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࠬ∪"): bstack1ll11lll11_opy_(bs_config),
        bstack11l11l1_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡲࡶࡨ࡮ࡥࡴࡶࡵࡥࡹ࡯࡯࡯ࠩ∫"): bstack1llll1111lll_opy_(bs_config)
    }
    return data
  except Exception as error:
    logger.error(bstack11l11l1_opy_ (u"ࠧࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡࡹ࡫࡭ࡱ࡫ࠠࡤࡴࡨࡥࡹ࡯࡮ࡨࠢࡳࡥࡾࡲ࡯ࡢࡦࠣࡪࡴࡸࠠࡕࡧࡶࡸࡍࡻࡢ࠻ࠢࠣࡿࢂࠨ∬").format(str(error)))
    return None
def bstack1llll111ll11_opy_(framework):
  return {
    bstack11l11l1_opy_ (u"࠭ࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡐࡤࡱࡪ࠭∭"): framework.get(bstack11l11l1_opy_ (u"ࠧࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡲࡦࡳࡥࠨ∮"), bstack11l11l1_opy_ (u"ࠨࡒࡼࡸࡪࡹࡴࠨ∯")),
    bstack11l11l1_opy_ (u"ࠩࡩࡶࡦࡳࡥࡸࡱࡵ࡯࡛࡫ࡲࡴ࡫ࡲࡲࠬ∰"): framework.get(bstack11l11l1_opy_ (u"ࠪࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡥࡶࡦࡴࡶ࡭ࡴࡴࠧ∱")),
    bstack11l11l1_opy_ (u"ࠫࡸࡪ࡫ࡗࡧࡵࡷ࡮ࡵ࡮ࠨ∲"): framework.get(bstack11l11l1_opy_ (u"ࠬࡹࡤ࡬ࡡࡹࡩࡷࡹࡩࡰࡰࠪ∳")),
    bstack11l11l1_opy_ (u"࠭࡬ࡢࡰࡪࡹࡦ࡭ࡥࠨ∴"): bstack11l11l1_opy_ (u"ࠧࡱࡻࡷ࡬ࡴࡴࠧ∵"),
    bstack11l11l1_opy_ (u"ࠨࡶࡨࡷࡹࡌࡲࡢ࡯ࡨࡻࡴࡸ࡫ࠨ∶"): framework.get(bstack11l11l1_opy_ (u"ࠩࡷࡩࡸࡺࡆࡳࡣࡰࡩࡼࡵࡲ࡬ࠩ∷"))
  }
def bstack1llll1111lll_opy_(bs_config):
  bstack11l11l1_opy_ (u"ࠥࠦࠧࠐࠠࠡࡔࡨࡸࡺࡸ࡮ࡴࠢࡷ࡬ࡪࠦࡴࡦࡵࡷࠤࡴࡸࡣࡩࡧࡶࡸࡷࡧࡴࡪࡱࡱࠤࡩࡧࡴࡢࠢࡩࡳࡷࠦࡢࡶ࡫࡯ࡨࠥࡹࡴࡢࡴࡷ࠲ࠏࠦࠠࠣࠤࠥ∸")
  if not bs_config:
    return {}
  bstack111lll11l11_opy_ = bstack1lll11ll1_opy_(bs_config).bstack111lll11ll1_opy_(bs_config)
  return bstack111lll11l11_opy_
def bstack1111l1ll1l_opy_(bs_config, framework):
  bstack111l1l111l_opy_ = False
  bstack1ll1l111l_opy_ = False
  bstack1llll1111ll1_opy_ = False
  if bstack11l11l1_opy_ (u"ࠫࡹࡻࡲࡣࡱࡖࡧࡦࡲࡥࠨ∹") in bs_config:
    bstack1llll1111ll1_opy_ = True
  elif bstack11l11l1_opy_ (u"ࠬࡧࡰࡱࠩ∺") in bs_config:
    bstack111l1l111l_opy_ = True
  else:
    bstack1ll1l111l_opy_ = True
  bstack111ll11ll1_opy_ = {
    bstack11l11l1_opy_ (u"࠭࡯ࡣࡵࡨࡶࡻࡧࡢࡪ࡮࡬ࡸࡾ࠭∻"): bstack1ll1l1l1_opy_.bstack11l11l11ll1_opy_(bs_config, framework),
    bstack11l11l1_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠧ∼"): bstack111llll1_opy_.bstack111l1ll11l_opy_(bs_config),
    bstack11l11l1_opy_ (u"ࠨࡲࡨࡶࡨࡿࠧ∽"): bs_config.get(bstack11l11l1_opy_ (u"ࠩࡳࡩࡷࡩࡹࠨ∾"), False),
    bstack11l11l1_opy_ (u"ࠪࡥࡺࡺ࡯࡮ࡣࡷࡩࠬ∿"): bstack1ll1l111l_opy_,
    bstack11l11l1_opy_ (u"ࠫࡦࡶࡰࡠࡣࡸࡸࡴࡳࡡࡵࡧࠪ≀"): bstack111l1l111l_opy_,
    bstack11l11l1_opy_ (u"ࠬࡺࡵࡳࡤࡲࡷࡨࡧ࡬ࡦࠩ≁"): bstack1llll1111ll1_opy_
  }
  return bstack111ll11ll1_opy_
@error_handler(class_method=False)
def bstack1llll111llll_opy_(bs_config):
  try:
    bstack1llll111l1l1_opy_ = json.loads(os.getenv(bstack11l11l1_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡢࡅࡈࡉࡅࡔࡕࡌࡆࡎࡒࡉࡕ࡛ࡢࡇࡔࡔࡆࡊࡉࡘࡖࡆ࡚ࡉࡐࡐࡢ࡝ࡒࡒࠧ≂"), bstack11l11l1_opy_ (u"ࠧࡼࡿࠪ≃")))
    bstack1llll111l1l1_opy_ = bstack1llll111l111_opy_(bs_config, bstack1llll111l1l1_opy_)
    return {
        bstack11l11l1_opy_ (u"ࠨࡵࡨࡸࡹ࡯࡮ࡨࡵࠪ≄"): bstack1llll111l1l1_opy_
    }
  except Exception as error:
    logger.error(bstack11l11l1_opy_ (u"ࠤࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥࡽࡨࡪ࡮ࡨࠤࡨࡸࡥࡢࡶ࡬ࡲ࡬ࠦࡧࡦࡶࡢࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࡢࡷࡪࡺࡴࡪࡰࡪࡷࠥ࡬࡯ࡳࠢࡗࡩࡸࡺࡈࡶࡤ࠽ࠤࠥࢁࡽࠣ≅").format(str(error)))
    return {}
def bstack1llll111l111_opy_(bs_config, bstack1llll111l1l1_opy_):
  if ((bstack11l11l1_opy_ (u"ࠪࡸࡺࡸࡢࡰࡕࡦࡥࡱ࡫ࠧ≆") in bs_config or not bstack1ll11lll11_opy_(bs_config)) and bstack111llll1_opy_.bstack111l1ll11l_opy_(bs_config)):
    bstack1llll111l1l1_opy_[bstack11l11l1_opy_ (u"ࠦ࡮ࡴࡣ࡭ࡷࡧࡩࡊࡴࡣࡰࡦࡨࡨࡊࡾࡴࡦࡰࡶ࡭ࡴࡴࠢ≇")] = True
  return bstack1llll111l1l1_opy_
def bstack1llll11l11l1_opy_(array, bstack1llll111l11l_opy_, bstack1llll111ll1l_opy_):
  result = {}
  for o in array:
    key = o[bstack1llll111l11l_opy_]
    result[key] = o[bstack1llll111ll1l_opy_]
  return result
def bstack1llll1l11111_opy_(bstack1l1l1l11l1_opy_=bstack11l11l1_opy_ (u"ࠬ࠭≈")):
  bstack1llll11l1111_opy_ = bstack111llll1_opy_.on()
  bstack1llll11l111l_opy_ = bstack1ll1l1l1_opy_.on()
  bstack1llll1111l1l_opy_ = percy.bstack1l11ll1111_opy_()
  if bstack1llll1111l1l_opy_ and not bstack1llll11l111l_opy_ and not bstack1llll11l1111_opy_:
    return bstack1l1l1l11l1_opy_ not in [bstack11l11l1_opy_ (u"࠭ࡃࡃࡖࡖࡩࡸࡹࡩࡰࡰࡆࡶࡪࡧࡴࡦࡦࠪ≉"), bstack11l11l1_opy_ (u"ࠧࡍࡱࡪࡇࡷ࡫ࡡࡵࡧࡧࠫ≊")]
  elif bstack1llll11l1111_opy_ and not bstack1llll11l111l_opy_:
    return bstack1l1l1l11l1_opy_ not in [bstack11l11l1_opy_ (u"ࠨࡊࡲࡳࡰࡘࡵ࡯ࡕࡷࡥࡷࡺࡥࡥࠩ≋"), bstack11l11l1_opy_ (u"ࠩࡋࡳࡴࡱࡒࡶࡰࡉ࡭ࡳ࡯ࡳࡩࡧࡧࠫ≌"), bstack11l11l1_opy_ (u"ࠪࡐࡴ࡭ࡃࡳࡧࡤࡸࡪࡪࠧ≍")]
  return bstack1llll11l1111_opy_ or bstack1llll11l111l_opy_ or bstack1llll1111l1l_opy_
@error_handler(class_method=False)
def bstack1llll11ll11l_opy_(bstack1l1l1l11l1_opy_, test=None):
  bstack1llll111lll1_opy_ = bstack111llll1_opy_.on()
  if not bstack1llll111lll1_opy_ or bstack1l1l1l11l1_opy_ not in [bstack11l11l1_opy_ (u"࡙ࠫ࡫ࡳࡵࡔࡸࡲࡋ࡯࡮ࡪࡵ࡫ࡩࡩ࠭≎")] or test == None:
    return None
  return {
    bstack11l11l1_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠬ≏"): bstack1llll111lll1_opy_ and bstack1ll11l1l_opy_(threading.current_thread(), bstack11l11l1_opy_ (u"࠭ࡡ࠲࠳ࡼࡔࡱࡧࡴࡧࡱࡵࡱࠬ≐"), None) == True and bstack111llll1_opy_.bstack11l1l1l1l_opy_(test[bstack11l11l1_opy_ (u"ࠧࡵࡣࡪࡷࠬ≑")])
  }
def bstack1llll111l1ll_opy_(bs_config, framework):
  bstack111l1l111l_opy_ = False
  bstack1ll1l111l_opy_ = False
  bstack1llll1111ll1_opy_ = False
  if bstack11l11l1_opy_ (u"ࠨࡶࡸࡶࡧࡵࡓࡤࡣ࡯ࡩࠬ≒") in bs_config:
    bstack1llll1111ll1_opy_ = True
  elif bstack11l11l1_opy_ (u"ࠩࡤࡴࡵ࠭≓") in bs_config:
    bstack111l1l111l_opy_ = True
  else:
    bstack1ll1l111l_opy_ = True
  bstack111ll11ll1_opy_ = {
    bstack11l11l1_opy_ (u"ࠪࡳࡧࡹࡥࡳࡸࡤࡦ࡮ࡲࡩࡵࡻࠪ≔"): bstack1ll1l1l1_opy_.bstack11l11l11ll1_opy_(bs_config, framework),
    bstack11l11l1_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠫ≕"): bstack111llll1_opy_.bstack111l1l1l11_opy_(bs_config),
    bstack11l11l1_opy_ (u"ࠬࡶࡥࡳࡥࡼࠫ≖"): bs_config.get(bstack11l11l1_opy_ (u"࠭ࡰࡦࡴࡦࡽࠬ≗"), False),
    bstack11l11l1_opy_ (u"ࠧࡢࡷࡷࡳࡲࡧࡴࡦࠩ≘"): bstack1ll1l111l_opy_,
    bstack11l11l1_opy_ (u"ࠨࡣࡳࡴࡤࡧࡵࡵࡱࡰࡥࡹ࡫ࠧ≙"): bstack111l1l111l_opy_,
    bstack11l11l1_opy_ (u"ࠩࡷࡹࡷࡨ࡯ࡴࡥࡤࡰࡪ࠭≚"): bstack1llll1111ll1_opy_
  }
  return bstack111ll11ll1_opy_