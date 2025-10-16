# coding: UTF-8
import sys
bstack11llll1_opy_ = sys.version_info [0] == 2
bstack11lll1l_opy_ = 2048
bstack1l1l1l1_opy_ = 7
def bstack1ll11_opy_ (bstack11l11ll_opy_):
    global bstack11l1lll_opy_
    bstack1l1l111_opy_ = ord (bstack11l11ll_opy_ [-1])
    bstack11_opy_ = bstack11l11ll_opy_ [:-1]
    bstack1l1llll_opy_ = bstack1l1l111_opy_ % len (bstack11_opy_)
    bstack11111_opy_ = bstack11_opy_ [:bstack1l1llll_opy_] + bstack11_opy_ [bstack1l1llll_opy_:]
    if bstack11llll1_opy_:
        bstack111_opy_ = unicode () .join ([unichr (ord (char) - bstack11lll1l_opy_ - (bstack1111ll1_opy_ + bstack1l1l111_opy_) % bstack1l1l1l1_opy_) for bstack1111ll1_opy_, char in enumerate (bstack11111_opy_)])
    else:
        bstack111_opy_ = str () .join ([chr (ord (char) - bstack11lll1l_opy_ - (bstack1111ll1_opy_ + bstack1l1l111_opy_) % bstack1l1l1l1_opy_) for bstack1111ll1_opy_, char in enumerate (bstack11111_opy_)])
    return eval (bstack111_opy_)
import os
import re
import sys
import json
import time
import shutil
import tempfile
import requests
import subprocess
from threading import Thread
from os.path import expanduser
from bstack_utils.constants import *
from requests.auth import HTTPBasicAuth
from bstack_utils.helper import bstack11ll1llll_opy_
from bstack_utils.measure import measure
from bstack_utils.bstack1l1l111ll1_opy_ import bstack111lll1ll_opy_
class bstack1l1l11l1l_opy_:
  working_dir = os.getcwd()
  bstack1l1lllll11_opy_ = False
  config = {}
  bstack111l11lll1l_opy_ = bstack1ll11_opy_ (u"ࠨࠩἦ")
  binary_path = bstack1ll11_opy_ (u"ࠩࠪἧ")
  bstack1llllll111l1_opy_ = bstack1ll11_opy_ (u"ࠪࠫἨ")
  bstack1l1ll111l_opy_ = False
  bstack1lllllll1ll1_opy_ = None
  bstack111111l1ll1_opy_ = {}
  bstack1111111lll1_opy_ = 300
  bstack11111111ll1_opy_ = False
  logger = None
  bstack1lllllll1l11_opy_ = False
  bstack1lll111ll1_opy_ = False
  percy_build_id = None
  bstack1111111l111_opy_ = bstack1ll11_opy_ (u"ࠫࠬἩ")
  bstack1lllll1ll1l1_opy_ = {
    bstack1ll11_opy_ (u"ࠬࡩࡨࡳࡱࡰࡩࠬἪ") : 1,
    bstack1ll11_opy_ (u"࠭ࡦࡪࡴࡨࡪࡴࡾࠧἫ") : 2,
    bstack1ll11_opy_ (u"ࠧࡦࡦࡪࡩࠬἬ") : 3,
    bstack1ll11_opy_ (u"ࠨࡵࡤࡪࡦࡸࡩࠨἭ") : 4
  }
  def __init__(self) -> None: pass
  def bstack1llllllll1l1_opy_(self):
    bstack1lllllll1l1l_opy_ = bstack1ll11_opy_ (u"ࠩࠪἮ")
    bstack1llllll1ll1l_opy_ = sys.platform
    bstack111111111l1_opy_ = bstack1ll11_opy_ (u"ࠪࡴࡪࡸࡣࡺࠩἯ")
    if re.match(bstack1ll11_opy_ (u"ࠦࡩࡧࡲࡸ࡫ࡱࢀࡲࡧࡣࠡࡱࡶࠦἰ"), bstack1llllll1ll1l_opy_) != None:
      bstack1lllllll1l1l_opy_ = bstack11l1l111l11_opy_ + bstack1ll11_opy_ (u"ࠧ࠵ࡰࡦࡴࡦࡽ࠲ࡵࡳࡹ࠰ࡽ࡭ࡵࠨἱ")
      self.bstack1111111l111_opy_ = bstack1ll11_opy_ (u"࠭࡭ࡢࡥࠪἲ")
    elif re.match(bstack1ll11_opy_ (u"ࠢ࡮ࡵࡺ࡭ࡳࢂ࡭ࡴࡻࡶࢀࡲ࡯࡮ࡨࡹࡿࡧࡾ࡭ࡷࡪࡰࡿࡦࡨࡩࡷࡪࡰࡿࡻ࡮ࡴࡣࡦࡾࡨࡱࡨࢂࡷࡪࡰ࠶࠶ࠧἳ"), bstack1llllll1ll1l_opy_) != None:
      bstack1lllllll1l1l_opy_ = bstack11l1l111l11_opy_ + bstack1ll11_opy_ (u"ࠣ࠱ࡳࡩࡷࡩࡹ࠮ࡹ࡬ࡲ࠳ࢀࡩࡱࠤἴ")
      bstack111111111l1_opy_ = bstack1ll11_opy_ (u"ࠤࡳࡩࡷࡩࡹ࠯ࡧࡻࡩࠧἵ")
      self.bstack1111111l111_opy_ = bstack1ll11_opy_ (u"ࠪࡻ࡮ࡴࠧἶ")
    else:
      bstack1lllllll1l1l_opy_ = bstack11l1l111l11_opy_ + bstack1ll11_opy_ (u"ࠦ࠴ࡶࡥࡳࡥࡼ࠱ࡱ࡯࡮ࡶࡺ࠱ࡾ࡮ࡶࠢἷ")
      self.bstack1111111l111_opy_ = bstack1ll11_opy_ (u"ࠬࡲࡩ࡯ࡷࡻࠫἸ")
    return bstack1lllllll1l1l_opy_, bstack111111111l1_opy_
  def bstack111111ll11l_opy_(self):
    try:
      bstack1111111l1l1_opy_ = [os.path.join(expanduser(bstack1ll11_opy_ (u"ࠨࡾࠣἹ")), bstack1ll11_opy_ (u"ࠧ࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠧἺ")), self.working_dir, tempfile.gettempdir()]
      for path in bstack1111111l1l1_opy_:
        if(self.bstack111111l111l_opy_(path)):
          return path
      raise bstack1ll11_opy_ (u"ࠣࡗࡱࡥࡧࡲࡥࠡࡶࡲࠤࡩࡵࡷ࡯࡮ࡲࡥࡩࠦࡰࡦࡴࡦࡽࠥࡨࡩ࡯ࡣࡵࡽࠧἻ")
    except Exception as e:
      self.logger.error(bstack1ll11_opy_ (u"ࠤࡉࡥ࡮ࡲࡥࡥࠢࡷࡳࠥ࡬ࡩ࡯ࡦࠣࡥࡻࡧࡩ࡭ࡣࡥࡰࡪࠦࡰࡢࡶ࡫ࠤ࡫ࡵࡲࠡࡲࡨࡶࡨࡿࠠࡥࡱࡺࡲࡱࡵࡡࡥ࠮ࠣࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦ࠭ࠡࡽࢀࠦἼ").format(e))
  def bstack111111l111l_opy_(self, path):
    try:
      if not os.path.exists(path):
        os.makedirs(path)
      return True
    except:
      return False
  def bstack1lllll1lll1l_opy_(self, bstack1llllllll1ll_opy_):
    return os.path.join(bstack1llllllll1ll_opy_, self.bstack111l11lll1l_opy_ + bstack1ll11_opy_ (u"ࠥ࠲ࡪࡺࡡࡨࠤἽ"))
  def bstack1lllll1lll11_opy_(self, bstack1llllllll1ll_opy_, bstack1llllll11l1l_opy_):
    if not bstack1llllll11l1l_opy_: return
    try:
      bstack111111l1111_opy_ = self.bstack1lllll1lll1l_opy_(bstack1llllllll1ll_opy_)
      with open(bstack111111l1111_opy_, bstack1ll11_opy_ (u"ࠦࡼࠨἾ")) as f:
        f.write(bstack1llllll11l1l_opy_)
        self.logger.debug(bstack1ll11_opy_ (u"࡙ࠧࡡࡷࡧࡧࠤࡳ࡫ࡷࠡࡇࡗࡥ࡬ࠦࡦࡰࡴࠣࡴࡪࡸࡣࡺࠤἿ"))
    except Exception as e:
      self.logger.error(bstack1ll11_opy_ (u"ࠨࡕ࡯ࡣࡥࡰࡪࠦࡴࡰࠢࡶࡥࡻ࡫ࠠࡵࡪࡨࠤࡪࡺࡡࡨ࠮ࠣࡩࡷࡸ࡯ࡳ࠼ࠣࡿࢂࠨὀ").format(e))
  def bstack1llllll11111_opy_(self, bstack1llllllll1ll_opy_):
    try:
      bstack111111l1111_opy_ = self.bstack1lllll1lll1l_opy_(bstack1llllllll1ll_opy_)
      if os.path.exists(bstack111111l1111_opy_):
        with open(bstack111111l1111_opy_, bstack1ll11_opy_ (u"ࠢࡳࠤὁ")) as f:
          bstack1llllll11l1l_opy_ = f.read().strip()
          return bstack1llllll11l1l_opy_ if bstack1llllll11l1l_opy_ else None
    except Exception as e:
      self.logger.error(bstack1ll11_opy_ (u"ࠣࡈࡤ࡭ࡱ࡫ࡤࠡ࡮ࡲࡥࡩ࡯࡮ࡨࠢࡈࡘࡦ࡭ࠬࠡࡧࡵࡶࡴࡸ࠺ࠡࡽࢀࠦὂ").format(e))
  def bstack1111111111l_opy_(self, bstack1llllllll1ll_opy_, bstack1lllllll1l1l_opy_):
    bstack1llllll11ll1_opy_ = self.bstack1llllll11111_opy_(bstack1llllllll1ll_opy_)
    if bstack1llllll11ll1_opy_:
      try:
        bstack1lllllll1111_opy_ = self.bstack1lllllllllll_opy_(bstack1llllll11ll1_opy_, bstack1lllllll1l1l_opy_)
        if not bstack1lllllll1111_opy_:
          self.logger.debug(bstack1ll11_opy_ (u"ࠤࡓࡩࡷࡩࡹࠡࡤ࡬ࡲࡦࡸࡹࠡ࡫ࡶࠤࡺࡶࠠࡵࡱࠣࡨࡦࡺࡥࠡࠪࡈࡘࡦ࡭ࠠࡶࡰࡦ࡬ࡦࡴࡧࡦࡦࠬࠦὃ"))
          return True
        self.logger.debug(bstack1ll11_opy_ (u"ࠥࡒࡪࡽࠠࡑࡧࡵࡧࡾࠦࡢࡪࡰࡤࡶࡾࠦࡶࡦࡴࡶ࡭ࡴࡴࠠࡢࡸࡤ࡭ࡱࡧࡢ࡭ࡧ࠯ࠤࡩࡵࡷ࡯࡮ࡲࡥࡩ࡯࡮ࡨࠢࡸࡴࡩࡧࡴࡦࠤὄ"))
        return False
      except Exception as e:
        self.logger.warn(bstack1ll11_opy_ (u"ࠦࡋࡧࡩ࡭ࡧࡧࠤࡹࡵࠠࡤࡪࡨࡧࡰࠦࡦࡰࡴࠣࡦ࡮ࡴࡡࡳࡻࠣࡹࡵࡪࡡࡵࡧࡶ࠰ࠥࡻࡳࡪࡰࡪࠤࡪࡾࡩࡴࡶ࡬ࡲ࡬ࠦࡢࡪࡰࡤࡶࡾࡀࠠࡼࡿࠥὅ").format(e))
    return False
  def bstack1lllllllllll_opy_(self, bstack1llllll11ll1_opy_, bstack1lllllll1l1l_opy_):
    try:
      headers = {
        bstack1ll11_opy_ (u"ࠧࡏࡦ࠮ࡐࡲࡲࡪ࠳ࡍࡢࡶࡦ࡬ࠧ὆"): bstack1llllll11ll1_opy_
      }
      response = bstack11ll1llll_opy_(bstack1ll11_opy_ (u"࠭ࡇࡆࡖࠪ὇"), bstack1lllllll1l1l_opy_, {}, {bstack1ll11_opy_ (u"ࠢࡩࡧࡤࡨࡪࡸࡳࠣὈ"): headers})
      if response.status_code == 304:
        return False
      return True
    except Exception as e:
      raise(bstack1ll11_opy_ (u"ࠣࡇࡵࡶࡴࡸࠠࡤࡪࡨࡧࡰ࡯࡮ࡨࠢࡩࡳࡷࠦࡐࡦࡴࡦࡽࠥࡨࡩ࡯ࡣࡵࡽࠥࡻࡰࡥࡣࡷࡩࡸࡀࠠࡼࡿࠥὉ").format(e))
  @measure(event_name=EVENTS.bstack11l1l1lll11_opy_, stage=STAGE.bstack1111l1111_opy_)
  def bstack111111l1lll_opy_(self, bstack1lllllll1l1l_opy_, bstack111111111l1_opy_):
    try:
      bstack11111111l1l_opy_ = self.bstack111111ll11l_opy_()
      bstack1llllllll11l_opy_ = os.path.join(bstack11111111l1l_opy_, bstack1ll11_opy_ (u"ࠩࡳࡩࡷࡩࡹ࠯ࡼ࡬ࡴࠬὊ"))
      bstack11111111lll_opy_ = os.path.join(bstack11111111l1l_opy_, bstack111111111l1_opy_)
      if self.bstack1111111111l_opy_(bstack11111111l1l_opy_, bstack1lllllll1l1l_opy_): # if bstack1llllll1111l_opy_, bstack1lllll1l11l_opy_ bstack1llllll11l1l_opy_ is bstack1lllll1lllll_opy_ to bstack1111l1ll11l_opy_ version available (response 304)
        if os.path.exists(bstack11111111lll_opy_):
          self.logger.info(bstack1ll11_opy_ (u"ࠥࡔࡪࡸࡣࡺࠢࡥ࡭ࡳࡧࡲࡺࠢࡩࡳࡺࡴࡤࠡ࡫ࡱࠤࢀࢃࠬࠡࡵ࡮࡭ࡵࡶࡩ࡯ࡩࠣࡨࡴࡽ࡮࡭ࡱࡤࡨࠧὋ").format(bstack11111111lll_opy_))
          return bstack11111111lll_opy_
        if os.path.exists(bstack1llllllll11l_opy_):
          self.logger.info(bstack1ll11_opy_ (u"ࠦࡕ࡫ࡲࡤࡻࠣࡾ࡮ࡶࠠࡧࡱࡸࡲࡩࠦࡩ࡯ࠢࡾࢁ࠱ࠦࡵ࡯ࡼ࡬ࡴࡵ࡯࡮ࡨࠤὌ").format(bstack1llllllll11l_opy_))
          return self.bstack111111l11l1_opy_(bstack1llllllll11l_opy_, bstack111111111l1_opy_)
      self.logger.info(bstack1ll11_opy_ (u"ࠧࡊ࡯ࡸࡰ࡯ࡳࡦࡪࡩ࡯ࡩࠣࡴࡪࡸࡣࡺࠢࡥ࡭ࡳࡧࡲࡺࠢࡩࡶࡴࡳࠠࡼࡿࠥὍ").format(bstack1lllllll1l1l_opy_))
      response = bstack11ll1llll_opy_(bstack1ll11_opy_ (u"࠭ࡇࡆࡖࠪ὎"), bstack1lllllll1l1l_opy_, {}, {})
      if response.status_code == 200:
        bstack1lllll1ll111_opy_ = response.headers.get(bstack1ll11_opy_ (u"ࠢࡆࡖࡤ࡫ࠧ὏"), bstack1ll11_opy_ (u"ࠣࠤὐ"))
        if bstack1lllll1ll111_opy_:
          self.bstack1lllll1lll11_opy_(bstack11111111l1l_opy_, bstack1lllll1ll111_opy_)
        with open(bstack1llllllll11l_opy_, bstack1ll11_opy_ (u"ࠩࡺࡦࠬὑ")) as file:
          file.write(response.content)
        self.logger.info(bstack1ll11_opy_ (u"ࠥࡈࡴࡽ࡮࡭ࡱࡤࡨࡪࡪࠠࡱࡧࡵࡧࡾࠦࡢࡪࡰࡤࡶࡾࠦࡡ࡯ࡦࠣࡷࡦࡼࡥࡥࠢࡤࡸࠥࢁࡽࠣὒ").format(bstack1llllllll11l_opy_))
        return self.bstack111111l11l1_opy_(bstack1llllllll11l_opy_, bstack111111111l1_opy_)
      else:
        raise(bstack1ll11_opy_ (u"ࠦࡋࡧࡩ࡭ࡧࡧࠤࡹࡵࠠࡥࡱࡺࡲࡱࡵࡡࡥࠢࡷ࡬ࡪࠦࡦࡪ࡮ࡨ࠲࡙ࠥࡴࡢࡶࡸࡷࠥࡩ࡯ࡥࡧ࠽ࠤࢀࢃࠢὓ").format(response.status_code))
    except Exception as e:
      self.logger.error(bstack1ll11_opy_ (u"࡛ࠧ࡮ࡢࡤ࡯ࡩࠥࡺ࡯ࠡࡦࡲࡻࡳࡲ࡯ࡢࡦࠣࡴࡪࡸࡣࡺࠢࡥ࡭ࡳࡧࡲࡺ࠼ࠣࡿࢂࠨὔ").format(e))
  def bstack111111ll111_opy_(self, bstack1lllllll1l1l_opy_, bstack111111111l1_opy_):
    try:
      retry = 2
      bstack11111111lll_opy_ = None
      bstack1llllll111ll_opy_ = False
      while retry > 0:
        bstack11111111lll_opy_ = self.bstack111111l1lll_opy_(bstack1lllllll1l1l_opy_, bstack111111111l1_opy_)
        bstack1llllll111ll_opy_ = self.bstack1llllll1llll_opy_(bstack1lllllll1l1l_opy_, bstack111111111l1_opy_, bstack11111111lll_opy_)
        if bstack1llllll111ll_opy_:
          break
        retry -= 1
      return bstack11111111lll_opy_, bstack1llllll111ll_opy_
    except Exception as e:
      self.logger.error(bstack1ll11_opy_ (u"ࠨࡕ࡯ࡣࡥࡰࡪࠦࡴࡰࠢࡪࡩࡹࠦࡰࡦࡴࡦࡽࠥࡨࡩ࡯ࡣࡵࡽࠥࡶࡡࡵࡪࠥὕ").format(e))
    return bstack11111111lll_opy_, False
  def bstack1llllll1llll_opy_(self, bstack1lllllll1l1l_opy_, bstack111111111l1_opy_, bstack11111111lll_opy_, bstack1llllll11l11_opy_ = 0):
    if bstack1llllll11l11_opy_ > 1:
      return False
    if bstack11111111lll_opy_ == None or os.path.exists(bstack11111111lll_opy_) == False:
      self.logger.warn(bstack1ll11_opy_ (u"ࠢࡑࡧࡵࡧࡾࠦࡰࡢࡶ࡫ࠤࡳࡵࡴࠡࡨࡲࡹࡳࡪࠬࠡࡴࡨࡸࡷࡿࡩ࡯ࡩࠣࡨࡴࡽ࡮࡭ࡱࡤࡨࠧὖ"))
      return False
    bstack1lllllll111l_opy_ = bstack1ll11_opy_ (u"ࡳࠤࡡ࠲࠯ࡆࡰࡦࡴࡦࡽ࠴ࡩ࡬ࡪࠢ࡟ࡨ࠰ࡢ࠮࡝ࡦ࠮ࡠ࠳ࡢࡤࠬࠤὗ")
    command = bstack1ll11_opy_ (u"ࠩࡾࢁࠥ࠳࠭ࡷࡧࡵࡷ࡮ࡵ࡮ࠨ὘").format(bstack11111111lll_opy_)
    bstack111111l1l11_opy_ = subprocess.check_output(command, shell=True, text=True)
    if re.match(bstack1lllllll111l_opy_, bstack111111l1l11_opy_) != None:
      return True
    else:
      self.logger.error(bstack1ll11_opy_ (u"ࠥࡔࡪࡸࡣࡺࠢࡹࡩࡷࡹࡩࡰࡰࠣࡧ࡭࡫ࡣ࡬ࠢࡩࡥ࡮ࡲࡥࡥࠤὙ"))
      return False
  def bstack111111l11l1_opy_(self, bstack1llllllll11l_opy_, bstack111111111l1_opy_):
    try:
      working_dir = os.path.dirname(bstack1llllllll11l_opy_)
      shutil.unpack_archive(bstack1llllllll11l_opy_, working_dir)
      bstack11111111lll_opy_ = os.path.join(working_dir, bstack111111111l1_opy_)
      os.chmod(bstack11111111lll_opy_, 0o755)
      return bstack11111111lll_opy_
    except Exception as e:
      self.logger.error(bstack1ll11_opy_ (u"࡚ࠦࡴࡡࡣ࡮ࡨࠤࡹࡵࠠࡶࡰࡽ࡭ࡵࠦࡰࡦࡴࡦࡽࠥࡨࡩ࡯ࡣࡵࡽࠧ὚"))
  def bstack1lllllll11ll_opy_(self):
    try:
      bstack11111111111_opy_ = self.config.get(bstack1ll11_opy_ (u"ࠬࡶࡥࡳࡥࡼࠫὛ"))
      bstack1lllllll11ll_opy_ = bstack11111111111_opy_ or (bstack11111111111_opy_ is None and self.bstack1l1lllll11_opy_)
      if not bstack1lllllll11ll_opy_ or self.config.get(bstack1ll11_opy_ (u"࠭ࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࠩ὜"), None) not in bstack11l1l1l1l1l_opy_:
        return False
      self.bstack1l1ll111l_opy_ = True
      return True
    except Exception as e:
      self.logger.error(bstack1ll11_opy_ (u"ࠢࡖࡰࡤࡦࡱ࡫ࠠࡵࡱࠣࡨࡪࡺࡥࡤࡶࠣࡴࡪࡸࡣࡺ࠮ࠣࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡻࡾࠤὝ").format(e))
  def bstack1llllll1lll1_opy_(self):
    try:
      bstack1llllll1lll1_opy_ = self.percy_capture_mode
      return bstack1llllll1lll1_opy_
    except Exception as e:
      self.logger.error(bstack1ll11_opy_ (u"ࠣࡗࡱࡥࡧࡲࡥࠡࡶࡲࠤࡩ࡫ࡴࡦࡥࡷࠤࡵ࡫ࡲࡤࡻࠣࡧࡦࡶࡴࡶࡴࡨࠤࡲࡵࡤࡦ࠮ࠣࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡻࡾࠤ὞").format(e))
  def init(self, bstack1l1lllll11_opy_, config, logger):
    self.bstack1l1lllll11_opy_ = bstack1l1lllll11_opy_
    self.config = config
    self.logger = logger
    if not self.bstack1lllllll11ll_opy_():
      return
    self.bstack111111l1ll1_opy_ = config.get(bstack1ll11_opy_ (u"ࠩࡳࡩࡷࡩࡹࡐࡲࡷ࡭ࡴࡴࡳࠨὟ"), {})
    self.percy_capture_mode = config.get(bstack1ll11_opy_ (u"ࠪࡴࡪࡸࡣࡺࡅࡤࡴࡹࡻࡲࡦࡏࡲࡨࡪ࠭ὠ"))
    try:
      bstack1lllllll1l1l_opy_, bstack111111111l1_opy_ = self.bstack1llllllll1l1_opy_()
      self.bstack111l11lll1l_opy_ = bstack111111111l1_opy_
      bstack11111111lll_opy_, bstack1llllll111ll_opy_ = self.bstack111111ll111_opy_(bstack1lllllll1l1l_opy_, bstack111111111l1_opy_)
      if bstack1llllll111ll_opy_:
        self.binary_path = bstack11111111lll_opy_
        thread = Thread(target=self.bstack111111ll1l1_opy_)
        thread.start()
      else:
        self.bstack1lllllll1l11_opy_ = True
        self.logger.error(bstack1ll11_opy_ (u"ࠦࡎࡴࡶࡢ࡮࡬ࡨࠥࡶࡥࡳࡥࡼࠤࡵࡧࡴࡩࠢࡩࡳࡺࡴࡤࠡ࠯ࠣࡿࢂ࠲ࠠࡖࡰࡤࡦࡱ࡫ࠠࡵࡱࠣࡷࡹࡧࡲࡵࠢࡓࡩࡷࡩࡹࠣὡ").format(bstack11111111lll_opy_))
    except Exception as e:
      self.logger.error(bstack1ll11_opy_ (u"࡛ࠧ࡮ࡢࡤ࡯ࡩࠥࡺ࡯ࠡࡵࡷࡥࡷࡺࠠࡱࡧࡵࡧࡾ࠲ࠠࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣࡿࢂࠨὢ").format(e))
  def bstack1lllllll11l1_opy_(self):
    try:
      logfile = os.path.join(self.working_dir, bstack1ll11_opy_ (u"࠭࡬ࡰࡩࠪὣ"), bstack1ll11_opy_ (u"ࠧࡱࡧࡵࡧࡾ࠴࡬ࡰࡩࠪὤ"))
      os.makedirs(os.path.dirname(logfile)) if not os.path.exists(os.path.dirname(logfile)) else None
      self.logger.debug(bstack1ll11_opy_ (u"ࠣࡒࡸࡷ࡭࡯࡮ࡨࠢࡳࡩࡷࡩࡹࠡ࡮ࡲ࡫ࡸࠦࡡࡵࠢࡾࢁࠧὥ").format(logfile))
      self.bstack1llllll111l1_opy_ = logfile
    except Exception as e:
      self.logger.error(bstack1ll11_opy_ (u"ࠤࡘࡲࡦࡨ࡬ࡦࠢࡷࡳࠥࡹࡥࡵࠢࡳࡩࡷࡩࡹࠡ࡮ࡲ࡫ࠥࡶࡡࡵࡪ࠯ࠤࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡼࡿࠥὦ").format(e))
  @measure(event_name=EVENTS.bstack11l11llll11_opy_, stage=STAGE.bstack1111l1111_opy_)
  def bstack111111ll1l1_opy_(self):
    bstack1111111llll_opy_ = self.bstack1llllll1l11l_opy_()
    if bstack1111111llll_opy_ == None:
      self.bstack1lllllll1l11_opy_ = True
      self.logger.error(bstack1ll11_opy_ (u"ࠥࡔࡪࡸࡣࡺࠢࡷࡳࡰ࡫࡮ࠡࡰࡲࡸࠥ࡬࡯ࡶࡰࡧ࠰ࠥࡌࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡࡵࡷࡥࡷࡺࠠࡱࡧࡵࡧࡾࠨὧ"))
      return False
    bstack1111111ll1l_opy_ = [bstack1ll11_opy_ (u"ࠦࡦࡶࡰ࠻ࡧࡻࡩࡨࡀࡳࡵࡣࡵࡸࠧὨ") if self.bstack1l1lllll11_opy_ else bstack1ll11_opy_ (u"ࠬ࡫ࡸࡦࡥ࠽ࡷࡹࡧࡲࡵࠩὩ")]
    bstack11111ll1l1l_opy_ = self.bstack111111l1l1l_opy_()
    if bstack11111ll1l1l_opy_ != None:
      bstack1111111ll1l_opy_.append(bstack1ll11_opy_ (u"ࠨ࠭ࡤࠢࡾࢁࠧὪ").format(bstack11111ll1l1l_opy_))
    env = os.environ.copy()
    env[bstack1ll11_opy_ (u"ࠢࡑࡇࡕࡇ࡞ࡥࡔࡐࡍࡈࡒࠧὫ")] = bstack1111111llll_opy_
    env[bstack1ll11_opy_ (u"ࠣࡖࡋࡣࡇ࡛ࡉࡍࡆࡢ࡙࡚ࡏࡄࠣὬ")] = os.environ.get(bstack1ll11_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡎࡕࡃࡡࡘ࡙ࡎࡊࠧὭ"), bstack1ll11_opy_ (u"ࠪࠫὮ"))
    bstack1llllll1ll11_opy_ = [self.binary_path]
    self.bstack1lllllll11l1_opy_()
    self.bstack1lllllll1ll1_opy_ = self.bstack1llllll1l111_opy_(bstack1llllll1ll11_opy_ + bstack1111111ll1l_opy_, env)
    self.logger.debug(bstack1ll11_opy_ (u"ࠦࡘࡺࡡࡳࡶ࡬ࡲ࡬ࠦࡈࡦࡣ࡯ࡸ࡭ࠦࡃࡩࡧࡦ࡯ࠧὯ"))
    bstack1llllll11l11_opy_ = 0
    while self.bstack1lllllll1ll1_opy_.poll() == None:
      bstack1lllll1ll11l_opy_ = self.bstack111111111ll_opy_()
      if bstack1lllll1ll11l_opy_:
        self.logger.debug(bstack1ll11_opy_ (u"ࠧࡎࡥࡢ࡮ࡷ࡬ࠥࡉࡨࡦࡥ࡮ࠤࡸࡻࡣࡤࡧࡶࡷ࡫ࡻ࡬ࠣὰ"))
        self.bstack11111111ll1_opy_ = True
        return True
      bstack1llllll11l11_opy_ += 1
      self.logger.debug(bstack1ll11_opy_ (u"ࠨࡈࡦࡣ࡯ࡸ࡭ࠦࡃࡩࡧࡦ࡯ࠥࡘࡥࡵࡴࡼࠤ࠲ࠦࡻࡾࠤά").format(bstack1llllll11l11_opy_))
      time.sleep(2)
    self.logger.error(bstack1ll11_opy_ (u"ࠢࡇࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡷࡹࡧࡲࡵࠢࡳࡩࡷࡩࡹ࠭ࠢࡋࡩࡦࡲࡴࡩࠢࡆ࡬ࡪࡩ࡫ࠡࡈࡤ࡭ࡱ࡫ࡤࠡࡣࡩࡸࡪࡸࠠࡼࡿࠣࡥࡹࡺࡥ࡮ࡲࡷࡷࠧὲ").format(bstack1llllll11l11_opy_))
    self.bstack1lllllll1l11_opy_ = True
    return False
  def bstack111111111ll_opy_(self, bstack1llllll11l11_opy_ = 0):
    if bstack1llllll11l11_opy_ > 10:
      return False
    try:
      bstack111111l11ll_opy_ = os.environ.get(bstack1ll11_opy_ (u"ࠨࡒࡈࡖࡈ࡟࡟ࡔࡇࡕ࡚ࡊࡘ࡟ࡂࡆࡇࡖࡊ࡙ࡓࠨέ"), bstack1ll11_opy_ (u"ࠩ࡫ࡸࡹࡶ࠺࠰࠱࡯ࡳࡨࡧ࡬ࡩࡱࡶࡸ࠿࠻࠳࠴࠺ࠪὴ"))
      bstack1llllll11lll_opy_ = bstack111111l11ll_opy_ + bstack11l1l1l1111_opy_
      response = requests.get(bstack1llllll11lll_opy_)
      data = response.json()
      self.percy_build_id = data.get(bstack1ll11_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࠩή"), {}).get(bstack1ll11_opy_ (u"ࠫ࡮ࡪࠧὶ"), None)
      return True
    except:
      self.logger.debug(bstack1ll11_opy_ (u"ࠧࡋࡲࡳࡱࡵࠤࡴࡩࡣࡶࡴࡵࡩࡩࠦࡷࡩ࡫࡯ࡩࠥࡶࡲࡰࡥࡨࡷࡸ࡯࡮ࡨࠢ࡫ࡩࡦࡲࡴࡩࠢࡦ࡬ࡪࡩ࡫ࠡࡴࡨࡷࡵࡵ࡮ࡴࡧࠥί"))
      return False
  def bstack1llllll1l11l_opy_(self):
    bstack1lllllllll1l_opy_ = bstack1ll11_opy_ (u"࠭ࡡࡱࡲࠪὸ") if self.bstack1l1lllll11_opy_ else bstack1ll11_opy_ (u"ࠧࡢࡷࡷࡳࡲࡧࡴࡦࠩό")
    bstack1lllllllll11_opy_ = bstack1ll11_opy_ (u"ࠣࡷࡱࡨࡪ࡬ࡩ࡯ࡧࡧࠦὺ") if self.config.get(bstack1ll11_opy_ (u"ࠩࡳࡩࡷࡩࡹࠨύ")) is None else True
    bstack11ll11lll11_opy_ = bstack1ll11_opy_ (u"ࠥࡥࡵ࡯࠯ࡢࡲࡳࡣࡵ࡫ࡲࡤࡻ࠲࡫ࡪࡺ࡟ࡱࡴࡲ࡮ࡪࡩࡴࡠࡶࡲ࡯ࡪࡴ࠿࡯ࡣࡰࡩࡂࢁࡽࠧࡶࡼࡴࡪࡃࡻࡾࠨࡳࡩࡷࡩࡹ࠾ࡽࢀࠦὼ").format(self.config[bstack1ll11_opy_ (u"ࠫࡵࡸ࡯࡫ࡧࡦࡸࡓࡧ࡭ࡦࠩώ")], bstack1lllllllll1l_opy_, bstack1lllllllll11_opy_)
    if self.percy_capture_mode:
      bstack11ll11lll11_opy_ += bstack1ll11_opy_ (u"ࠧࠬࡰࡦࡴࡦࡽࡤࡩࡡࡱࡶࡸࡶࡪࡥ࡭ࡰࡦࡨࡁࢀࢃࠢ὾").format(self.percy_capture_mode)
    uri = bstack111lll1ll_opy_(bstack11ll11lll11_opy_)
    try:
      response = bstack11ll1llll_opy_(bstack1ll11_opy_ (u"࠭ࡇࡆࡖࠪ὿"), uri, {}, {bstack1ll11_opy_ (u"ࠧࡢࡷࡷ࡬ࠬᾀ"): (self.config[bstack1ll11_opy_ (u"ࠨࡷࡶࡩࡷࡔࡡ࡮ࡧࠪᾁ")], self.config[bstack1ll11_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴࡍࡨࡽࠬᾂ")])})
      if response.status_code == 200:
        data = response.json()
        self.bstack1l1ll111l_opy_ = data.get(bstack1ll11_opy_ (u"ࠪࡷࡺࡩࡣࡦࡵࡶࠫᾃ"))
        self.percy_capture_mode = data.get(bstack1ll11_opy_ (u"ࠫࡵ࡫ࡲࡤࡻࡢࡧࡦࡶࡴࡶࡴࡨࡣࡲࡵࡤࡦࠩᾄ"))
        os.environ[bstack1ll11_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡕࡋࡒࡄ࡛ࠪᾅ")] = str(self.bstack1l1ll111l_opy_)
        os.environ[bstack1ll11_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡖࡅࡓࡅ࡜ࡣࡈࡇࡐࡕࡗࡕࡉࡤࡓࡏࡅࡇࠪᾆ")] = str(self.percy_capture_mode)
        if bstack1lllllllll11_opy_ == bstack1ll11_opy_ (u"ࠢࡶࡰࡧࡩ࡫࡯࡮ࡦࡦࠥᾇ") and str(self.bstack1l1ll111l_opy_).lower() == bstack1ll11_opy_ (u"ࠣࡶࡵࡹࡪࠨᾈ"):
          self.bstack1lll111ll1_opy_ = True
        if bstack1ll11_opy_ (u"ࠤࡷࡳࡰ࡫࡮ࠣᾉ") in data:
          return data[bstack1ll11_opy_ (u"ࠥࡸࡴࡱࡥ࡯ࠤᾊ")]
        else:
          raise bstack1ll11_opy_ (u"࡙ࠫࡵ࡫ࡦࡰࠣࡒࡴࡺࠠࡇࡱࡸࡲࡩࠦ࠭ࠡࡽࢀࠫᾋ").format(data)
      else:
        raise bstack1ll11_opy_ (u"ࠧࡌࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡࡨࡨࡸࡨ࡮ࠠࡱࡧࡵࡧࡾࠦࡴࡰ࡭ࡨࡲ࠱ࠦࡒࡦࡵࡳࡳࡳࡹࡥࠡࡵࡷࡥࡹࡻࡳࠡ࠯ࠣࡿࢂ࠲ࠠࡓࡧࡶࡴࡴࡴࡳࡦࠢࡅࡳࡩࡿࠠ࠮ࠢࡾࢁࠧᾌ").format(response.status_code, response.json())
    except Exception as e:
      self.logger.error(bstack1ll11_opy_ (u"ࠨࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥࡩࡲࡦࡣࡷ࡭ࡳ࡭ࠠࡱࡧࡵࡧࡾࠦࡰࡳࡱ࡭ࡩࡨࡺࠢᾍ").format(e))
  def bstack111111l1l1l_opy_(self):
    bstack1lllll1ll1ll_opy_ = os.path.join(tempfile.gettempdir(), bstack1ll11_opy_ (u"ࠢࡱࡧࡵࡧࡾࡉ࡯࡯ࡨ࡬࡫࠳ࡰࡳࡰࡰࠥᾎ"))
    try:
      if bstack1ll11_opy_ (u"ࠨࡸࡨࡶࡸ࡯࡯࡯ࠩᾏ") not in self.bstack111111l1ll1_opy_:
        self.bstack111111l1ll1_opy_[bstack1ll11_opy_ (u"ࠩࡹࡩࡷࡹࡩࡰࡰࠪᾐ")] = 2
      with open(bstack1lllll1ll1ll_opy_, bstack1ll11_opy_ (u"ࠪࡻࠬᾑ")) as fp:
        json.dump(self.bstack111111l1ll1_opy_, fp)
      return bstack1lllll1ll1ll_opy_
    except Exception as e:
      self.logger.error(bstack1ll11_opy_ (u"࡚ࠦࡴࡡࡣ࡮ࡨࠤࡹࡵࠠࡤࡴࡨࡥࡹ࡫ࠠࡱࡧࡵࡧࡾࠦࡣࡰࡰࡩ࠰ࠥࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡࡽࢀࠦᾒ").format(e))
  def bstack1llllll1l111_opy_(self, cmd, env = os.environ.copy()):
    try:
      if self.bstack1111111l111_opy_ == bstack1ll11_opy_ (u"ࠬࡽࡩ࡯ࠩᾓ"):
        bstack1llllllll111_opy_ = [bstack1ll11_opy_ (u"࠭ࡣ࡮ࡦ࠱ࡩࡽ࡫ࠧᾔ"), bstack1ll11_opy_ (u"ࠧ࠰ࡥࠪᾕ")]
        cmd = bstack1llllllll111_opy_ + cmd
      cmd = bstack1ll11_opy_ (u"ࠨࠢࠪᾖ").join(cmd)
      self.logger.debug(bstack1ll11_opy_ (u"ࠤࡕࡹࡳࡴࡩ࡯ࡩࠣࡿࢂࠨᾗ").format(cmd))
      with open(self.bstack1llllll111l1_opy_, bstack1ll11_opy_ (u"ࠥࡥࠧᾘ")) as bstack1llllllllll1_opy_:
        process = subprocess.Popen(cmd, shell=True, stdout=bstack1llllllllll1_opy_, text=True, stderr=bstack1llllllllll1_opy_, env=env, universal_newlines=True)
      return process
    except Exception as e:
      self.bstack1lllllll1l11_opy_ = True
      self.logger.error(bstack1ll11_opy_ (u"ࠦࡋࡧࡩ࡭ࡧࡧࠤࡹࡵࠠࡴࡶࡤࡶࡹࠦࡰࡦࡴࡦࡽࠥࡽࡩࡵࡪࠣࡧࡲࡪࠠ࠮ࠢࡾࢁ࠱ࠦࡅࡹࡥࡨࡴࡹ࡯࡯࡯࠼ࠣࡿࢂࠨᾙ").format(cmd, e))
  def shutdown(self):
    try:
      if self.bstack11111111ll1_opy_:
        self.logger.info(bstack1ll11_opy_ (u"࡙ࠧࡴࡰࡲࡳ࡭ࡳ࡭ࠠࡑࡧࡵࡧࡾࠨᾚ"))
        cmd = [self.binary_path, bstack1ll11_opy_ (u"ࠨࡥࡹࡧࡦ࠾ࡸࡺ࡯ࡱࠤᾛ")]
        self.bstack1llllll1l111_opy_(cmd)
        self.bstack11111111ll1_opy_ = False
    except Exception as e:
      self.logger.error(bstack1ll11_opy_ (u"ࠢࡇࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡷࡹࡵࡰࠡࡵࡨࡷࡸ࡯࡯࡯ࠢࡺ࡭ࡹ࡮ࠠࡤࡱࡰࡱࡦࡴࡤࠡ࠯ࠣࡿࢂ࠲ࠠࡆࡺࡦࡩࡵࡺࡩࡰࡰ࠽ࠤࢀࢃࠢᾜ").format(cmd, e))
  def bstack1ll1l1l1ll_opy_(self):
    if not self.bstack1l1ll111l_opy_:
      return
    try:
      bstack1lllllll1lll_opy_ = 0
      while not self.bstack11111111ll1_opy_ and bstack1lllllll1lll_opy_ < self.bstack1111111lll1_opy_:
        if self.bstack1lllllll1l11_opy_:
          self.logger.info(bstack1ll11_opy_ (u"ࠣࡒࡨࡶࡨࡿࠠࡴࡧࡷࡹࡵࠦࡦࡢ࡫࡯ࡩࡩࠨᾝ"))
          return
        time.sleep(1)
        bstack1lllllll1lll_opy_ += 1
      os.environ[bstack1ll11_opy_ (u"ࠩࡓࡉࡗࡉ࡙ࡠࡄࡈࡗ࡙ࡥࡐࡍࡃࡗࡊࡔࡘࡍࠨᾞ")] = str(self.bstack1111111ll11_opy_())
      self.logger.info(bstack1ll11_opy_ (u"ࠥࡔࡪࡸࡣࡺࠢࡶࡩࡹࡻࡰࠡࡥࡲࡱࡵࡲࡥࡵࡧࡧࠦᾟ"))
    except Exception as e:
      self.logger.error(bstack1ll11_opy_ (u"࡚ࠦࡴࡡࡣ࡮ࡨࠤࡹࡵࠠࡴࡧࡷࡹࡵࠦࡰࡦࡴࡦࡽ࠱ࠦࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢࡾࢁࠧᾠ").format(e))
  def bstack1111111ll11_opy_(self):
    if self.bstack1l1lllll11_opy_:
      return
    try:
      bstack1llllll1l1l1_opy_ = [platform[bstack1ll11_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡔࡡ࡮ࡧࠪᾡ")].lower() for platform in self.config.get(bstack1ll11_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩᾢ"), [])]
      bstack1111111l11l_opy_ = sys.maxsize
      bstack1111111l1ll_opy_ = bstack1ll11_opy_ (u"ࠧࠨᾣ")
      for browser in bstack1llllll1l1l1_opy_:
        if browser in self.bstack1lllll1ll1l1_opy_:
          bstack11111111l11_opy_ = self.bstack1lllll1ll1l1_opy_[browser]
        if bstack11111111l11_opy_ < bstack1111111l11l_opy_:
          bstack1111111l11l_opy_ = bstack11111111l11_opy_
          bstack1111111l1ll_opy_ = browser
      return bstack1111111l1ll_opy_
    except Exception as e:
      self.logger.error(bstack1ll11_opy_ (u"ࠣࡗࡱࡥࡧࡲࡥࠡࡶࡲࠤ࡫࡯࡮ࡥࠢࡥࡩࡸࡺࠠࡱ࡮ࡤࡸ࡫ࡵࡲ࡮࠮ࠣࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡻࡾࠤᾤ").format(e))
  @classmethod
  def bstack1l1l1llll_opy_(self):
    return os.getenv(bstack1ll11_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡒࡈࡖࡈ࡟ࠧᾥ"), bstack1ll11_opy_ (u"ࠪࡊࡦࡲࡳࡦࠩᾦ")).lower()
  @classmethod
  def bstack11l1111l1l_opy_(self):
    return os.getenv(bstack1ll11_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡔࡊࡘࡃ࡚ࡡࡆࡅࡕ࡚ࡕࡓࡇࡢࡑࡔࡊࡅࠨᾧ"), bstack1ll11_opy_ (u"ࠬ࠭ᾨ"))
  @classmethod
  def bstack11lllllll1l_opy_(cls, value):
    cls.bstack1lll111ll1_opy_ = value
  @classmethod
  def bstack1llllll1l1ll_opy_(cls):
    return cls.bstack1lll111ll1_opy_
  @classmethod
  def bstack1l1111111l1_opy_(cls, value):
    cls.percy_build_id = value
  @classmethod
  def bstack1lllll1llll1_opy_(cls):
    return cls.percy_build_id