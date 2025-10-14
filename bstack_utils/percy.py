# coding: UTF-8
import sys
bstack1_opy_ = sys.version_info [0] == 2
bstack11l1ll1_opy_ = 2048
bstack1l1l1ll_opy_ = 7
def bstack11l1l11_opy_ (bstack111l1ll_opy_):
    global bstack1l1lll1_opy_
    bstack1l1l11_opy_ = ord (bstack111l1ll_opy_ [-1])
    bstack111l1l1_opy_ = bstack111l1ll_opy_ [:-1]
    bstack111ll_opy_ = bstack1l1l11_opy_ % len (bstack111l1l1_opy_)
    bstack11l11l1_opy_ = bstack111l1l1_opy_ [:bstack111ll_opy_] + bstack111l1l1_opy_ [bstack111ll_opy_:]
    if bstack1_opy_:
        bstack1111l1l_opy_ = unicode () .join ([unichr (ord (char) - bstack11l1ll1_opy_ - (bstack1l111ll_opy_ + bstack1l1l11_opy_) % bstack1l1l1ll_opy_) for bstack1l111ll_opy_, char in enumerate (bstack11l11l1_opy_)])
    else:
        bstack1111l1l_opy_ = str () .join ([chr (ord (char) - bstack11l1ll1_opy_ - (bstack1l111ll_opy_ + bstack1l1l11_opy_) % bstack1l1l1ll_opy_) for bstack1l111ll_opy_, char in enumerate (bstack11l11l1_opy_)])
    return eval (bstack1111l1l_opy_)
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
from bstack_utils.helper import bstack11lll1llll_opy_
from bstack_utils.measure import measure
from bstack_utils.bstack1lll11l1l1_opy_ import bstack1l11l1l1ll_opy_
class bstack11ll1lll1l_opy_:
  working_dir = os.getcwd()
  bstack1ll1l1lll_opy_ = False
  config = {}
  bstack1111lll1lll_opy_ = bstack11l1l11_opy_ (u"ࠨࠩ἟")
  binary_path = bstack11l1l11_opy_ (u"ࠩࠪἠ")
  bstack1lllllll1lll_opy_ = bstack11l1l11_opy_ (u"ࠪࠫἡ")
  bstack1l1l1l1l1l_opy_ = False
  bstack111111ll11l_opy_ = None
  bstack1lllll1ll11l_opy_ = {}
  bstack1llllll1lll1_opy_ = 300
  bstack111111111ll_opy_ = False
  logger = None
  bstack1llllll1l1ll_opy_ = False
  bstack1l11lll11_opy_ = False
  percy_build_id = None
  bstack1lllll1ll111_opy_ = bstack11l1l11_opy_ (u"ࠫࠬἢ")
  bstack1lllllll1l11_opy_ = {
    bstack11l1l11_opy_ (u"ࠬࡩࡨࡳࡱࡰࡩࠬἣ") : 1,
    bstack11l1l11_opy_ (u"࠭ࡦࡪࡴࡨࡪࡴࡾࠧἤ") : 2,
    bstack11l1l11_opy_ (u"ࠧࡦࡦࡪࡩࠬἥ") : 3,
    bstack11l1l11_opy_ (u"ࠨࡵࡤࡪࡦࡸࡩࠨἦ") : 4
  }
  def __init__(self) -> None: pass
  def bstack111111l11ll_opy_(self):
    bstack1111111111l_opy_ = bstack11l1l11_opy_ (u"ࠩࠪἧ")
    bstack1lllllll11ll_opy_ = sys.platform
    bstack111111l1l11_opy_ = bstack11l1l11_opy_ (u"ࠪࡴࡪࡸࡣࡺࠩἨ")
    if re.match(bstack11l1l11_opy_ (u"ࠦࡩࡧࡲࡸ࡫ࡱࢀࡲࡧࡣࠡࡱࡶࠦἩ"), bstack1lllllll11ll_opy_) != None:
      bstack1111111111l_opy_ = bstack11l1l1l1l1l_opy_ + bstack11l1l11_opy_ (u"ࠧ࠵ࡰࡦࡴࡦࡽ࠲ࡵࡳࡹ࠰ࡽ࡭ࡵࠨἪ")
      self.bstack1lllll1ll111_opy_ = bstack11l1l11_opy_ (u"࠭࡭ࡢࡥࠪἫ")
    elif re.match(bstack11l1l11_opy_ (u"ࠢ࡮ࡵࡺ࡭ࡳࢂ࡭ࡴࡻࡶࢀࡲ࡯࡮ࡨࡹࡿࡧࡾ࡭ࡷࡪࡰࡿࡦࡨࡩࡷࡪࡰࡿࡻ࡮ࡴࡣࡦࡾࡨࡱࡨࢂࡷࡪࡰ࠶࠶ࠧἬ"), bstack1lllllll11ll_opy_) != None:
      bstack1111111111l_opy_ = bstack11l1l1l1l1l_opy_ + bstack11l1l11_opy_ (u"ࠣ࠱ࡳࡩࡷࡩࡹ࠮ࡹ࡬ࡲ࠳ࢀࡩࡱࠤἭ")
      bstack111111l1l11_opy_ = bstack11l1l11_opy_ (u"ࠤࡳࡩࡷࡩࡹ࠯ࡧࡻࡩࠧἮ")
      self.bstack1lllll1ll111_opy_ = bstack11l1l11_opy_ (u"ࠪࡻ࡮ࡴࠧἯ")
    else:
      bstack1111111111l_opy_ = bstack11l1l1l1l1l_opy_ + bstack11l1l11_opy_ (u"ࠦ࠴ࡶࡥࡳࡥࡼ࠱ࡱ࡯࡮ࡶࡺ࠱ࡾ࡮ࡶࠢἰ")
      self.bstack1lllll1ll111_opy_ = bstack11l1l11_opy_ (u"ࠬࡲࡩ࡯ࡷࡻࠫἱ")
    return bstack1111111111l_opy_, bstack111111l1l11_opy_
  def bstack1llllll1ll1l_opy_(self):
    try:
      bstack1lllllll1ll1_opy_ = [os.path.join(expanduser(bstack11l1l11_opy_ (u"ࠨࡾࠣἲ")), bstack11l1l11_opy_ (u"ࠧ࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠧἳ")), self.working_dir, tempfile.gettempdir()]
      for path in bstack1lllllll1ll1_opy_:
        if(self.bstack1lllllll111l_opy_(path)):
          return path
      raise bstack11l1l11_opy_ (u"ࠣࡗࡱࡥࡧࡲࡥࠡࡶࡲࠤࡩࡵࡷ࡯࡮ࡲࡥࡩࠦࡰࡦࡴࡦࡽࠥࡨࡩ࡯ࡣࡵࡽࠧἴ")
    except Exception as e:
      self.logger.error(bstack11l1l11_opy_ (u"ࠤࡉࡥ࡮ࡲࡥࡥࠢࡷࡳࠥ࡬ࡩ࡯ࡦࠣࡥࡻࡧࡩ࡭ࡣࡥࡰࡪࠦࡰࡢࡶ࡫ࠤ࡫ࡵࡲࠡࡲࡨࡶࡨࡿࠠࡥࡱࡺࡲࡱࡵࡡࡥ࠮ࠣࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦ࠭ࠡࡽࢀࠦἵ").format(e))
  def bstack1lllllll111l_opy_(self, path):
    try:
      if not os.path.exists(path):
        os.makedirs(path)
      return True
    except:
      return False
  def bstack1llllll11l1l_opy_(self, bstack1llllllll111_opy_):
    return os.path.join(bstack1llllllll111_opy_, self.bstack1111lll1lll_opy_ + bstack11l1l11_opy_ (u"ࠥ࠲ࡪࡺࡡࡨࠤἶ"))
  def bstack1lllll1lll11_opy_(self, bstack1llllllll111_opy_, bstack1111111l1ll_opy_):
    if not bstack1111111l1ll_opy_: return
    try:
      bstack11111111l1l_opy_ = self.bstack1llllll11l1l_opy_(bstack1llllllll111_opy_)
      with open(bstack11111111l1l_opy_, bstack11l1l11_opy_ (u"ࠦࡼࠨἷ")) as f:
        f.write(bstack1111111l1ll_opy_)
        self.logger.debug(bstack11l1l11_opy_ (u"࡙ࠧࡡࡷࡧࡧࠤࡳ࡫ࡷࠡࡇࡗࡥ࡬ࠦࡦࡰࡴࠣࡴࡪࡸࡣࡺࠤἸ"))
    except Exception as e:
      self.logger.error(bstack11l1l11_opy_ (u"ࠨࡕ࡯ࡣࡥࡰࡪࠦࡴࡰࠢࡶࡥࡻ࡫ࠠࡵࡪࡨࠤࡪࡺࡡࡨ࠮ࠣࡩࡷࡸ࡯ࡳ࠼ࠣࡿࢂࠨἹ").format(e))
  def bstack1111111ll11_opy_(self, bstack1llllllll111_opy_):
    try:
      bstack11111111l1l_opy_ = self.bstack1llllll11l1l_opy_(bstack1llllllll111_opy_)
      if os.path.exists(bstack11111111l1l_opy_):
        with open(bstack11111111l1l_opy_, bstack11l1l11_opy_ (u"ࠢࡳࠤἺ")) as f:
          bstack1111111l1ll_opy_ = f.read().strip()
          return bstack1111111l1ll_opy_ if bstack1111111l1ll_opy_ else None
    except Exception as e:
      self.logger.error(bstack11l1l11_opy_ (u"ࠣࡈࡤ࡭ࡱ࡫ࡤࠡ࡮ࡲࡥࡩ࡯࡮ࡨࠢࡈࡘࡦ࡭ࠬࠡࡧࡵࡶࡴࡸ࠺ࠡࡽࢀࠦἻ").format(e))
  def bstack1lllll1llll1_opy_(self, bstack1llllllll111_opy_, bstack1111111111l_opy_):
    bstack1llllll11l11_opy_ = self.bstack1111111ll11_opy_(bstack1llllllll111_opy_)
    if bstack1llllll11l11_opy_:
      try:
        bstack111111l1lll_opy_ = self.bstack11111111l11_opy_(bstack1llllll11l11_opy_, bstack1111111111l_opy_)
        if not bstack111111l1lll_opy_:
          self.logger.debug(bstack11l1l11_opy_ (u"ࠤࡓࡩࡷࡩࡹࠡࡤ࡬ࡲࡦࡸࡹࠡ࡫ࡶࠤࡺࡶࠠࡵࡱࠣࡨࡦࡺࡥࠡࠪࡈࡘࡦ࡭ࠠࡶࡰࡦ࡬ࡦࡴࡧࡦࡦࠬࠦἼ"))
          return True
        self.logger.debug(bstack11l1l11_opy_ (u"ࠥࡒࡪࡽࠠࡑࡧࡵࡧࡾࠦࡢࡪࡰࡤࡶࡾࠦࡶࡦࡴࡶ࡭ࡴࡴࠠࡢࡸࡤ࡭ࡱࡧࡢ࡭ࡧ࠯ࠤࡩࡵࡷ࡯࡮ࡲࡥࡩ࡯࡮ࡨࠢࡸࡴࡩࡧࡴࡦࠤἽ"))
        return False
      except Exception as e:
        self.logger.warn(bstack11l1l11_opy_ (u"ࠦࡋࡧࡩ࡭ࡧࡧࠤࡹࡵࠠࡤࡪࡨࡧࡰࠦࡦࡰࡴࠣࡦ࡮ࡴࡡࡳࡻࠣࡹࡵࡪࡡࡵࡧࡶ࠰ࠥࡻࡳࡪࡰࡪࠤࡪࡾࡩࡴࡶ࡬ࡲ࡬ࠦࡢࡪࡰࡤࡶࡾࡀࠠࡼࡿࠥἾ").format(e))
    return False
  def bstack11111111l11_opy_(self, bstack1llllll11l11_opy_, bstack1111111111l_opy_):
    try:
      headers = {
        bstack11l1l11_opy_ (u"ࠧࡏࡦ࠮ࡐࡲࡲࡪ࠳ࡍࡢࡶࡦ࡬ࠧἿ"): bstack1llllll11l11_opy_
      }
      response = bstack11lll1llll_opy_(bstack11l1l11_opy_ (u"࠭ࡇࡆࡖࠪὀ"), bstack1111111111l_opy_, {}, {bstack11l1l11_opy_ (u"ࠢࡩࡧࡤࡨࡪࡸࡳࠣὁ"): headers})
      if response.status_code == 304:
        return False
      return True
    except Exception as e:
      raise(bstack11l1l11_opy_ (u"ࠣࡇࡵࡶࡴࡸࠠࡤࡪࡨࡧࡰ࡯࡮ࡨࠢࡩࡳࡷࠦࡐࡦࡴࡦࡽࠥࡨࡩ࡯ࡣࡵࡽࠥࡻࡰࡥࡣࡷࡩࡸࡀࠠࡼࡿࠥὂ").format(e))
  @measure(event_name=EVENTS.bstack11l1l111111_opy_, stage=STAGE.bstack11l1lllll_opy_)
  def bstack1lllll1lllll_opy_(self, bstack1111111111l_opy_, bstack111111l1l11_opy_):
    try:
      bstack1lllllll11l1_opy_ = self.bstack1llllll1ll1l_opy_()
      bstack1lllllllll11_opy_ = os.path.join(bstack1lllllll11l1_opy_, bstack11l1l11_opy_ (u"ࠩࡳࡩࡷࡩࡹ࠯ࡼ࡬ࡴࠬὃ"))
      bstack1llllll1l11l_opy_ = os.path.join(bstack1lllllll11l1_opy_, bstack111111l1l11_opy_)
      if self.bstack1lllll1llll1_opy_(bstack1lllllll11l1_opy_, bstack1111111111l_opy_): # if bstack1lllllllllll_opy_, bstack1lllll1ll11_opy_ bstack1111111l1ll_opy_ is bstack1llllll1llll_opy_ to bstack1111l1l111l_opy_ version available (response 304)
        if os.path.exists(bstack1llllll1l11l_opy_):
          self.logger.info(bstack11l1l11_opy_ (u"ࠥࡔࡪࡸࡣࡺࠢࡥ࡭ࡳࡧࡲࡺࠢࡩࡳࡺࡴࡤࠡ࡫ࡱࠤࢀࢃࠬࠡࡵ࡮࡭ࡵࡶࡩ࡯ࡩࠣࡨࡴࡽ࡮࡭ࡱࡤࡨࠧὄ").format(bstack1llllll1l11l_opy_))
          return bstack1llllll1l11l_opy_
        if os.path.exists(bstack1lllllllll11_opy_):
          self.logger.info(bstack11l1l11_opy_ (u"ࠦࡕ࡫ࡲࡤࡻࠣࡾ࡮ࡶࠠࡧࡱࡸࡲࡩࠦࡩ࡯ࠢࡾࢁ࠱ࠦࡵ࡯ࡼ࡬ࡴࡵ࡯࡮ࡨࠤὅ").format(bstack1lllllllll11_opy_))
          return self.bstack1llllllll1ll_opy_(bstack1lllllllll11_opy_, bstack111111l1l11_opy_)
      self.logger.info(bstack11l1l11_opy_ (u"ࠧࡊ࡯ࡸࡰ࡯ࡳࡦࡪࡩ࡯ࡩࠣࡴࡪࡸࡣࡺࠢࡥ࡭ࡳࡧࡲࡺࠢࡩࡶࡴࡳࠠࡼࡿࠥ὆").format(bstack1111111111l_opy_))
      response = bstack11lll1llll_opy_(bstack11l1l11_opy_ (u"࠭ࡇࡆࡖࠪ὇"), bstack1111111111l_opy_, {}, {})
      if response.status_code == 200:
        bstack11111111111_opy_ = response.headers.get(bstack11l1l11_opy_ (u"ࠢࡆࡖࡤ࡫ࠧὈ"), bstack11l1l11_opy_ (u"ࠣࠤὉ"))
        if bstack11111111111_opy_:
          self.bstack1lllll1lll11_opy_(bstack1lllllll11l1_opy_, bstack11111111111_opy_)
        with open(bstack1lllllllll11_opy_, bstack11l1l11_opy_ (u"ࠩࡺࡦࠬὊ")) as file:
          file.write(response.content)
        self.logger.info(bstack11l1l11_opy_ (u"ࠥࡈࡴࡽ࡮࡭ࡱࡤࡨࡪࡪࠠࡱࡧࡵࡧࡾࠦࡢࡪࡰࡤࡶࡾࠦࡡ࡯ࡦࠣࡷࡦࡼࡥࡥࠢࡤࡸࠥࢁࡽࠣὋ").format(bstack1lllllllll11_opy_))
        return self.bstack1llllllll1ll_opy_(bstack1lllllllll11_opy_, bstack111111l1l11_opy_)
      else:
        raise(bstack11l1l11_opy_ (u"ࠦࡋࡧࡩ࡭ࡧࡧࠤࡹࡵࠠࡥࡱࡺࡲࡱࡵࡡࡥࠢࡷ࡬ࡪࠦࡦࡪ࡮ࡨ࠲࡙ࠥࡴࡢࡶࡸࡷࠥࡩ࡯ࡥࡧ࠽ࠤࢀࢃࠢὌ").format(response.status_code))
    except Exception as e:
      self.logger.error(bstack11l1l11_opy_ (u"࡛ࠧ࡮ࡢࡤ࡯ࡩࠥࡺ࡯ࠡࡦࡲࡻࡳࡲ࡯ࡢࡦࠣࡴࡪࡸࡣࡺࠢࡥ࡭ࡳࡧࡲࡺ࠼ࠣࡿࢂࠨὍ").format(e))
  def bstack1111111l11l_opy_(self, bstack1111111111l_opy_, bstack111111l1l11_opy_):
    try:
      retry = 2
      bstack1llllll1l11l_opy_ = None
      bstack1llllll11111_opy_ = False
      while retry > 0:
        bstack1llllll1l11l_opy_ = self.bstack1lllll1lllll_opy_(bstack1111111111l_opy_, bstack111111l1l11_opy_)
        bstack1llllll11111_opy_ = self.bstack1lllll1lll1l_opy_(bstack1111111111l_opy_, bstack111111l1l11_opy_, bstack1llllll1l11l_opy_)
        if bstack1llllll11111_opy_:
          break
        retry -= 1
      return bstack1llllll1l11l_opy_, bstack1llllll11111_opy_
    except Exception as e:
      self.logger.error(bstack11l1l11_opy_ (u"ࠨࡕ࡯ࡣࡥࡰࡪࠦࡴࡰࠢࡪࡩࡹࠦࡰࡦࡴࡦࡽࠥࡨࡩ࡯ࡣࡵࡽࠥࡶࡡࡵࡪࠥ὎").format(e))
    return bstack1llllll1l11l_opy_, False
  def bstack1lllll1lll1l_opy_(self, bstack1111111111l_opy_, bstack111111l1l11_opy_, bstack1llllll1l11l_opy_, bstack111111l1ll1_opy_ = 0):
    if bstack111111l1ll1_opy_ > 1:
      return False
    if bstack1llllll1l11l_opy_ == None or os.path.exists(bstack1llllll1l11l_opy_) == False:
      self.logger.warn(bstack11l1l11_opy_ (u"ࠢࡑࡧࡵࡧࡾࠦࡰࡢࡶ࡫ࠤࡳࡵࡴࠡࡨࡲࡹࡳࡪࠬࠡࡴࡨࡸࡷࡿࡩ࡯ࡩࠣࡨࡴࡽ࡮࡭ࡱࡤࡨࠧ὏"))
      return False
    bstack11111111lll_opy_ = bstack11l1l11_opy_ (u"ࡳࠤࡡ࠲࠯ࡆࡰࡦࡴࡦࡽ࠴ࡩ࡬ࡪࠢ࡟ࡨ࠰ࡢ࠮࡝ࡦ࠮ࡠ࠳ࡢࡤࠬࠤὐ")
    command = bstack11l1l11_opy_ (u"ࠩࡾࢁࠥ࠳࠭ࡷࡧࡵࡷ࡮ࡵ࡮ࠨὑ").format(bstack1llllll1l11l_opy_)
    bstack111111ll111_opy_ = subprocess.check_output(command, shell=True, text=True)
    if re.match(bstack11111111lll_opy_, bstack111111ll111_opy_) != None:
      return True
    else:
      self.logger.error(bstack11l1l11_opy_ (u"ࠥࡔࡪࡸࡣࡺࠢࡹࡩࡷࡹࡩࡰࡰࠣࡧ࡭࡫ࡣ࡬ࠢࡩࡥ࡮ࡲࡥࡥࠤὒ"))
      return False
  def bstack1llllllll1ll_opy_(self, bstack1lllllllll11_opy_, bstack111111l1l11_opy_):
    try:
      working_dir = os.path.dirname(bstack1lllllllll11_opy_)
      shutil.unpack_archive(bstack1lllllllll11_opy_, working_dir)
      bstack1llllll1l11l_opy_ = os.path.join(working_dir, bstack111111l1l11_opy_)
      os.chmod(bstack1llllll1l11l_opy_, 0o755)
      return bstack1llllll1l11l_opy_
    except Exception as e:
      self.logger.error(bstack11l1l11_opy_ (u"࡚ࠦࡴࡡࡣ࡮ࡨࠤࡹࡵࠠࡶࡰࡽ࡭ࡵࠦࡰࡦࡴࡦࡽࠥࡨࡩ࡯ࡣࡵࡽࠧὓ"))
  def bstack111111l11l1_opy_(self):
    try:
      bstack111111111l1_opy_ = self.config.get(bstack11l1l11_opy_ (u"ࠬࡶࡥࡳࡥࡼࠫὔ"))
      bstack111111l11l1_opy_ = bstack111111111l1_opy_ or (bstack111111111l1_opy_ is None and self.bstack1ll1l1lll_opy_)
      if not bstack111111l11l1_opy_ or self.config.get(bstack11l1l11_opy_ (u"࠭ࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࠩὕ"), None) not in bstack11l1l1l11ll_opy_:
        return False
      self.bstack1l1l1l1l1l_opy_ = True
      return True
    except Exception as e:
      self.logger.error(bstack11l1l11_opy_ (u"ࠢࡖࡰࡤࡦࡱ࡫ࠠࡵࡱࠣࡨࡪࡺࡥࡤࡶࠣࡴࡪࡸࡣࡺ࠮ࠣࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡻࡾࠤὖ").format(e))
  def bstack1lllllll1111_opy_(self):
    try:
      bstack1lllllll1111_opy_ = self.percy_capture_mode
      return bstack1lllllll1111_opy_
    except Exception as e:
      self.logger.error(bstack11l1l11_opy_ (u"ࠣࡗࡱࡥࡧࡲࡥࠡࡶࡲࠤࡩ࡫ࡴࡦࡥࡷࠤࡵ࡫ࡲࡤࡻࠣࡧࡦࡶࡴࡶࡴࡨࠤࡲࡵࡤࡦ࠮ࠣࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡻࡾࠤὗ").format(e))
  def init(self, bstack1ll1l1lll_opy_, config, logger):
    self.bstack1ll1l1lll_opy_ = bstack1ll1l1lll_opy_
    self.config = config
    self.logger = logger
    if not self.bstack111111l11l1_opy_():
      return
    self.bstack1lllll1ll11l_opy_ = config.get(bstack11l1l11_opy_ (u"ࠩࡳࡩࡷࡩࡹࡐࡲࡷ࡭ࡴࡴࡳࠨ὘"), {})
    self.percy_capture_mode = config.get(bstack11l1l11_opy_ (u"ࠪࡴࡪࡸࡣࡺࡅࡤࡴࡹࡻࡲࡦࡏࡲࡨࡪ࠭Ὑ"))
    try:
      bstack1111111111l_opy_, bstack111111l1l11_opy_ = self.bstack111111l11ll_opy_()
      self.bstack1111lll1lll_opy_ = bstack111111l1l11_opy_
      bstack1llllll1l11l_opy_, bstack1llllll11111_opy_ = self.bstack1111111l11l_opy_(bstack1111111111l_opy_, bstack111111l1l11_opy_)
      if bstack1llllll11111_opy_:
        self.binary_path = bstack1llllll1l11l_opy_
        thread = Thread(target=self.bstack1llllllll1l1_opy_)
        thread.start()
      else:
        self.bstack1llllll1l1ll_opy_ = True
        self.logger.error(bstack11l1l11_opy_ (u"ࠦࡎࡴࡶࡢ࡮࡬ࡨࠥࡶࡥࡳࡥࡼࠤࡵࡧࡴࡩࠢࡩࡳࡺࡴࡤࠡ࠯ࠣࡿࢂ࠲ࠠࡖࡰࡤࡦࡱ࡫ࠠࡵࡱࠣࡷࡹࡧࡲࡵࠢࡓࡩࡷࡩࡹࠣ὚").format(bstack1llllll1l11l_opy_))
    except Exception as e:
      self.logger.error(bstack11l1l11_opy_ (u"࡛ࠧ࡮ࡢࡤ࡯ࡩࠥࡺ࡯ࠡࡵࡷࡥࡷࡺࠠࡱࡧࡵࡧࡾ࠲ࠠࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣࡿࢂࠨὛ").format(e))
  def bstack1lllll1l1lll_opy_(self):
    try:
      logfile = os.path.join(self.working_dir, bstack11l1l11_opy_ (u"࠭࡬ࡰࡩࠪ὜"), bstack11l1l11_opy_ (u"ࠧࡱࡧࡵࡧࡾ࠴࡬ࡰࡩࠪὝ"))
      os.makedirs(os.path.dirname(logfile)) if not os.path.exists(os.path.dirname(logfile)) else None
      self.logger.debug(bstack11l1l11_opy_ (u"ࠣࡒࡸࡷ࡭࡯࡮ࡨࠢࡳࡩࡷࡩࡹࠡ࡮ࡲ࡫ࡸࠦࡡࡵࠢࡾࢁࠧ὞").format(logfile))
      self.bstack1lllllll1lll_opy_ = logfile
    except Exception as e:
      self.logger.error(bstack11l1l11_opy_ (u"ࠤࡘࡲࡦࡨ࡬ࡦࠢࡷࡳࠥࡹࡥࡵࠢࡳࡩࡷࡩࡹࠡ࡮ࡲ࡫ࠥࡶࡡࡵࡪ࠯ࠤࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡼࡿࠥὟ").format(e))
  @measure(event_name=EVENTS.bstack11l1l1ll111_opy_, stage=STAGE.bstack11l1lllll_opy_)
  def bstack1llllllll1l1_opy_(self):
    bstack111111l111l_opy_ = self.bstack1lllllll1l1l_opy_()
    if bstack111111l111l_opy_ == None:
      self.bstack1llllll1l1ll_opy_ = True
      self.logger.error(bstack11l1l11_opy_ (u"ࠥࡔࡪࡸࡣࡺࠢࡷࡳࡰ࡫࡮ࠡࡰࡲࡸࠥ࡬࡯ࡶࡰࡧ࠰ࠥࡌࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡࡵࡷࡥࡷࡺࠠࡱࡧࡵࡧࡾࠨὠ"))
      return False
    bstack11111111ll1_opy_ = [bstack11l1l11_opy_ (u"ࠦࡦࡶࡰ࠻ࡧࡻࡩࡨࡀࡳࡵࡣࡵࡸࠧὡ") if self.bstack1ll1l1lll_opy_ else bstack11l1l11_opy_ (u"ࠬ࡫ࡸࡦࡥ࠽ࡷࡹࡧࡲࡵࠩὢ")]
    bstack11111lll1ll_opy_ = self.bstack111111l1l1l_opy_()
    if bstack11111lll1ll_opy_ != None:
      bstack11111111ll1_opy_.append(bstack11l1l11_opy_ (u"ࠨ࠭ࡤࠢࡾࢁࠧὣ").format(bstack11111lll1ll_opy_))
    env = os.environ.copy()
    env[bstack11l1l11_opy_ (u"ࠢࡑࡇࡕࡇ࡞ࡥࡔࡐࡍࡈࡒࠧὤ")] = bstack111111l111l_opy_
    env[bstack11l1l11_opy_ (u"ࠣࡖࡋࡣࡇ࡛ࡉࡍࡆࡢ࡙࡚ࡏࡄࠣὥ")] = os.environ.get(bstack11l1l11_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡎࡕࡃࡡࡘ࡙ࡎࡊࠧὦ"), bstack11l1l11_opy_ (u"ࠪࠫὧ"))
    bstack1llllll11lll_opy_ = [self.binary_path]
    self.bstack1lllll1l1lll_opy_()
    self.bstack111111ll11l_opy_ = self.bstack111111l1111_opy_(bstack1llllll11lll_opy_ + bstack11111111ll1_opy_, env)
    self.logger.debug(bstack11l1l11_opy_ (u"ࠦࡘࡺࡡࡳࡶ࡬ࡲ࡬ࠦࡈࡦࡣ࡯ࡸ࡭ࠦࡃࡩࡧࡦ࡯ࠧὨ"))
    bstack111111l1ll1_opy_ = 0
    while self.bstack111111ll11l_opy_.poll() == None:
      bstack1llllll111ll_opy_ = self.bstack1111111llll_opy_()
      if bstack1llllll111ll_opy_:
        self.logger.debug(bstack11l1l11_opy_ (u"ࠧࡎࡥࡢ࡮ࡷ࡬ࠥࡉࡨࡦࡥ࡮ࠤࡸࡻࡣࡤࡧࡶࡷ࡫ࡻ࡬ࠣὩ"))
        self.bstack111111111ll_opy_ = True
        return True
      bstack111111l1ll1_opy_ += 1
      self.logger.debug(bstack11l1l11_opy_ (u"ࠨࡈࡦࡣ࡯ࡸ࡭ࠦࡃࡩࡧࡦ࡯ࠥࡘࡥࡵࡴࡼࠤ࠲ࠦࡻࡾࠤὪ").format(bstack111111l1ll1_opy_))
      time.sleep(2)
    self.logger.error(bstack11l1l11_opy_ (u"ࠢࡇࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡷࡹࡧࡲࡵࠢࡳࡩࡷࡩࡹ࠭ࠢࡋࡩࡦࡲࡴࡩࠢࡆ࡬ࡪࡩ࡫ࠡࡈࡤ࡭ࡱ࡫ࡤࠡࡣࡩࡸࡪࡸࠠࡼࡿࠣࡥࡹࡺࡥ࡮ࡲࡷࡷࠧὫ").format(bstack111111l1ll1_opy_))
    self.bstack1llllll1l1ll_opy_ = True
    return False
  def bstack1111111llll_opy_(self, bstack111111l1ll1_opy_ = 0):
    if bstack111111l1ll1_opy_ > 10:
      return False
    try:
      bstack1llllll1ll11_opy_ = os.environ.get(bstack11l1l11_opy_ (u"ࠨࡒࡈࡖࡈ࡟࡟ࡔࡇࡕ࡚ࡊࡘ࡟ࡂࡆࡇࡖࡊ࡙ࡓࠨὬ"), bstack11l1l11_opy_ (u"ࠩ࡫ࡸࡹࡶ࠺࠰࠱࡯ࡳࡨࡧ࡬ࡩࡱࡶࡸ࠿࠻࠳࠴࠺ࠪὭ"))
      bstack1llllll1l111_opy_ = bstack1llllll1ll11_opy_ + bstack11l1l1111l1_opy_
      response = requests.get(bstack1llllll1l111_opy_)
      data = response.json()
      self.percy_build_id = data.get(bstack11l1l11_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࠩὮ"), {}).get(bstack11l1l11_opy_ (u"ࠫ࡮ࡪࠧὯ"), None)
      return True
    except:
      self.logger.debug(bstack11l1l11_opy_ (u"ࠧࡋࡲࡳࡱࡵࠤࡴࡩࡣࡶࡴࡵࡩࡩࠦࡷࡩ࡫࡯ࡩࠥࡶࡲࡰࡥࡨࡷࡸ࡯࡮ࡨࠢ࡫ࡩࡦࡲࡴࡩࠢࡦ࡬ࡪࡩ࡫ࠡࡴࡨࡷࡵࡵ࡮ࡴࡧࠥὰ"))
      return False
  def bstack1lllllll1l1l_opy_(self):
    bstack1lllll1ll1l1_opy_ = bstack11l1l11_opy_ (u"࠭ࡡࡱࡲࠪά") if self.bstack1ll1l1lll_opy_ else bstack11l1l11_opy_ (u"ࠧࡢࡷࡷࡳࡲࡧࡴࡦࠩὲ")
    bstack1111111ll1l_opy_ = bstack11l1l11_opy_ (u"ࠣࡷࡱࡨࡪ࡬ࡩ࡯ࡧࡧࠦέ") if self.config.get(bstack11l1l11_opy_ (u"ࠩࡳࡩࡷࡩࡹࠨὴ")) is None else True
    bstack11ll11l1ll1_opy_ = bstack11l1l11_opy_ (u"ࠥࡥࡵ࡯࠯ࡢࡲࡳࡣࡵ࡫ࡲࡤࡻ࠲࡫ࡪࡺ࡟ࡱࡴࡲ࡮ࡪࡩࡴࡠࡶࡲ࡯ࡪࡴ࠿࡯ࡣࡰࡩࡂࢁࡽࠧࡶࡼࡴࡪࡃࡻࡾࠨࡳࡩࡷࡩࡹ࠾ࡽࢀࠦή").format(self.config[bstack11l1l11_opy_ (u"ࠫࡵࡸ࡯࡫ࡧࡦࡸࡓࡧ࡭ࡦࠩὶ")], bstack1lllll1ll1l1_opy_, bstack1111111ll1l_opy_)
    if self.percy_capture_mode:
      bstack11ll11l1ll1_opy_ += bstack11l1l11_opy_ (u"ࠧࠬࡰࡦࡴࡦࡽࡤࡩࡡࡱࡶࡸࡶࡪࡥ࡭ࡰࡦࡨࡁࢀࢃࠢί").format(self.percy_capture_mode)
    uri = bstack1l11l1l1ll_opy_(bstack11ll11l1ll1_opy_)
    try:
      response = bstack11lll1llll_opy_(bstack11l1l11_opy_ (u"࠭ࡇࡆࡖࠪὸ"), uri, {}, {bstack11l1l11_opy_ (u"ࠧࡢࡷࡷ࡬ࠬό"): (self.config[bstack11l1l11_opy_ (u"ࠨࡷࡶࡩࡷࡔࡡ࡮ࡧࠪὺ")], self.config[bstack11l1l11_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴࡍࡨࡽࠬύ")])})
      if response.status_code == 200:
        data = response.json()
        self.bstack1l1l1l1l1l_opy_ = data.get(bstack11l1l11_opy_ (u"ࠪࡷࡺࡩࡣࡦࡵࡶࠫὼ"))
        self.percy_capture_mode = data.get(bstack11l1l11_opy_ (u"ࠫࡵ࡫ࡲࡤࡻࡢࡧࡦࡶࡴࡶࡴࡨࡣࡲࡵࡤࡦࠩώ"))
        os.environ[bstack11l1l11_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡕࡋࡒࡄ࡛ࠪ὾")] = str(self.bstack1l1l1l1l1l_opy_)
        os.environ[bstack11l1l11_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡖࡅࡓࡅ࡜ࡣࡈࡇࡐࡕࡗࡕࡉࡤࡓࡏࡅࡇࠪ὿")] = str(self.percy_capture_mode)
        if bstack1111111ll1l_opy_ == bstack11l1l11_opy_ (u"ࠢࡶࡰࡧࡩ࡫࡯࡮ࡦࡦࠥᾀ") and str(self.bstack1l1l1l1l1l_opy_).lower() == bstack11l1l11_opy_ (u"ࠣࡶࡵࡹࡪࠨᾁ"):
          self.bstack1l11lll11_opy_ = True
        if bstack11l1l11_opy_ (u"ࠤࡷࡳࡰ࡫࡮ࠣᾂ") in data:
          return data[bstack11l1l11_opy_ (u"ࠥࡸࡴࡱࡥ࡯ࠤᾃ")]
        else:
          raise bstack11l1l11_opy_ (u"࡙ࠫࡵ࡫ࡦࡰࠣࡒࡴࡺࠠࡇࡱࡸࡲࡩࠦ࠭ࠡࡽࢀࠫᾄ").format(data)
      else:
        raise bstack11l1l11_opy_ (u"ࠧࡌࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡࡨࡨࡸࡨ࡮ࠠࡱࡧࡵࡧࡾࠦࡴࡰ࡭ࡨࡲ࠱ࠦࡒࡦࡵࡳࡳࡳࡹࡥࠡࡵࡷࡥࡹࡻࡳࠡ࠯ࠣࡿࢂ࠲ࠠࡓࡧࡶࡴࡴࡴࡳࡦࠢࡅࡳࡩࡿࠠ࠮ࠢࡾࢁࠧᾅ").format(response.status_code, response.json())
    except Exception as e:
      self.logger.error(bstack11l1l11_opy_ (u"ࠨࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥࡩࡲࡦࡣࡷ࡭ࡳ࡭ࠠࡱࡧࡵࡧࡾࠦࡰࡳࡱ࡭ࡩࡨࡺࠢᾆ").format(e))
  def bstack111111l1l1l_opy_(self):
    bstack1lllllllll1l_opy_ = os.path.join(tempfile.gettempdir(), bstack11l1l11_opy_ (u"ࠢࡱࡧࡵࡧࡾࡉ࡯࡯ࡨ࡬࡫࠳ࡰࡳࡰࡰࠥᾇ"))
    try:
      if bstack11l1l11_opy_ (u"ࠨࡸࡨࡶࡸ࡯࡯࡯ࠩᾈ") not in self.bstack1lllll1ll11l_opy_:
        self.bstack1lllll1ll11l_opy_[bstack11l1l11_opy_ (u"ࠩࡹࡩࡷࡹࡩࡰࡰࠪᾉ")] = 2
      with open(bstack1lllllllll1l_opy_, bstack11l1l11_opy_ (u"ࠪࡻࠬᾊ")) as fp:
        json.dump(self.bstack1lllll1ll11l_opy_, fp)
      return bstack1lllllllll1l_opy_
    except Exception as e:
      self.logger.error(bstack11l1l11_opy_ (u"࡚ࠦࡴࡡࡣ࡮ࡨࠤࡹࡵࠠࡤࡴࡨࡥࡹ࡫ࠠࡱࡧࡵࡧࡾࠦࡣࡰࡰࡩ࠰ࠥࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡࡽࢀࠦᾋ").format(e))
  def bstack111111l1111_opy_(self, cmd, env = os.environ.copy()):
    try:
      if self.bstack1lllll1ll111_opy_ == bstack11l1l11_opy_ (u"ࠬࡽࡩ࡯ࠩᾌ"):
        bstack1111111l111_opy_ = [bstack11l1l11_opy_ (u"࠭ࡣ࡮ࡦ࠱ࡩࡽ࡫ࠧᾍ"), bstack11l1l11_opy_ (u"ࠧ࠰ࡥࠪᾎ")]
        cmd = bstack1111111l111_opy_ + cmd
      cmd = bstack11l1l11_opy_ (u"ࠨࠢࠪᾏ").join(cmd)
      self.logger.debug(bstack11l1l11_opy_ (u"ࠤࡕࡹࡳࡴࡩ࡯ࡩࠣࡿࢂࠨᾐ").format(cmd))
      with open(self.bstack1lllllll1lll_opy_, bstack11l1l11_opy_ (u"ࠥࡥࠧᾑ")) as bstack1111111l1l1_opy_:
        process = subprocess.Popen(cmd, shell=True, stdout=bstack1111111l1l1_opy_, text=True, stderr=bstack1111111l1l1_opy_, env=env, universal_newlines=True)
      return process
    except Exception as e:
      self.bstack1llllll1l1ll_opy_ = True
      self.logger.error(bstack11l1l11_opy_ (u"ࠦࡋࡧࡩ࡭ࡧࡧࠤࡹࡵࠠࡴࡶࡤࡶࡹࠦࡰࡦࡴࡦࡽࠥࡽࡩࡵࡪࠣࡧࡲࡪࠠ࠮ࠢࡾࢁ࠱ࠦࡅࡹࡥࡨࡴࡹ࡯࡯࡯࠼ࠣࡿࢂࠨᾒ").format(cmd, e))
  def shutdown(self):
    try:
      if self.bstack111111111ll_opy_:
        self.logger.info(bstack11l1l11_opy_ (u"࡙ࠧࡴࡰࡲࡳ࡭ࡳ࡭ࠠࡑࡧࡵࡧࡾࠨᾓ"))
        cmd = [self.binary_path, bstack11l1l11_opy_ (u"ࠨࡥࡹࡧࡦ࠾ࡸࡺ࡯ࡱࠤᾔ")]
        self.bstack111111l1111_opy_(cmd)
        self.bstack111111111ll_opy_ = False
    except Exception as e:
      self.logger.error(bstack11l1l11_opy_ (u"ࠢࡇࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡷࡹࡵࡰࠡࡵࡨࡷࡸ࡯࡯࡯ࠢࡺ࡭ࡹ࡮ࠠࡤࡱࡰࡱࡦࡴࡤࠡ࠯ࠣࡿࢂ࠲ࠠࡆࡺࡦࡩࡵࡺࡩࡰࡰ࠽ࠤࢀࢃࠢᾕ").format(cmd, e))
  def bstack1l1l1l1l1_opy_(self):
    if not self.bstack1l1l1l1l1l_opy_:
      return
    try:
      bstack1llllll11ll1_opy_ = 0
      while not self.bstack111111111ll_opy_ and bstack1llllll11ll1_opy_ < self.bstack1llllll1lll1_opy_:
        if self.bstack1llllll1l1ll_opy_:
          self.logger.info(bstack11l1l11_opy_ (u"ࠣࡒࡨࡶࡨࡿࠠࡴࡧࡷࡹࡵࠦࡦࡢ࡫࡯ࡩࡩࠨᾖ"))
          return
        time.sleep(1)
        bstack1llllll11ll1_opy_ += 1
      os.environ[bstack11l1l11_opy_ (u"ࠩࡓࡉࡗࡉ࡙ࡠࡄࡈࡗ࡙ࡥࡐࡍࡃࡗࡊࡔࡘࡍࠨᾗ")] = str(self.bstack1llllllllll1_opy_())
      self.logger.info(bstack11l1l11_opy_ (u"ࠥࡔࡪࡸࡣࡺࠢࡶࡩࡹࡻࡰࠡࡥࡲࡱࡵࡲࡥࡵࡧࡧࠦᾘ"))
    except Exception as e:
      self.logger.error(bstack11l1l11_opy_ (u"࡚ࠦࡴࡡࡣ࡮ࡨࠤࡹࡵࠠࡴࡧࡷࡹࡵࠦࡰࡦࡴࡦࡽ࠱ࠦࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢࡾࢁࠧᾙ").format(e))
  def bstack1llllllllll1_opy_(self):
    if self.bstack1ll1l1lll_opy_:
      return
    try:
      bstack1llllll111l1_opy_ = [platform[bstack11l1l11_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡔࡡ࡮ࡧࠪᾚ")].lower() for platform in self.config.get(bstack11l1l11_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩᾛ"), [])]
      bstack1llllllll11l_opy_ = sys.maxsize
      bstack1111111lll1_opy_ = bstack11l1l11_opy_ (u"ࠧࠨᾜ")
      for browser in bstack1llllll111l1_opy_:
        if browser in self.bstack1lllllll1l11_opy_:
          bstack1llllll1111l_opy_ = self.bstack1lllllll1l11_opy_[browser]
        if bstack1llllll1111l_opy_ < bstack1llllllll11l_opy_:
          bstack1llllllll11l_opy_ = bstack1llllll1111l_opy_
          bstack1111111lll1_opy_ = browser
      return bstack1111111lll1_opy_
    except Exception as e:
      self.logger.error(bstack11l1l11_opy_ (u"ࠣࡗࡱࡥࡧࡲࡥࠡࡶࡲࠤ࡫࡯࡮ࡥࠢࡥࡩࡸࡺࠠࡱ࡮ࡤࡸ࡫ࡵࡲ࡮࠮ࠣࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡻࡾࠤᾝ").format(e))
  @classmethod
  def bstack1llll11111_opy_(self):
    return os.getenv(bstack11l1l11_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡒࡈࡖࡈ࡟ࠧᾞ"), bstack11l1l11_opy_ (u"ࠪࡊࡦࡲࡳࡦࠩᾟ")).lower()
  @classmethod
  def bstack11l1lllll1_opy_(self):
    return os.getenv(bstack11l1l11_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡔࡊࡘࡃ࡚ࡡࡆࡅࡕ࡚ࡕࡓࡇࡢࡑࡔࡊࡅࠨᾠ"), bstack11l1l11_opy_ (u"ࠬ࠭ᾡ"))
  @classmethod
  def bstack11llllll1l1_opy_(cls, value):
    cls.bstack1l11lll11_opy_ = value
  @classmethod
  def bstack1lllll1ll1ll_opy_(cls):
    return cls.bstack1l11lll11_opy_
  @classmethod
  def bstack11llllllll1_opy_(cls, value):
    cls.percy_build_id = value
  @classmethod
  def bstack1llllll1l1l1_opy_(cls):
    return cls.percy_build_id