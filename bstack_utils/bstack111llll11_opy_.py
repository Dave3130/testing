# coding: UTF-8
import sys
bstack1llll1l_opy_ = sys.version_info [0] == 2
bstack11ll1l_opy_ = 2048
bstack11l1_opy_ = 7
def bstack11l11ll_opy_ (bstack1lll_opy_):
    global bstack11111l_opy_
    bstack11ll11l_opy_ = ord (bstack1lll_opy_ [-1])
    bstack1l1l_opy_ = bstack1lll_opy_ [:-1]
    bstack1lll1l1_opy_ = bstack11ll11l_opy_ % len (bstack1l1l_opy_)
    bstack1l11ll_opy_ = bstack1l1l_opy_ [:bstack1lll1l1_opy_] + bstack1l1l_opy_ [bstack1lll1l1_opy_:]
    if bstack1llll1l_opy_:
        bstack1lllll1l_opy_ = unicode () .join ([unichr (ord (char) - bstack11ll1l_opy_ - (bstack11ll1ll_opy_ + bstack11ll11l_opy_) % bstack11l1_opy_) for bstack11ll1ll_opy_, char in enumerate (bstack1l11ll_opy_)])
    else:
        bstack1lllll1l_opy_ = str () .join ([chr (ord (char) - bstack11ll1l_opy_ - (bstack11ll1ll_opy_ + bstack11ll11l_opy_) % bstack11l1_opy_) for bstack11ll1ll_opy_, char in enumerate (bstack1l11ll_opy_)])
    return eval (bstack1lllll1l_opy_)
import os
import json
from bstack_utils.bstack11l1l11ll1_opy_ import get_logger
logger = get_logger(__name__)
class bstack1lllll11l111_opy_(object):
  bstack11111lll1_opy_ = os.path.join(os.path.expanduser(bstack11l11ll_opy_ (u"ࠬࢄࠧῧ")), bstack11l11ll_opy_ (u"࠭࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠭Ῠ"))
  bstack1lllll111ll1_opy_ = os.path.join(bstack11111lll1_opy_, bstack11l11ll_opy_ (u"ࠧࡤࡱࡰࡱࡦࡴࡤࡴ࠰࡭ࡷࡴࡴࠧῩ"))
  commands_to_wrap = None
  perform_scan = None
  bstack1l1111lll1_opy_ = None
  bstack11lll11l1l_opy_ = None
  bstack1lllll1111l1_opy_ = None
  bstack1lllll11111l_opy_ = None
  def __new__(cls):
    if not hasattr(cls, bstack11l11ll_opy_ (u"ࠨ࡫ࡱࡷࡹࡧ࡮ࡤࡧࠪῪ")):
      cls.instance = super(bstack1lllll11l111_opy_, cls).__new__(cls)
      cls.instance.bstack1lllll111l11_opy_()
    return cls.instance
  def bstack1lllll111l11_opy_(self):
    try:
      with open(self.bstack1lllll111ll1_opy_, bstack11l11ll_opy_ (u"ࠩࡵࠫΎ")) as bstack11111l1ll1_opy_:
        bstack1lllll111l1l_opy_ = bstack11111l1ll1_opy_.read()
        data = json.loads(bstack1lllll111l1l_opy_)
        if bstack11l11ll_opy_ (u"ࠪࡧࡴࡳ࡭ࡢࡰࡧࡷࠬῬ") in data:
          self.bstack1lllll111lll_opy_(data[bstack11l11ll_opy_ (u"ࠫࡨࡵ࡭࡮ࡣࡱࡨࡸ࠭῭")])
        if bstack11l11ll_opy_ (u"ࠬࡹࡣࡳ࡫ࡳࡸࡸ࠭΅") in data:
          self.bstack11ll111lll_opy_(data[bstack11l11ll_opy_ (u"࠭ࡳࡤࡴ࡬ࡴࡹࡹࠧ`")])
        if bstack11l11ll_opy_ (u"ࠧ࡯ࡱࡱࡆࡘࡺࡡࡤ࡭ࡌࡲ࡫ࡸࡡࡂ࠳࠴ࡽࡈ࡮ࡲࡰ࡯ࡨࡓࡵࡺࡩࡰࡰࡶࠫ῰") in data:
          self.bstack1lllll1111ll_opy_(data[bstack11l11ll_opy_ (u"ࠨࡰࡲࡲࡇ࡙ࡴࡢࡥ࡮ࡍࡳ࡬ࡲࡢࡃ࠴࠵ࡾࡉࡨࡳࡱࡰࡩࡔࡶࡴࡪࡱࡱࡷࠬ῱")])
    except:
      pass
  def bstack1lllll1111ll_opy_(self, bstack1lllll11111l_opy_):
    if bstack1lllll11111l_opy_ != None:
      self.bstack1lllll11111l_opy_ = bstack1lllll11111l_opy_
  def bstack11ll111lll_opy_(self, scripts):
    if scripts != None:
      self.perform_scan = scripts.get(bstack11l11ll_opy_ (u"ࠩࡶࡧࡦࡴࠧῲ"),bstack11l11ll_opy_ (u"ࠪࠫῳ"))
      self.bstack1l1111lll1_opy_ = scripts.get(bstack11l11ll_opy_ (u"ࠫ࡬࡫ࡴࡓࡧࡶࡹࡱࡺࡳࠨῴ"),bstack11l11ll_opy_ (u"ࠬ࠭῵"))
      self.bstack11lll11l1l_opy_ = scripts.get(bstack11l11ll_opy_ (u"࠭ࡧࡦࡶࡕࡩࡸࡻ࡬ࡵࡵࡖࡹࡲࡳࡡࡳࡻࠪῶ"),bstack11l11ll_opy_ (u"ࠧࠨῷ"))
      self.bstack1lllll1111l1_opy_ = scripts.get(bstack11l11ll_opy_ (u"ࠨࡵࡤࡺࡪࡘࡥࡴࡷ࡯ࡸࡸ࠭Ὸ"),bstack11l11ll_opy_ (u"ࠩࠪΌ"))
  def bstack1lllll111lll_opy_(self, commands_to_wrap):
    if commands_to_wrap != None and len(commands_to_wrap) != 0:
      self.commands_to_wrap = commands_to_wrap
  def store(self):
    try:
      with open(self.bstack1lllll111ll1_opy_, bstack11l11ll_opy_ (u"ࠪࡻࠬῺ")) as file:
        json.dump({
          bstack11l11ll_opy_ (u"ࠦࡨࡵ࡭࡮ࡣࡱࡨࡸࠨΏ"): self.commands_to_wrap,
          bstack11l11ll_opy_ (u"ࠧࡹࡣࡳ࡫ࡳࡸࡸࠨῼ"): {
            bstack11l11ll_opy_ (u"ࠨࡳࡤࡣࡱࠦ´"): self.perform_scan,
            bstack11l11ll_opy_ (u"ࠢࡨࡧࡷࡖࡪࡹࡵ࡭ࡶࡶࠦ῾"): self.bstack1l1111lll1_opy_,
            bstack11l11ll_opy_ (u"ࠣࡩࡨࡸࡗ࡫ࡳࡶ࡮ࡷࡷࡘࡻ࡭࡮ࡣࡵࡽࠧ῿"): self.bstack11lll11l1l_opy_,
            bstack11l11ll_opy_ (u"ࠤࡶࡥࡻ࡫ࡒࡦࡵࡸࡰࡹࡹࠢ "): self.bstack1lllll1111l1_opy_
          },
          bstack11l11ll_opy_ (u"ࠥࡲࡴࡴࡂࡔࡶࡤࡧࡰࡏ࡮ࡧࡴࡤࡅ࠶࠷ࡹࡄࡪࡵࡳࡲ࡫ࡏࡱࡶ࡬ࡳࡳࡹࠢ "): self.bstack1lllll11111l_opy_
        }, file)
    except Exception as e:
      logger.error(bstack11l11ll_opy_ (u"ࠦࡊࡸࡲࡰࡴࠣࡻ࡭࡯࡬ࡦࠢࡶࡸࡴࡸࡩ࡯ࡩࠣࡧࡴࡳ࡭ࡢࡰࡧࡷ࠿ࠦࡻࡾࠤ ").format(e))
      pass
  def bstack11l1ll1111_opy_(self, command_name):
    try:
      return any(command.get(bstack11l11ll_opy_ (u"ࠬࡴࡡ࡮ࡧࠪ ")) == command_name for command in self.commands_to_wrap)
    except:
      return False
bstack111llll11_opy_ = bstack1lllll11l111_opy_()