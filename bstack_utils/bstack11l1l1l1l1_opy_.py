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
import os
import json
from bstack_utils.bstack111ll1ll1l_opy_ import get_logger
logger = get_logger(__name__)
class bstack1lllll11ll1l_opy_(object):
  bstack11l11ll1ll_opy_ = os.path.join(os.path.expanduser(bstack11111_opy_ (u"ࠬࢄࠧᾚ")), bstack11111_opy_ (u"࠭࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠭ᾛ"))
  bstack1lllll1l11l1_opy_ = os.path.join(bstack11l11ll1ll_opy_, bstack11111_opy_ (u"ࠧࡤࡱࡰࡱࡦࡴࡤࡴ࠰࡭ࡷࡴࡴࠧᾜ"))
  commands_to_wrap = None
  perform_scan = None
  bstack1111ll11l_opy_ = None
  bstack111lll1l1_opy_ = None
  bstack1lllll1l1l11_opy_ = None
  bstack1lllll11llll_opy_ = None
  def __new__(cls):
    if not hasattr(cls, bstack11111_opy_ (u"ࠨ࡫ࡱࡷࡹࡧ࡮ࡤࡧࠪᾝ")):
      cls.instance = super(bstack1lllll11ll1l_opy_, cls).__new__(cls)
      cls.instance.bstack1lllll11lll1_opy_()
    return cls.instance
  def bstack1lllll11lll1_opy_(self):
    try:
      with open(self.bstack1lllll1l11l1_opy_, bstack11111_opy_ (u"ࠩࡵࠫᾞ")) as bstack111l1l11l1_opy_:
        bstack1lllll1l111l_opy_ = bstack111l1l11l1_opy_.read()
        data = json.loads(bstack1lllll1l111l_opy_)
        if bstack11111_opy_ (u"ࠪࡧࡴࡳ࡭ࡢࡰࡧࡷࠬᾟ") in data:
          self.bstack1lllll1l11ll_opy_(data[bstack11111_opy_ (u"ࠫࡨࡵ࡭࡮ࡣࡱࡨࡸ࠭ᾠ")])
        if bstack11111_opy_ (u"ࠬࡹࡣࡳ࡫ࡳࡸࡸ࠭ᾡ") in data:
          self.bstack1llll1ll11_opy_(data[bstack11111_opy_ (u"࠭ࡳࡤࡴ࡬ࡴࡹࡹࠧᾢ")])
        if bstack11111_opy_ (u"ࠧ࡯ࡱࡱࡆࡘࡺࡡࡤ࡭ࡌࡲ࡫ࡸࡡࡂ࠳࠴ࡽࡈ࡮ࡲࡰ࡯ࡨࡓࡵࡺࡩࡰࡰࡶࠫᾣ") in data:
          self.bstack1lllll1l1111_opy_(data[bstack11111_opy_ (u"ࠨࡰࡲࡲࡇ࡙ࡴࡢࡥ࡮ࡍࡳ࡬ࡲࡢࡃ࠴࠵ࡾࡉࡨࡳࡱࡰࡩࡔࡶࡴࡪࡱࡱࡷࠬᾤ")])
    except:
      pass
  def bstack1lllll1l1111_opy_(self, bstack1lllll11llll_opy_):
    if bstack1lllll11llll_opy_ != None:
      self.bstack1lllll11llll_opy_ = bstack1lllll11llll_opy_
  def bstack1llll1ll11_opy_(self, scripts):
    if scripts != None:
      self.perform_scan = scripts.get(bstack11111_opy_ (u"ࠩࡶࡧࡦࡴࠧᾥ"),bstack11111_opy_ (u"ࠪࠫᾦ"))
      self.bstack1111ll11l_opy_ = scripts.get(bstack11111_opy_ (u"ࠫ࡬࡫ࡴࡓࡧࡶࡹࡱࡺࡳࠨᾧ"),bstack11111_opy_ (u"ࠬ࠭ᾨ"))
      self.bstack111lll1l1_opy_ = scripts.get(bstack11111_opy_ (u"࠭ࡧࡦࡶࡕࡩࡸࡻ࡬ࡵࡵࡖࡹࡲࡳࡡࡳࡻࠪᾩ"),bstack11111_opy_ (u"ࠧࠨᾪ"))
      self.bstack1lllll1l1l11_opy_ = scripts.get(bstack11111_opy_ (u"ࠨࡵࡤࡺࡪࡘࡥࡴࡷ࡯ࡸࡸ࠭ᾫ"),bstack11111_opy_ (u"ࠩࠪᾬ"))
  def bstack1lllll1l11ll_opy_(self, commands_to_wrap):
    if commands_to_wrap != None and len(commands_to_wrap) != 0:
      self.commands_to_wrap = commands_to_wrap
  def store(self):
    try:
      with open(self.bstack1lllll1l11l1_opy_, bstack11111_opy_ (u"ࠪࡻࠬᾭ")) as file:
        json.dump({
          bstack11111_opy_ (u"ࠦࡨࡵ࡭࡮ࡣࡱࡨࡸࠨᾮ"): self.commands_to_wrap,
          bstack11111_opy_ (u"ࠧࡹࡣࡳ࡫ࡳࡸࡸࠨᾯ"): {
            bstack11111_opy_ (u"ࠨࡳࡤࡣࡱࠦᾰ"): self.perform_scan,
            bstack11111_opy_ (u"ࠢࡨࡧࡷࡖࡪࡹࡵ࡭ࡶࡶࠦᾱ"): self.bstack1111ll11l_opy_,
            bstack11111_opy_ (u"ࠣࡩࡨࡸࡗ࡫ࡳࡶ࡮ࡷࡷࡘࡻ࡭࡮ࡣࡵࡽࠧᾲ"): self.bstack111lll1l1_opy_,
            bstack11111_opy_ (u"ࠤࡶࡥࡻ࡫ࡒࡦࡵࡸࡰࡹࡹࠢᾳ"): self.bstack1lllll1l1l11_opy_
          },
          bstack11111_opy_ (u"ࠥࡲࡴࡴࡂࡔࡶࡤࡧࡰࡏ࡮ࡧࡴࡤࡅ࠶࠷ࡹࡄࡪࡵࡳࡲ࡫ࡏࡱࡶ࡬ࡳࡳࡹࠢᾴ"): self.bstack1lllll11llll_opy_
        }, file)
    except Exception as e:
      logger.error(bstack11111_opy_ (u"ࠦࡊࡸࡲࡰࡴࠣࡻ࡭࡯࡬ࡦࠢࡶࡸࡴࡸࡩ࡯ࡩࠣࡧࡴࡳ࡭ࡢࡰࡧࡷ࠿ࠦࡻࡾࠤ᾵").format(e))
      pass
  def bstack1ll11111l1_opy_(self, command_name):
    try:
      return any(command.get(bstack11111_opy_ (u"ࠬࡴࡡ࡮ࡧࠪᾶ")) == command_name for command in self.commands_to_wrap)
    except:
      return False
bstack11l1l1l1l1_opy_ = bstack1lllll11ll1l_opy_()