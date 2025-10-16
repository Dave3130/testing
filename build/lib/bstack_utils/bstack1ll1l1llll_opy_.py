# coding: UTF-8
import sys
bstack11l1_opy_ = sys.version_info [0] == 2
bstack1l1l1ll_opy_ = 2048
bstack1llllll1_opy_ = 7
def bstack1l_opy_ (bstack11l1lll_opy_):
    global bstack1ll1ll1_opy_
    bstack1ll1l_opy_ = ord (bstack11l1lll_opy_ [-1])
    bstack1lll11_opy_ = bstack11l1lll_opy_ [:-1]
    bstack111l111_opy_ = bstack1ll1l_opy_ % len (bstack1lll11_opy_)
    bstack1ll11l_opy_ = bstack1lll11_opy_ [:bstack111l111_opy_] + bstack1lll11_opy_ [bstack111l111_opy_:]
    if bstack11l1_opy_:
        bstack1l1ll1l_opy_ = unicode () .join ([unichr (ord (char) - bstack1l1l1ll_opy_ - (bstack111l11_opy_ + bstack1ll1l_opy_) % bstack1llllll1_opy_) for bstack111l11_opy_, char in enumerate (bstack1ll11l_opy_)])
    else:
        bstack1l1ll1l_opy_ = str () .join ([chr (ord (char) - bstack1l1l1ll_opy_ - (bstack111l11_opy_ + bstack1ll1l_opy_) % bstack1llllll1_opy_) for bstack111l11_opy_, char in enumerate (bstack1ll11l_opy_)])
    return eval (bstack1l1ll1l_opy_)
import os
import json
from bstack_utils.bstack111ll1l1l_opy_ import get_logger
logger = get_logger(__name__)
class bstack1lllll1l1ll1_opy_(object):
  bstack1l11llll1l_opy_ = os.path.join(os.path.expanduser(bstack1l_opy_ (u"ࠩࢁࠫᾬ")), bstack1l_opy_ (u"ࠪ࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࠪᾭ"))
  bstack1lllll1l111l_opy_ = os.path.join(bstack1l11llll1l_opy_, bstack1l_opy_ (u"ࠫࡨࡵ࡭࡮ࡣࡱࡨࡸ࠴ࡪࡴࡱࡱࠫᾮ"))
  commands_to_wrap = None
  perform_scan = None
  bstack1l1l1llll_opy_ = None
  bstack111l111l1_opy_ = None
  bstack1lllll1l1l11_opy_ = None
  bstack1lllll1l11l1_opy_ = None
  def __new__(cls):
    if not hasattr(cls, bstack1l_opy_ (u"ࠬ࡯࡮ࡴࡶࡤࡲࡨ࡫ࠧᾯ")):
      cls.instance = super(bstack1lllll1l1ll1_opy_, cls).__new__(cls)
      cls.instance.bstack1lllll1l11ll_opy_()
    return cls.instance
  def bstack1lllll1l11ll_opy_(self):
    try:
      with open(self.bstack1lllll1l111l_opy_, bstack1l_opy_ (u"࠭ࡲࠨᾰ")) as bstack11l11l11l_opy_:
        bstack1lllll1l1111_opy_ = bstack11l11l11l_opy_.read()
        data = json.loads(bstack1lllll1l1111_opy_)
        if bstack1l_opy_ (u"ࠧࡤࡱࡰࡱࡦࡴࡤࡴࠩᾱ") in data:
          self.bstack1lllll1l1l1l_opy_(data[bstack1l_opy_ (u"ࠨࡥࡲࡱࡲࡧ࡮ࡥࡵࠪᾲ")])
        if bstack1l_opy_ (u"ࠩࡶࡧࡷ࡯ࡰࡵࡵࠪᾳ") in data:
          self.bstack1l11l1llll_opy_(data[bstack1l_opy_ (u"ࠪࡷࡨࡸࡩࡱࡶࡶࠫᾴ")])
        if bstack1l_opy_ (u"ࠫࡳࡵ࡮ࡃࡕࡷࡥࡨࡱࡉ࡯ࡨࡵࡥࡆ࠷࠱ࡺࡅ࡫ࡶࡴࡳࡥࡐࡲࡷ࡭ࡴࡴࡳࠨ᾵") in data:
          self.bstack1lllll1l1lll_opy_(data[bstack1l_opy_ (u"ࠬࡴ࡯࡯ࡄࡖࡸࡦࡩ࡫ࡊࡰࡩࡶࡦࡇ࠱࠲ࡻࡆ࡬ࡷࡵ࡭ࡦࡑࡳࡸ࡮ࡵ࡮ࡴࠩᾶ")])
    except:
      pass
  def bstack1lllll1l1lll_opy_(self, bstack1lllll1l11l1_opy_):
    if bstack1lllll1l11l1_opy_ != None:
      self.bstack1lllll1l11l1_opy_ = bstack1lllll1l11l1_opy_
  def bstack1l11l1llll_opy_(self, scripts):
    if scripts != None:
      self.perform_scan = scripts.get(bstack1l_opy_ (u"࠭ࡳࡤࡣࡱࠫᾷ"),bstack1l_opy_ (u"ࠧࠨᾸ"))
      self.bstack1l1l1llll_opy_ = scripts.get(bstack1l_opy_ (u"ࠨࡩࡨࡸࡗ࡫ࡳࡶ࡮ࡷࡷࠬᾹ"),bstack1l_opy_ (u"ࠩࠪᾺ"))
      self.bstack111l111l1_opy_ = scripts.get(bstack1l_opy_ (u"ࠪ࡫ࡪࡺࡒࡦࡵࡸࡰࡹࡹࡓࡶ࡯ࡰࡥࡷࡿࠧΆ"),bstack1l_opy_ (u"ࠫࠬᾼ"))
      self.bstack1lllll1l1l11_opy_ = scripts.get(bstack1l_opy_ (u"ࠬࡹࡡࡷࡧࡕࡩࡸࡻ࡬ࡵࡵࠪ᾽"),bstack1l_opy_ (u"࠭ࠧι"))
  def bstack1lllll1l1l1l_opy_(self, commands_to_wrap):
    if commands_to_wrap != None and len(commands_to_wrap) != 0:
      self.commands_to_wrap = commands_to_wrap
  def store(self):
    try:
      with open(self.bstack1lllll1l111l_opy_, bstack1l_opy_ (u"ࠧࡸࠩ᾿")) as file:
        json.dump({
          bstack1l_opy_ (u"ࠣࡥࡲࡱࡲࡧ࡮ࡥࡵࠥ῀"): self.commands_to_wrap,
          bstack1l_opy_ (u"ࠤࡶࡧࡷ࡯ࡰࡵࡵࠥ῁"): {
            bstack1l_opy_ (u"ࠥࡷࡨࡧ࡮ࠣῂ"): self.perform_scan,
            bstack1l_opy_ (u"ࠦ࡬࡫ࡴࡓࡧࡶࡹࡱࡺࡳࠣῃ"): self.bstack1l1l1llll_opy_,
            bstack1l_opy_ (u"ࠧ࡭ࡥࡵࡔࡨࡷࡺࡲࡴࡴࡕࡸࡱࡲࡧࡲࡺࠤῄ"): self.bstack111l111l1_opy_,
            bstack1l_opy_ (u"ࠨࡳࡢࡸࡨࡖࡪࡹࡵ࡭ࡶࡶࠦ῅"): self.bstack1lllll1l1l11_opy_
          },
          bstack1l_opy_ (u"ࠢ࡯ࡱࡱࡆࡘࡺࡡࡤ࡭ࡌࡲ࡫ࡸࡡࡂ࠳࠴ࡽࡈ࡮ࡲࡰ࡯ࡨࡓࡵࡺࡩࡰࡰࡶࠦῆ"): self.bstack1lllll1l11l1_opy_
        }, file)
    except Exception as e:
      logger.error(bstack1l_opy_ (u"ࠣࡇࡵࡶࡴࡸࠠࡸࡪ࡬ࡰࡪࠦࡳࡵࡱࡵ࡭ࡳ࡭ࠠࡤࡱࡰࡱࡦࡴࡤࡴ࠼ࠣࡿࢂࠨῇ").format(e))
      pass
  def bstack1ll11lll11_opy_(self, command_name):
    try:
      return any(command.get(bstack1l_opy_ (u"ࠩࡱࡥࡲ࡫ࠧῈ")) == command_name for command in self.commands_to_wrap)
    except:
      return False
bstack1ll1l1llll_opy_ = bstack1lllll1l1ll1_opy_()