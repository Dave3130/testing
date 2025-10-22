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
import os
import json
import logging
import datetime
import threading
from bstack_utils.helper import bstack1111l11l111_opy_, bstack1l1l1llll1_opy_, get_host_info, bstack1111ll1llll_opy_, \
 bstack11l1l111l_opy_, bstack1l11l1ll_opy_, error_handler, bstack1111lllll11_opy_, bstack1lllll11_opy_
import bstack_utils.accessibility as bstack1lll11ll1_opy_
from bstack_utils.bstack1lll1llll_opy_ import bstack1llll1lll_opy_
from bstack_utils.bstack1llll111_opy_ import bstack1lll1111_opy_
from bstack_utils.percy import bstack1ll1111ll_opy_
from bstack_utils.config import Config
bstack1lllll1l1_opy_ = Config.bstack1111ll1l_opy_()
logger = logging.getLogger(__name__)
percy = bstack1ll1111ll_opy_()
@error_handler(class_method=False)
def bstack1llll11ll1ll_opy_(bs_config, bstack1l11l11l1l_opy_):
  try:
    data = {
        bstack111l1l_opy_ (u"ࠬ࡬࡯ࡳ࡯ࡤࡸࠬ∗"): bstack111l1l_opy_ (u"࠭ࡪࡴࡱࡱࠫ∘"),
        bstack111l1l_opy_ (u"ࠧࡱࡴࡲ࡮ࡪࡩࡴࡠࡰࡤࡱࡪ࠭∙"): bs_config.get(bstack111l1l_opy_ (u"ࠨࡲࡵࡳ࡯࡫ࡣࡵࡐࡤࡱࡪ࠭√"), bstack111l1l_opy_ (u"ࠩࠪ∛")),
        bstack111l1l_opy_ (u"ࠪࡲࡦࡳࡥࠨ∜"): bs_config.get(bstack111l1l_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡑࡥࡲ࡫ࠧ∝"), os.path.basename(os.path.abspath(os.getcwd()))),
        bstack111l1l_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡣ࡮ࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨ∞"): bs_config.get(bstack111l1l_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨ∟")),
        bstack111l1l_opy_ (u"ࠧࡥࡧࡶࡧࡷ࡯ࡰࡵ࡫ࡲࡲࠬ∠"): bs_config.get(bstack111l1l_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡄࡦࡵࡦࡶ࡮ࡶࡴࡪࡱࡱࠫ∡"), bstack111l1l_opy_ (u"ࠩࠪ∢")),
        bstack111l1l_opy_ (u"ࠪࡷࡹࡧࡲࡵࡧࡧࡣࡦࡺࠧ∣"): bstack1lllll11_opy_(),
        bstack111l1l_opy_ (u"ࠫࡹࡧࡧࡴࠩ∤"): bstack1111ll1llll_opy_(bs_config),
        bstack111l1l_opy_ (u"ࠬ࡮࡯ࡴࡶࡢ࡭ࡳ࡬࡯ࠨ∥"): get_host_info(),
        bstack111l1l_opy_ (u"࠭ࡣࡪࡡ࡬ࡲ࡫ࡵࠧ∦"): bstack1l1l1llll1_opy_(),
        bstack111l1l_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡥࡲࡶࡰࡢ࡭ࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧ∧"): os.environ.get(bstack111l1l_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡃࡗࡌࡐࡉࡥࡒࡖࡐࡢࡍࡉࡋࡎࡕࡋࡉࡍࡊࡘࠧ∨")),
        bstack111l1l_opy_ (u"ࠩࡩࡥ࡮ࡲࡥࡥࡡࡷࡩࡸࡺࡳࡠࡴࡨࡶࡺࡴࠧ∩"): os.environ.get(bstack111l1l_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡕࡉࡗ࡛ࡎࠨ∪"), False),
        bstack111l1l_opy_ (u"ࠫࡻ࡫ࡲࡴ࡫ࡲࡲࡤࡩ࡯࡯ࡶࡵࡳࡱ࠭∫"): bstack1111l11l111_opy_(),
        bstack111l1l_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠬ∬"): bstack1llll111l1l1_opy_(bs_config),
        bstack111l1l_opy_ (u"࠭ࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡧࡩࡹࡧࡩ࡭ࡵࠪ∭"): bstack1llll1111l1l_opy_(bstack1l11l11l1l_opy_),
        bstack111l1l_opy_ (u"ࠧࡱࡴࡲࡨࡺࡩࡴࡠ࡯ࡤࡴࠬ∮"): bstack1llll1111ll1_opy_(bs_config, bstack1l11l11l1l_opy_.get(bstack111l1l_opy_ (u"ࠨࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡺࡹࡥࡥࠩ∯"), bstack111l1l_opy_ (u"ࠩࠪ∰"))),
        bstack111l1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡃࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࠬ∱"): bstack11l1l111l_opy_(bs_config),
        bstack111l1l_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡲࡶࡨ࡮ࡥࡴࡶࡵࡥࡹ࡯࡯࡯ࠩ∲"): bstack1llll11111ll_opy_(bs_config)
    }
    return data
  except Exception as error:
    logger.error(bstack111l1l_opy_ (u"ࠧࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡࡹ࡫࡭ࡱ࡫ࠠࡤࡴࡨࡥࡹ࡯࡮ࡨࠢࡳࡥࡾࡲ࡯ࡢࡦࠣࡪࡴࡸࠠࡕࡧࡶࡸࡍࡻࡢ࠻ࠢࠣࡿࢂࠨ∳").format(str(error)))
    return None
def bstack1llll1111l1l_opy_(framework):
  return {
    bstack111l1l_opy_ (u"࠭ࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡐࡤࡱࡪ࠭∴"): framework.get(bstack111l1l_opy_ (u"ࠧࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡲࡦࡳࡥࠨ∵"), bstack111l1l_opy_ (u"ࠨࡒࡼࡸࡪࡹࡴࠨ∶")),
    bstack111l1l_opy_ (u"ࠩࡩࡶࡦࡳࡥࡸࡱࡵ࡯࡛࡫ࡲࡴ࡫ࡲࡲࠬ∷"): framework.get(bstack111l1l_opy_ (u"ࠪࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡥࡶࡦࡴࡶ࡭ࡴࡴࠧ∸")),
    bstack111l1l_opy_ (u"ࠫࡸࡪ࡫ࡗࡧࡵࡷ࡮ࡵ࡮ࠨ∹"): framework.get(bstack111l1l_opy_ (u"ࠬࡹࡤ࡬ࡡࡹࡩࡷࡹࡩࡰࡰࠪ∺")),
    bstack111l1l_opy_ (u"࠭࡬ࡢࡰࡪࡹࡦ࡭ࡥࠨ∻"): bstack111l1l_opy_ (u"ࠧࡱࡻࡷ࡬ࡴࡴࠧ∼"),
    bstack111l1l_opy_ (u"ࠨࡶࡨࡷࡹࡌࡲࡢ࡯ࡨࡻࡴࡸ࡫ࠨ∽"): framework.get(bstack111l1l_opy_ (u"ࠩࡷࡩࡸࡺࡆࡳࡣࡰࡩࡼࡵࡲ࡬ࠩ∾"))
  }
def bstack1llll11111ll_opy_(bs_config):
  bstack111l1l_opy_ (u"ࠥࠦࠧࠐࠠࠡࡔࡨࡸࡺࡸ࡮ࡴࠢࡷ࡬ࡪࠦࡴࡦࡵࡷࠤࡴࡸࡣࡩࡧࡶࡸࡷࡧࡴࡪࡱࡱࠤࡩࡧࡴࡢࠢࡩࡳࡷࠦࡢࡶ࡫࡯ࡨࠥࡹࡴࡢࡴࡷ࠲ࠏࠦࠠࠣࠤࠥ∿")
  if not bs_config:
    return {}
  bstack111ll1ll11l_opy_ = bstack1llll1lll_opy_(bs_config).bstack11l1111l111_opy_(bs_config)
  return bstack111ll1ll11l_opy_
def bstack11lll11l1_opy_(bs_config, framework):
  bstack11lll1lll_opy_ = False
  bstack11111l111l_opy_ = False
  bstack1llll1111l11_opy_ = False
  if bstack111l1l_opy_ (u"ࠫࡹࡻࡲࡣࡱࡖࡧࡦࡲࡥࠨ≀") in bs_config:
    bstack1llll1111l11_opy_ = True
  elif bstack111l1l_opy_ (u"ࠬࡧࡰࡱࠩ≁") in bs_config:
    bstack11lll1lll_opy_ = True
  else:
    bstack11111l111l_opy_ = True
  bstack11llll11l1_opy_ = {
    bstack111l1l_opy_ (u"࠭࡯ࡣࡵࡨࡶࡻࡧࡢࡪ࡮࡬ࡸࡾ࠭≂"): bstack1lll1111_opy_.bstack11l111lll1l_opy_(bs_config, framework),
    bstack111l1l_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠧ≃"): bstack1lll11ll1_opy_.bstack1l1lllll1l_opy_(bs_config),
    bstack111l1l_opy_ (u"ࠨࡲࡨࡶࡨࡿࠧ≄"): bs_config.get(bstack111l1l_opy_ (u"ࠩࡳࡩࡷࡩࡹࠨ≅"), False),
    bstack111l1l_opy_ (u"ࠪࡥࡺࡺ࡯࡮ࡣࡷࡩࠬ≆"): bstack11111l111l_opy_,
    bstack111l1l_opy_ (u"ࠫࡦࡶࡰࡠࡣࡸࡸࡴࡳࡡࡵࡧࠪ≇"): bstack11lll1lll_opy_,
    bstack111l1l_opy_ (u"ࠬࡺࡵࡳࡤࡲࡷࡨࡧ࡬ࡦࠩ≈"): bstack1llll1111l11_opy_
  }
  return bstack11llll11l1_opy_
@error_handler(class_method=False)
def bstack1llll111l1l1_opy_(bs_config):
  try:
    bstack1llll111l111_opy_ = json.loads(os.getenv(bstack111l1l_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡢࡅࡈࡉࡅࡔࡕࡌࡆࡎࡒࡉࡕ࡛ࡢࡇࡔࡔࡆࡊࡉࡘࡖࡆ࡚ࡉࡐࡐࡢ࡝ࡒࡒࠧ≉"), bstack111l1l_opy_ (u"ࠧࡼࡿࠪ≊")))
    bstack1llll111l111_opy_ = bstack1llll111ll1l_opy_(bs_config, bstack1llll111l111_opy_)
    return {
        bstack111l1l_opy_ (u"ࠨࡵࡨࡸࡹ࡯࡮ࡨࡵࠪ≋"): bstack1llll111l111_opy_
    }
  except Exception as error:
    logger.error(bstack111l1l_opy_ (u"ࠤࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥࡽࡨࡪ࡮ࡨࠤࡨࡸࡥࡢࡶ࡬ࡲ࡬ࠦࡧࡦࡶࡢࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࡢࡷࡪࡺࡴࡪࡰࡪࡷࠥ࡬࡯ࡳࠢࡗࡩࡸࡺࡈࡶࡤ࠽ࠤࠥࢁࡽࠣ≌").format(str(error)))
    return {}
def bstack1llll111ll1l_opy_(bs_config, bstack1llll111l111_opy_):
  if ((bstack111l1l_opy_ (u"ࠪࡸࡺࡸࡢࡰࡕࡦࡥࡱ࡫ࠧ≍") in bs_config or not bstack11l1l111l_opy_(bs_config)) and bstack1lll11ll1_opy_.bstack1l1lllll1l_opy_(bs_config)):
    bstack1llll111l111_opy_[bstack111l1l_opy_ (u"ࠦ࡮ࡴࡣ࡭ࡷࡧࡩࡊࡴࡣࡰࡦࡨࡨࡊࡾࡴࡦࡰࡶ࡭ࡴࡴࠢ≎")] = True
  return bstack1llll111l111_opy_
def bstack1llll11l1l1l_opy_(array, bstack1llll1111lll_opy_, bstack1llll111l11l_opy_):
  result = {}
  for o in array:
    key = o[bstack1llll1111lll_opy_]
    result[key] = o[bstack1llll111l11l_opy_]
  return result
def bstack1llll11lll1l_opy_(bstack1111l11ll_opy_=bstack111l1l_opy_ (u"ࠬ࠭≏")):
  bstack1llll111l1ll_opy_ = bstack1lll11ll1_opy_.on()
  bstack1llll11111l1_opy_ = bstack1lll1111_opy_.on()
  bstack1llll111111l_opy_ = percy.bstack111llll1ll_opy_()
  if bstack1llll111111l_opy_ and not bstack1llll11111l1_opy_ and not bstack1llll111l1ll_opy_:
    return bstack1111l11ll_opy_ not in [bstack111l1l_opy_ (u"࠭ࡃࡃࡖࡖࡩࡸࡹࡩࡰࡰࡆࡶࡪࡧࡴࡦࡦࠪ≐"), bstack111l1l_opy_ (u"ࠧࡍࡱࡪࡇࡷ࡫ࡡࡵࡧࡧࠫ≑")]
  elif bstack1llll111l1ll_opy_ and not bstack1llll11111l1_opy_:
    return bstack1111l11ll_opy_ not in [bstack111l1l_opy_ (u"ࠨࡊࡲࡳࡰࡘࡵ࡯ࡕࡷࡥࡷࡺࡥࡥࠩ≒"), bstack111l1l_opy_ (u"ࠩࡋࡳࡴࡱࡒࡶࡰࡉ࡭ࡳ࡯ࡳࡩࡧࡧࠫ≓"), bstack111l1l_opy_ (u"ࠪࡐࡴ࡭ࡃࡳࡧࡤࡸࡪࡪࠧ≔")]
  return bstack1llll111l1ll_opy_ or bstack1llll11111l1_opy_ or bstack1llll111111l_opy_
@error_handler(class_method=False)
def bstack1llll11l1ll1_opy_(bstack1111l11ll_opy_, test=None):
  bstack1llll111ll11_opy_ = bstack1lll11ll1_opy_.on()
  if not bstack1llll111ll11_opy_ or bstack1111l11ll_opy_ not in [bstack111l1l_opy_ (u"࡙ࠫ࡫ࡳࡵࡔࡸࡲࡋ࡯࡮ࡪࡵ࡫ࡩࡩ࠭≕")] or test == None:
    return None
  return {
    bstack111l1l_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠬ≖"): bstack1llll111ll11_opy_ and bstack1l11l1ll_opy_(threading.current_thread(), bstack111l1l_opy_ (u"࠭ࡡ࠲࠳ࡼࡔࡱࡧࡴࡧࡱࡵࡱࠬ≗"), None) == True and bstack1lll11ll1_opy_.bstack1l1ll11lll_opy_(test[bstack111l1l_opy_ (u"ࠧࡵࡣࡪࡷࠬ≘")])
  }
def bstack1llll1111ll1_opy_(bs_config, framework):
  bstack11lll1lll_opy_ = False
  bstack11111l111l_opy_ = False
  bstack1llll1111l11_opy_ = False
  if bstack111l1l_opy_ (u"ࠨࡶࡸࡶࡧࡵࡓࡤࡣ࡯ࡩࠬ≙") in bs_config:
    bstack1llll1111l11_opy_ = True
  elif bstack111l1l_opy_ (u"ࠩࡤࡴࡵ࠭≚") in bs_config:
    bstack11lll1lll_opy_ = True
  else:
    bstack11111l111l_opy_ = True
  bstack11llll11l1_opy_ = {
    bstack111l1l_opy_ (u"ࠪࡳࡧࡹࡥࡳࡸࡤࡦ࡮ࡲࡩࡵࡻࠪ≛"): bstack1lll1111_opy_.bstack11l111lll1l_opy_(bs_config, framework),
    bstack111l1l_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠫ≜"): bstack1lll11ll1_opy_.bstack11ll1l1ll1_opy_(bs_config),
    bstack111l1l_opy_ (u"ࠬࡶࡥࡳࡥࡼࠫ≝"): bs_config.get(bstack111l1l_opy_ (u"࠭ࡰࡦࡴࡦࡽࠬ≞"), False),
    bstack111l1l_opy_ (u"ࠧࡢࡷࡷࡳࡲࡧࡴࡦࠩ≟"): bstack11111l111l_opy_,
    bstack111l1l_opy_ (u"ࠨࡣࡳࡴࡤࡧࡵࡵࡱࡰࡥࡹ࡫ࠧ≠"): bstack11lll1lll_opy_,
    bstack111l1l_opy_ (u"ࠩࡷࡹࡷࡨ࡯ࡴࡥࡤࡰࡪ࠭≡"): bstack1llll1111l11_opy_
  }
  return bstack11llll11l1_opy_