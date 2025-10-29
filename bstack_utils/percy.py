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
from bstack_utils.helper import bstack1l111lll1_opy_
from bstack_utils.measure import measure
from bstack_utils.bstack11l1ll111_opy_ import bstack1l11lll1l1_opy_
class bstack11lll11111_opy_:
  working_dir = os.getcwd()
  bstack1l1ll1l11_opy_ = False
  config = {}
  bstack111l1l1llll_opy_ = bstack11l11ll_opy_ (u"ࠧࠨὤ")
  binary_path = bstack11l11ll_opy_ (u"ࠨࠩὥ")
  bstack1lllllllll11_opy_ = bstack11l11ll_opy_ (u"ࠩࠪὦ")
  bstack1l1111lll_opy_ = False
  bstack1llllll11l1l_opy_ = None
  bstack1lllll1l11l1_opy_ = {}
  bstack1llllllllll1_opy_ = 300
  bstack1llllllll1ll_opy_ = False
  logger = None
  bstack1lllllll1lll_opy_ = False
  bstack11l1lll11_opy_ = False
  percy_build_id = None
  bstack1lllll11llll_opy_ = bstack11l11ll_opy_ (u"ࠪࠫὧ")
  bstack1lllll11lll1_opy_ = {
    bstack11l11ll_opy_ (u"ࠫࡨ࡮ࡲࡰ࡯ࡨࠫὨ") : 1,
    bstack11l11ll_opy_ (u"ࠬ࡬ࡩࡳࡧࡩࡳࡽ࠭Ὡ") : 2,
    bstack11l11ll_opy_ (u"࠭ࡥࡥࡩࡨࠫὪ") : 3,
    bstack11l11ll_opy_ (u"ࠧࡴࡣࡩࡥࡷ࡯ࠧὫ") : 4
  }
  def __init__(self) -> None: pass
  def bstack1lllll1ll111_opy_(self):
    bstack1lllll1lll11_opy_ = bstack11l11ll_opy_ (u"ࠨࠩὬ")
    bstack1llllll1ll11_opy_ = sys.platform
    bstack1lllll1l11ll_opy_ = bstack11l11ll_opy_ (u"ࠩࡳࡩࡷࡩࡹࠨὭ")
    if re.match(bstack11l11ll_opy_ (u"ࠥࡨࡦࡸࡷࡪࡰࡿࡱࡦࡩࠠࡰࡵࠥὮ"), bstack1llllll1ll11_opy_) != None:
      bstack1lllll1lll11_opy_ = bstack11l1l111l11_opy_ + bstack11l11ll_opy_ (u"ࠦ࠴ࡶࡥࡳࡥࡼ࠱ࡴࡹࡸ࠯ࡼ࡬ࡴࠧὯ")
      self.bstack1lllll11llll_opy_ = bstack11l11ll_opy_ (u"ࠬࡳࡡࡤࠩὰ")
    elif re.match(bstack11l11ll_opy_ (u"ࠨ࡭ࡴࡹ࡬ࡲࢁࡳࡳࡺࡵࡿࡱ࡮ࡴࡧࡸࡾࡦࡽ࡬ࡽࡩ࡯ࡾࡥࡧࡨࡽࡩ࡯ࡾࡺ࡭ࡳࡩࡥࡽࡧࡰࡧࢁࡽࡩ࡯࠵࠵ࠦά"), bstack1llllll1ll11_opy_) != None:
      bstack1lllll1lll11_opy_ = bstack11l1l111l11_opy_ + bstack11l11ll_opy_ (u"ࠢ࠰ࡲࡨࡶࡨࡿ࠭ࡸ࡫ࡱ࠲ࡿ࡯ࡰࠣὲ")
      bstack1lllll1l11ll_opy_ = bstack11l11ll_opy_ (u"ࠣࡲࡨࡶࡨࡿ࠮ࡦࡺࡨࠦέ")
      self.bstack1lllll11llll_opy_ = bstack11l11ll_opy_ (u"ࠩࡺ࡭ࡳ࠭ὴ")
    else:
      bstack1lllll1lll11_opy_ = bstack11l1l111l11_opy_ + bstack11l11ll_opy_ (u"ࠥ࠳ࡵ࡫ࡲࡤࡻ࠰ࡰ࡮ࡴࡵࡹ࠰ࡽ࡭ࡵࠨή")
      self.bstack1lllll11llll_opy_ = bstack11l11ll_opy_ (u"ࠫࡱ࡯࡮ࡶࡺࠪὶ")
    return bstack1lllll1lll11_opy_, bstack1lllll1l11ll_opy_
  def bstack1111111l1l1_opy_(self):
    try:
      bstack1llllll111l1_opy_ = [os.path.join(expanduser(bstack11l11ll_opy_ (u"ࠧࢄࠢί")), bstack11l11ll_opy_ (u"࠭࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠭ὸ")), self.working_dir, tempfile.gettempdir()]
      for path in bstack1llllll111l1_opy_:
        if(self.bstack1lllll11l1ll_opy_(path)):
          return path
      raise bstack11l11ll_opy_ (u"ࠢࡖࡰࡤࡦࡱ࡫ࠠࡵࡱࠣࡨࡴࡽ࡮࡭ࡱࡤࡨࠥࡶࡥࡳࡥࡼࠤࡧ࡯࡮ࡢࡴࡼࠦό")
    except Exception as e:
      self.logger.error(bstack11l11ll_opy_ (u"ࠣࡈࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤ࡫࡯࡮ࡥࠢࡤࡺࡦ࡯࡬ࡢࡤ࡯ࡩࠥࡶࡡࡵࡪࠣࡪࡴࡸࠠࡱࡧࡵࡧࡾࠦࡤࡰࡹࡱࡰࡴࡧࡤ࠭ࠢࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࠳ࠠࡼࡿࠥὺ").format(e))
  def bstack1lllll11l1ll_opy_(self, path):
    try:
      if not os.path.exists(path):
        os.makedirs(path)
      return True
    except:
      return False
  def bstack11111111ll1_opy_(self, bstack1llllll11lll_opy_):
    return os.path.join(bstack1llllll11lll_opy_, self.bstack111l1l1llll_opy_ + bstack11l11ll_opy_ (u"ࠤ࠱ࡩࡹࡧࡧࠣύ"))
  def bstack1llllllll1l1_opy_(self, bstack1llllll11lll_opy_, bstack1lllll1ll1l1_opy_):
    if not bstack1lllll1ll1l1_opy_: return
    try:
      bstack1llllll1l1ll_opy_ = self.bstack11111111ll1_opy_(bstack1llllll11lll_opy_)
      with open(bstack1llllll1l1ll_opy_, bstack11l11ll_opy_ (u"ࠥࡻࠧὼ")) as f:
        f.write(bstack1lllll1ll1l1_opy_)
        self.logger.debug(bstack11l11ll_opy_ (u"ࠦࡘࡧࡶࡦࡦࠣࡲࡪࡽࠠࡆࡖࡤ࡫ࠥ࡬࡯ࡳࠢࡳࡩࡷࡩࡹࠣώ"))
    except Exception as e:
      self.logger.error(bstack11l11ll_opy_ (u"࡛ࠧ࡮ࡢࡤ࡯ࡩࠥࡺ࡯ࠡࡵࡤࡺࡪࠦࡴࡩࡧࠣࡩࡹࡧࡧ࠭ࠢࡨࡶࡷࡵࡲ࠻ࠢࡾࢁࠧ὾").format(e))
  def bstack1lllllllll1l_opy_(self, bstack1llllll11lll_opy_):
    try:
      bstack1llllll1l1ll_opy_ = self.bstack11111111ll1_opy_(bstack1llllll11lll_opy_)
      if os.path.exists(bstack1llllll1l1ll_opy_):
        with open(bstack1llllll1l1ll_opy_, bstack11l11ll_opy_ (u"ࠨࡲࠣ὿")) as f:
          bstack1lllll1ll1l1_opy_ = f.read().strip()
          return bstack1lllll1ll1l1_opy_ if bstack1lllll1ll1l1_opy_ else None
    except Exception as e:
      self.logger.error(bstack11l11ll_opy_ (u"ࠢࡇࡣ࡬ࡰࡪࡪࠠ࡭ࡱࡤࡨ࡮ࡴࡧࠡࡇࡗࡥ࡬࠲ࠠࡦࡴࡵࡳࡷࡀࠠࡼࡿࠥᾀ").format(e))
  def bstack1llllll1ll1l_opy_(self, bstack1llllll11lll_opy_, bstack1lllll1lll11_opy_):
    bstack1lllllll111l_opy_ = self.bstack1lllllllll1l_opy_(bstack1llllll11lll_opy_)
    if bstack1lllllll111l_opy_:
      try:
        bstack11111111l11_opy_ = self.bstack1lllll1l1l11_opy_(bstack1lllllll111l_opy_, bstack1lllll1lll11_opy_)
        if not bstack11111111l11_opy_:
          self.logger.debug(bstack11l11ll_opy_ (u"ࠣࡒࡨࡶࡨࡿࠠࡣ࡫ࡱࡥࡷࡿࠠࡪࡵࠣࡹࡵࠦࡴࡰࠢࡧࡥࡹ࡫ࠠࠩࡇࡗࡥ࡬ࠦࡵ࡯ࡥ࡫ࡥࡳ࡭ࡥࡥࠫࠥᾁ"))
          return True
        self.logger.debug(bstack11l11ll_opy_ (u"ࠤࡑࡩࡼࠦࡐࡦࡴࡦࡽࠥࡨࡩ࡯ࡣࡵࡽࠥࡼࡥࡳࡵ࡬ࡳࡳࠦࡡࡷࡣ࡬ࡰࡦࡨ࡬ࡦ࠮ࠣࡨࡴࡽ࡮࡭ࡱࡤࡨ࡮ࡴࡧࠡࡷࡳࡨࡦࡺࡥࠣᾂ"))
        return False
      except Exception as e:
        self.logger.warn(bstack11l11ll_opy_ (u"ࠥࡊࡦ࡯࡬ࡦࡦࠣࡸࡴࠦࡣࡩࡧࡦ࡯ࠥ࡬࡯ࡳࠢࡥ࡭ࡳࡧࡲࡺࠢࡸࡴࡩࡧࡴࡦࡵ࠯ࠤࡺࡹࡩ࡯ࡩࠣࡩࡽ࡯ࡳࡵ࡫ࡱ࡫ࠥࡨࡩ࡯ࡣࡵࡽ࠿ࠦࡻࡾࠤᾃ").format(e))
    return False
  def bstack1lllll1l1l11_opy_(self, bstack1lllllll111l_opy_, bstack1lllll1lll11_opy_):
    try:
      headers = {
        bstack11l11ll_opy_ (u"ࠦࡎ࡬࠭ࡏࡱࡱࡩ࠲ࡓࡡࡵࡥ࡫ࠦᾄ"): bstack1lllllll111l_opy_
      }
      response = bstack1l111lll1_opy_(bstack11l11ll_opy_ (u"ࠬࡍࡅࡕࠩᾅ"), bstack1lllll1lll11_opy_, {}, {bstack11l11ll_opy_ (u"ࠨࡨࡦࡣࡧࡩࡷࡹࠢᾆ"): headers})
      if response.status_code == 304:
        return False
      return True
    except Exception as e:
      raise(bstack11l11ll_opy_ (u"ࠢࡆࡴࡵࡳࡷࠦࡣࡩࡧࡦ࡯࡮ࡴࡧࠡࡨࡲࡶࠥࡖࡥࡳࡥࡼࠤࡧ࡯࡮ࡢࡴࡼࠤࡺࡶࡤࡢࡶࡨࡷ࠿ࠦࡻࡾࠤᾇ").format(e))
  @measure(event_name=EVENTS.bstack11l11ll111l_opy_, stage=STAGE.bstack1l1l1l1lll_opy_)
  def bstack1lllll11l11l_opy_(self, bstack1lllll1lll11_opy_, bstack1lllll1l11ll_opy_):
    try:
      bstack1llllll111ll_opy_ = self.bstack1111111l1l1_opy_()
      bstack1lllll1l1lll_opy_ = os.path.join(bstack1llllll111ll_opy_, bstack11l11ll_opy_ (u"ࠨࡲࡨࡶࡨࡿ࠮ࡻ࡫ࡳࠫᾈ"))
      bstack1lllll1l1111_opy_ = os.path.join(bstack1llllll111ll_opy_, bstack1lllll1l11ll_opy_)
      if self.bstack1llllll1ll1l_opy_(bstack1llllll111ll_opy_, bstack1lllll1lll11_opy_): # if bstack1lllll1l1l1l_opy_, bstack1llll1lll1l_opy_ bstack1lllll1ll1l1_opy_ is bstack1lllllll1ll1_opy_ to bstack111l1l11l11_opy_ version available (response 304)
        if os.path.exists(bstack1lllll1l1111_opy_):
          self.logger.info(bstack11l11ll_opy_ (u"ࠤࡓࡩࡷࡩࡹࠡࡤ࡬ࡲࡦࡸࡹࠡࡨࡲࡹࡳࡪࠠࡪࡰࠣࡿࢂ࠲ࠠࡴ࡭࡬ࡴࡵ࡯࡮ࡨࠢࡧࡳࡼࡴ࡬ࡰࡣࡧࠦᾉ").format(bstack1lllll1l1111_opy_))
          return bstack1lllll1l1111_opy_
        if os.path.exists(bstack1lllll1l1lll_opy_):
          self.logger.info(bstack11l11ll_opy_ (u"ࠥࡔࡪࡸࡣࡺࠢࡽ࡭ࡵࠦࡦࡰࡷࡱࡨࠥ࡯࡮ࠡࡽࢀ࠰ࠥࡻ࡮ࡻ࡫ࡳࡴ࡮ࡴࡧࠣᾊ").format(bstack1lllll1l1lll_opy_))
          return self.bstack1lllllll11ll_opy_(bstack1lllll1l1lll_opy_, bstack1lllll1l11ll_opy_)
      self.logger.info(bstack11l11ll_opy_ (u"ࠦࡉࡵࡷ࡯࡮ࡲࡥࡩ࡯࡮ࡨࠢࡳࡩࡷࡩࡹࠡࡤ࡬ࡲࡦࡸࡹࠡࡨࡵࡳࡲࠦࡻࡾࠤᾋ").format(bstack1lllll1lll11_opy_))
      response = bstack1l111lll1_opy_(bstack11l11ll_opy_ (u"ࠬࡍࡅࡕࠩᾌ"), bstack1lllll1lll11_opy_, {}, {})
      if response.status_code == 200:
        bstack1llllllll11l_opy_ = response.headers.get(bstack11l11ll_opy_ (u"ࠨࡅࡕࡣࡪࠦᾍ"), bstack11l11ll_opy_ (u"ࠢࠣᾎ"))
        if bstack1llllllll11l_opy_:
          self.bstack1llllllll1l1_opy_(bstack1llllll111ll_opy_, bstack1llllllll11l_opy_)
        with open(bstack1lllll1l1lll_opy_, bstack11l11ll_opy_ (u"ࠨࡹࡥࠫᾏ")) as file:
          file.write(response.content)
        self.logger.info(bstack11l11ll_opy_ (u"ࠤࡇࡳࡼࡴ࡬ࡰࡣࡧࡩࡩࠦࡰࡦࡴࡦࡽࠥࡨࡩ࡯ࡣࡵࡽࠥࡧ࡮ࡥࠢࡶࡥࡻ࡫ࡤࠡࡣࡷࠤࢀࢃࠢᾐ").format(bstack1lllll1l1lll_opy_))
        return self.bstack1lllllll11ll_opy_(bstack1lllll1l1lll_opy_, bstack1lllll1l11ll_opy_)
      else:
        raise(bstack11l11ll_opy_ (u"ࠥࡊࡦ࡯࡬ࡦࡦࠣࡸࡴࠦࡤࡰࡹࡱࡰࡴࡧࡤࠡࡶ࡫ࡩࠥ࡬ࡩ࡭ࡧ࠱ࠤࡘࡺࡡࡵࡷࡶࠤࡨࡵࡤࡦ࠼ࠣࡿࢂࠨᾑ").format(response.status_code))
    except Exception as e:
      self.logger.error(bstack11l11ll_opy_ (u"࡚ࠦࡴࡡࡣ࡮ࡨࠤࡹࡵࠠࡥࡱࡺࡲࡱࡵࡡࡥࠢࡳࡩࡷࡩࡹࠡࡤ࡬ࡲࡦࡸࡹ࠻ࠢࡾࢁࠧᾒ").format(e))
  def bstack1lllll1ll1ll_opy_(self, bstack1lllll1lll11_opy_, bstack1lllll1l11ll_opy_):
    try:
      retry = 2
      bstack1lllll1l1111_opy_ = None
      bstack1llllll11ll1_opy_ = False
      while retry > 0:
        bstack1lllll1l1111_opy_ = self.bstack1lllll11l11l_opy_(bstack1lllll1lll11_opy_, bstack1lllll1l11ll_opy_)
        bstack1llllll11ll1_opy_ = self.bstack1llllll1lll1_opy_(bstack1lllll1lll11_opy_, bstack1lllll1l11ll_opy_, bstack1lllll1l1111_opy_)
        if bstack1llllll11ll1_opy_:
          break
        retry -= 1
      return bstack1lllll1l1111_opy_, bstack1llllll11ll1_opy_
    except Exception as e:
      self.logger.error(bstack11l11ll_opy_ (u"࡛ࠧ࡮ࡢࡤ࡯ࡩࠥࡺ࡯ࠡࡩࡨࡸࠥࡶࡥࡳࡥࡼࠤࡧ࡯࡮ࡢࡴࡼࠤࡵࡧࡴࡩࠤᾓ").format(e))
    return bstack1lllll1l1111_opy_, False
  def bstack1llllll1lll1_opy_(self, bstack1lllll1lll11_opy_, bstack1lllll1l11ll_opy_, bstack1lllll1l1111_opy_, bstack1lllll1llll1_opy_ = 0):
    if bstack1lllll1llll1_opy_ > 1:
      return False
    if bstack1lllll1l1111_opy_ == None or os.path.exists(bstack1lllll1l1111_opy_) == False:
      self.logger.warn(bstack11l11ll_opy_ (u"ࠨࡐࡦࡴࡦࡽࠥࡶࡡࡵࡪࠣࡲࡴࡺࠠࡧࡱࡸࡲࡩ࠲ࠠࡳࡧࡷࡶࡾ࡯࡮ࡨࠢࡧࡳࡼࡴ࡬ࡰࡣࡧࠦᾔ"))
      return False
    bstack1111111l1ll_opy_ = bstack11l11ll_opy_ (u"ࡲࠣࡠ࠱࠮ࡅࡶࡥࡳࡥࡼ࠳ࡨࡲࡩࠡ࡞ࡧ࠯ࡡ࠴࡜ࡥ࠭࡟࠲ࡡࡪࠫࠣᾕ")
    command = bstack11l11ll_opy_ (u"ࠨࡽࢀࠤ࠲࠳ࡶࡦࡴࡶ࡭ࡴࡴࠧᾖ").format(bstack1lllll1l1111_opy_)
    bstack111111111ll_opy_ = subprocess.check_output(command, shell=True, text=True)
    if re.match(bstack1111111l1ll_opy_, bstack111111111ll_opy_) != None:
      return True
    else:
      self.logger.error(bstack11l11ll_opy_ (u"ࠤࡓࡩࡷࡩࡹࠡࡸࡨࡶࡸ࡯࡯࡯ࠢࡦ࡬ࡪࡩ࡫ࠡࡨࡤ࡭ࡱ࡫ࡤࠣᾗ"))
      return False
  def bstack1lllllll11ll_opy_(self, bstack1lllll1l1lll_opy_, bstack1lllll1l11ll_opy_):
    try:
      working_dir = os.path.dirname(bstack1lllll1l1lll_opy_)
      shutil.unpack_archive(bstack1lllll1l1lll_opy_, working_dir)
      bstack1lllll1l1111_opy_ = os.path.join(working_dir, bstack1lllll1l11ll_opy_)
      os.chmod(bstack1lllll1l1111_opy_, 0o755)
      return bstack1lllll1l1111_opy_
    except Exception as e:
      self.logger.error(bstack11l11ll_opy_ (u"࡙ࠥࡳࡧࡢ࡭ࡧࠣࡸࡴࠦࡵ࡯ࡼ࡬ࡴࠥࡶࡥࡳࡥࡼࠤࡧ࡯࡮ࡢࡴࡼࠦᾘ"))
  def bstack1llllll11l11_opy_(self):
    try:
      bstack1llllll11111_opy_ = self.config.get(bstack11l11ll_opy_ (u"ࠫࡵ࡫ࡲࡤࡻࠪᾙ"))
      bstack1llllll11l11_opy_ = bstack1llllll11111_opy_ or (bstack1llllll11111_opy_ is None and self.bstack1l1ll1l11_opy_)
      if not bstack1llllll11l11_opy_ or self.config.get(bstack11l11ll_opy_ (u"ࠬ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࠨᾚ"), None) not in bstack11l11lllll1_opy_:
        return False
      self.bstack1l1111lll_opy_ = True
      return True
    except Exception as e:
      self.logger.error(bstack11l11ll_opy_ (u"ࠨࡕ࡯ࡣࡥࡰࡪࠦࡴࡰࠢࡧࡩࡹ࡫ࡣࡵࠢࡳࡩࡷࡩࡹ࠭ࠢࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥࢁࡽࠣᾛ").format(e))
  def bstack1111111l111_opy_(self):
    try:
      bstack1111111l111_opy_ = self.percy_capture_mode
      return bstack1111111l111_opy_
    except Exception as e:
      self.logger.error(bstack11l11ll_opy_ (u"ࠢࡖࡰࡤࡦࡱ࡫ࠠࡵࡱࠣࡨࡪࡺࡥࡤࡶࠣࡴࡪࡸࡣࡺࠢࡦࡥࡵࡺࡵࡳࡧࠣࡱࡴࡪࡥ࠭ࠢࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥࢁࡽࠣᾜ").format(e))
  def init(self, bstack1l1ll1l11_opy_, config, logger):
    self.bstack1l1ll1l11_opy_ = bstack1l1ll1l11_opy_
    self.config = config
    self.logger = logger
    if not self.bstack1llllll11l11_opy_():
      return
    self.bstack1lllll1l11l1_opy_ = config.get(bstack11l11ll_opy_ (u"ࠨࡲࡨࡶࡨࡿࡏࡱࡶ࡬ࡳࡳࡹࠧᾝ"), {})
    self.percy_capture_mode = config.get(bstack11l11ll_opy_ (u"ࠩࡳࡩࡷࡩࡹࡄࡣࡳࡸࡺࡸࡥࡎࡱࡧࡩࠬᾞ"))
    try:
      bstack1lllll1lll11_opy_, bstack1lllll1l11ll_opy_ = self.bstack1lllll1ll111_opy_()
      self.bstack111l1l1llll_opy_ = bstack1lllll1l11ll_opy_
      bstack1lllll1l1111_opy_, bstack1llllll11ll1_opy_ = self.bstack1lllll1ll1ll_opy_(bstack1lllll1lll11_opy_, bstack1lllll1l11ll_opy_)
      if bstack1llllll11ll1_opy_:
        self.binary_path = bstack1lllll1l1111_opy_
        thread = Thread(target=self.bstack1111111l11l_opy_)
        thread.start()
      else:
        self.bstack1lllllll1lll_opy_ = True
        self.logger.error(bstack11l11ll_opy_ (u"ࠥࡍࡳࡼࡡ࡭࡫ࡧࠤࡵ࡫ࡲࡤࡻࠣࡴࡦࡺࡨࠡࡨࡲࡹࡳࡪࠠ࠮ࠢࡾࢁ࠱ࠦࡕ࡯ࡣࡥࡰࡪࠦࡴࡰࠢࡶࡸࡦࡸࡴࠡࡒࡨࡶࡨࡿࠢᾟ").format(bstack1lllll1l1111_opy_))
    except Exception as e:
      self.logger.error(bstack11l11ll_opy_ (u"࡚ࠦࡴࡡࡣ࡮ࡨࠤࡹࡵࠠࡴࡶࡤࡶࡹࠦࡰࡦࡴࡦࡽ࠱ࠦࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢࡾࢁࠧᾠ").format(e))
  def bstack1lllll1lll1l_opy_(self):
    try:
      logfile = os.path.join(self.working_dir, bstack11l11ll_opy_ (u"ࠬࡲ࡯ࡨࠩᾡ"), bstack11l11ll_opy_ (u"࠭ࡰࡦࡴࡦࡽ࠳ࡲ࡯ࡨࠩᾢ"))
      os.makedirs(os.path.dirname(logfile)) if not os.path.exists(os.path.dirname(logfile)) else None
      self.logger.debug(bstack11l11ll_opy_ (u"ࠢࡑࡷࡶ࡬࡮ࡴࡧࠡࡲࡨࡶࡨࡿࠠ࡭ࡱࡪࡷࠥࡧࡴࠡࡽࢀࠦᾣ").format(logfile))
      self.bstack1lllllllll11_opy_ = logfile
    except Exception as e:
      self.logger.error(bstack11l11ll_opy_ (u"ࠣࡗࡱࡥࡧࡲࡥࠡࡶࡲࠤࡸ࡫ࡴࠡࡲࡨࡶࡨࡿࠠ࡭ࡱࡪࠤࡵࡧࡴࡩ࠮ࠣࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡻࡾࠤᾤ").format(e))
  @measure(event_name=EVENTS.bstack11l11l1l1l1_opy_, stage=STAGE.bstack1l1l1l1lll_opy_)
  def bstack1111111l11l_opy_(self):
    bstack1llllll1l111_opy_ = self.bstack1llllll1l1l1_opy_()
    if bstack1llllll1l111_opy_ == None:
      self.bstack1lllllll1lll_opy_ = True
      self.logger.error(bstack11l11ll_opy_ (u"ࠤࡓࡩࡷࡩࡹࠡࡶࡲ࡯ࡪࡴࠠ࡯ࡱࡷࠤ࡫ࡵࡵ࡯ࡦ࠯ࠤࡋࡧࡩ࡭ࡧࡧࠤࡹࡵࠠࡴࡶࡤࡶࡹࠦࡰࡦࡴࡦࡽࠧᾥ"))
      return False
    bstack1llllll1111l_opy_ = [bstack11l11ll_opy_ (u"ࠥࡥࡵࡶ࠺ࡦࡺࡨࡧ࠿ࡹࡴࡢࡴࡷࠦᾦ") if self.bstack1l1ll1l11_opy_ else bstack11l11ll_opy_ (u"ࠫࡪࡾࡥࡤ࠼ࡶࡸࡦࡸࡴࠨᾧ")]
    bstack11111l1l111_opy_ = self.bstack1lllll11ll1l_opy_()
    if bstack11111l1l111_opy_ != None:
      bstack1llllll1111l_opy_.append(bstack11l11ll_opy_ (u"ࠧ࠳ࡣࠡࡽࢀࠦᾨ").format(bstack11111l1l111_opy_))
    env = os.environ.copy()
    env[bstack11l11ll_opy_ (u"ࠨࡐࡆࡔࡆ࡝ࡤ࡚ࡏࡌࡇࡑࠦᾩ")] = bstack1llllll1l111_opy_
    env[bstack11l11ll_opy_ (u"ࠢࡕࡊࡢࡆ࡚ࡏࡌࡅࡡࡘ࡙ࡎࡊࠢᾪ")] = os.environ.get(bstack11l11ll_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡍ࡛ࡂࡠࡗࡘࡍࡉ࠭ᾫ"), bstack11l11ll_opy_ (u"ࠩࠪᾬ"))
    bstack11111111l1l_opy_ = [self.binary_path]
    self.bstack1lllll1lll1l_opy_()
    self.bstack1llllll11l1l_opy_ = self.bstack1lllll11ll11_opy_(bstack11111111l1l_opy_ + bstack1llllll1111l_opy_, env)
    self.logger.debug(bstack11l11ll_opy_ (u"ࠥࡗࡹࡧࡲࡵ࡫ࡱ࡫ࠥࡎࡥࡢ࡮ࡷ࡬ࠥࡉࡨࡦࡥ࡮ࠦᾭ"))
    bstack1lllll1llll1_opy_ = 0
    while self.bstack1llllll11l1l_opy_.poll() == None:
      bstack1lllllllllll_opy_ = self.bstack1lllllll1l1l_opy_()
      if bstack1lllllllllll_opy_:
        self.logger.debug(bstack11l11ll_opy_ (u"ࠦࡍ࡫ࡡ࡭ࡶ࡫ࠤࡈ࡮ࡥࡤ࡭ࠣࡷࡺࡩࡣࡦࡵࡶࡪࡺࡲࠢᾮ"))
        self.bstack1llllllll1ll_opy_ = True
        return True
      bstack1lllll1llll1_opy_ += 1
      self.logger.debug(bstack11l11ll_opy_ (u"ࠧࡎࡥࡢ࡮ࡷ࡬ࠥࡉࡨࡦࡥ࡮ࠤࡗ࡫ࡴࡳࡻࠣ࠱ࠥࢁࡽࠣᾯ").format(bstack1lllll1llll1_opy_))
      time.sleep(2)
    self.logger.error(bstack11l11ll_opy_ (u"ࠨࡆࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡶࡸࡦࡸࡴࠡࡲࡨࡶࡨࡿࠬࠡࡊࡨࡥࡱࡺࡨࠡࡅ࡫ࡩࡨࡱࠠࡇࡣ࡬ࡰࡪࡪࠠࡢࡨࡷࡩࡷࠦࡻࡾࠢࡤࡸࡹ࡫࡭ࡱࡶࡶࠦᾰ").format(bstack1lllll1llll1_opy_))
    self.bstack1lllllll1lll_opy_ = True
    return False
  def bstack1lllllll1l1l_opy_(self, bstack1lllll1llll1_opy_ = 0):
    if bstack1lllll1llll1_opy_ > 10:
      return False
    try:
      bstack1lllll1lllll_opy_ = os.environ.get(bstack11l11ll_opy_ (u"ࠧࡑࡇࡕࡇ࡞ࡥࡓࡆࡔ࡙ࡉࡗࡥࡁࡅࡆࡕࡉࡘ࡙ࠧᾱ"), bstack11l11ll_opy_ (u"ࠨࡪࡷࡸࡵࡀ࠯࠰࡮ࡲࡧࡦࡲࡨࡰࡵࡷ࠾࠺࠹࠳࠹ࠩᾲ"))
      bstack11111111111_opy_ = bstack1lllll1lllll_opy_ + bstack11l1l11l11l_opy_
      response = requests.get(bstack11111111111_opy_)
      data = response.json()
      self.percy_build_id = data.get(bstack11l11ll_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࠨᾳ"), {}).get(bstack11l11ll_opy_ (u"ࠪ࡭ࡩ࠭ᾴ"), None)
      return True
    except:
      self.logger.debug(bstack11l11ll_opy_ (u"ࠦࡊࡸࡲࡰࡴࠣࡳࡨࡩࡵࡳࡴࡨࡨࠥࡽࡨࡪ࡮ࡨࠤࡵࡸ࡯ࡤࡧࡶࡷ࡮ࡴࡧࠡࡪࡨࡥࡱࡺࡨࠡࡥ࡫ࡩࡨࡱࠠࡳࡧࡶࡴࡴࡴࡳࡦࠤ᾵"))
      return False
  def bstack1llllll1l1l1_opy_(self):
    bstack1111111111l_opy_ = bstack11l11ll_opy_ (u"ࠬࡧࡰࡱࠩᾶ") if self.bstack1l1ll1l11_opy_ else bstack11l11ll_opy_ (u"࠭ࡡࡶࡶࡲࡱࡦࡺࡥࠨᾷ")
    bstack1lllll1ll11l_opy_ = bstack11l11ll_opy_ (u"ࠢࡶࡰࡧࡩ࡫࡯࡮ࡦࡦࠥᾸ") if self.config.get(bstack11l11ll_opy_ (u"ࠨࡲࡨࡶࡨࡿࠧᾹ")) is None else True
    bstack11ll111llll_opy_ = bstack11l11ll_opy_ (u"ࠤࡤࡴ࡮࠵ࡡࡱࡲࡢࡴࡪࡸࡣࡺ࠱ࡪࡩࡹࡥࡰࡳࡱ࡭ࡩࡨࡺ࡟ࡵࡱ࡮ࡩࡳࡅ࡮ࡢ࡯ࡨࡁࢀࢃࠦࡵࡻࡳࡩࡂࢁࡽࠧࡲࡨࡶࡨࡿ࠽ࡼࡿࠥᾺ").format(self.config[bstack11l11ll_opy_ (u"ࠪࡴࡷࡵࡪࡦࡥࡷࡒࡦࡳࡥࠨΆ")], bstack1111111111l_opy_, bstack1lllll1ll11l_opy_)
    if self.percy_capture_mode:
      bstack11ll111llll_opy_ += bstack11l11ll_opy_ (u"ࠦࠫࡶࡥࡳࡥࡼࡣࡨࡧࡰࡵࡷࡵࡩࡤࡳ࡯ࡥࡧࡀࡿࢂࠨᾼ").format(self.percy_capture_mode)
    uri = bstack1l11lll1l1_opy_(bstack11ll111llll_opy_)
    try:
      response = bstack1l111lll1_opy_(bstack11l11ll_opy_ (u"ࠬࡍࡅࡕࠩ᾽"), uri, {}, {bstack11l11ll_opy_ (u"࠭ࡡࡶࡶ࡫ࠫι"): (self.config[bstack11l11ll_opy_ (u"ࠧࡶࡵࡨࡶࡓࡧ࡭ࡦࠩ᾿")], self.config[bstack11l11ll_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡌࡧࡼࠫ῀")])})
      if response.status_code == 200:
        data = response.json()
        self.bstack1l1111lll_opy_ = data.get(bstack11l11ll_opy_ (u"ࠩࡶࡹࡨࡩࡥࡴࡵࠪ῁"))
        self.percy_capture_mode = data.get(bstack11l11ll_opy_ (u"ࠪࡴࡪࡸࡣࡺࡡࡦࡥࡵࡺࡵࡳࡧࡢࡱࡴࡪࡥࠨῂ"))
        os.environ[bstack11l11ll_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡔࡊࡘࡃ࡚ࠩῃ")] = str(self.bstack1l1111lll_opy_)
        os.environ[bstack11l11ll_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡕࡋࡒࡄ࡛ࡢࡇࡆࡖࡔࡖࡔࡈࡣࡒࡕࡄࡆࠩῄ")] = str(self.percy_capture_mode)
        if bstack1lllll1ll11l_opy_ == bstack11l11ll_opy_ (u"ࠨࡵ࡯ࡦࡨࡪ࡮ࡴࡥࡥࠤ῅") and str(self.bstack1l1111lll_opy_).lower() == bstack11l11ll_opy_ (u"ࠢࡵࡴࡸࡩࠧῆ"):
          self.bstack11l1lll11_opy_ = True
        if bstack11l11ll_opy_ (u"ࠣࡶࡲ࡯ࡪࡴࠢῇ") in data:
          return data[bstack11l11ll_opy_ (u"ࠤࡷࡳࡰ࡫࡮ࠣῈ")]
        else:
          raise bstack11l11ll_opy_ (u"ࠪࡘࡴࡱࡥ࡯ࠢࡑࡳࡹࠦࡆࡰࡷࡱࡨࠥ࠳ࠠࡼࡿࠪΈ").format(data)
      else:
        raise bstack11l11ll_opy_ (u"ࠦࡋࡧࡩ࡭ࡧࡧࠤࡹࡵࠠࡧࡧࡷࡧ࡭ࠦࡰࡦࡴࡦࡽࠥࡺ࡯࡬ࡧࡱ࠰ࠥࡘࡥࡴࡲࡲࡲࡸ࡫ࠠࡴࡶࡤࡸࡺࡹࠠ࠮ࠢࡾࢁ࠱ࠦࡒࡦࡵࡳࡳࡳࡹࡥࠡࡄࡲࡨࡾࠦ࠭ࠡࡽࢀࠦῊ").format(response.status_code, response.json())
    except Exception as e:
      self.logger.error(bstack11l11ll_opy_ (u"ࠧࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡ࡫ࡱࠤࡨࡸࡥࡢࡶ࡬ࡲ࡬ࠦࡰࡦࡴࡦࡽࠥࡶࡲࡰ࡬ࡨࡧࡹࠨΉ").format(e))
  def bstack1lllll11ll1l_opy_(self):
    bstack1llllllll111_opy_ = os.path.join(tempfile.gettempdir(), bstack11l11ll_opy_ (u"ࠨࡰࡦࡴࡦࡽࡈࡵ࡮ࡧ࡫ࡪ࠲࡯ࡹ࡯࡯ࠤῌ"))
    try:
      if bstack11l11ll_opy_ (u"ࠧࡷࡧࡵࡷ࡮ࡵ࡮ࠨ῍") not in self.bstack1lllll1l11l1_opy_:
        self.bstack1lllll1l11l1_opy_[bstack11l11ll_opy_ (u"ࠨࡸࡨࡶࡸ࡯࡯࡯ࠩ῎")] = 2
      with open(bstack1llllllll111_opy_, bstack11l11ll_opy_ (u"ࠩࡺࠫ῏")) as fp:
        json.dump(self.bstack1lllll1l11l1_opy_, fp)
      return bstack1llllllll111_opy_
    except Exception as e:
      self.logger.error(bstack11l11ll_opy_ (u"࡙ࠥࡳࡧࡢ࡭ࡧࠣࡸࡴࠦࡣࡳࡧࡤࡸࡪࠦࡰࡦࡴࡦࡽࠥࡩ࡯࡯ࡨ࠯ࠤࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡼࡿࠥῐ").format(e))
  def bstack1lllll11ll11_opy_(self, cmd, env = os.environ.copy()):
    try:
      if self.bstack1lllll11llll_opy_ == bstack11l11ll_opy_ (u"ࠫࡼ࡯࡮ࠨῑ"):
        bstack1lllll11l1l1_opy_ = [bstack11l11ll_opy_ (u"ࠬࡩ࡭ࡥ࠰ࡨࡼࡪ࠭ῒ"), bstack11l11ll_opy_ (u"࠭࠯ࡤࠩΐ")]
        cmd = bstack1lllll11l1l1_opy_ + cmd
      cmd = bstack11l11ll_opy_ (u"ࠧࠡࠩ῔").join(cmd)
      self.logger.debug(bstack11l11ll_opy_ (u"ࠣࡔࡸࡲࡳ࡯࡮ࡨࠢࡾࢁࠧ῕").format(cmd))
      with open(self.bstack1lllllllll11_opy_, bstack11l11ll_opy_ (u"ࠤࡤࠦῖ")) as bstack1llllll1llll_opy_:
        process = subprocess.Popen(cmd, shell=True, stdout=bstack1llllll1llll_opy_, text=True, stderr=bstack1llllll1llll_opy_, env=env, universal_newlines=True)
      return process
    except Exception as e:
      self.bstack1lllllll1lll_opy_ = True
      self.logger.error(bstack11l11ll_opy_ (u"ࠥࡊࡦ࡯࡬ࡦࡦࠣࡸࡴࠦࡳࡵࡣࡵࡸࠥࡶࡥࡳࡥࡼࠤࡼ࡯ࡴࡩࠢࡦࡱࡩࠦ࠭ࠡࡽࢀ࠰ࠥࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮࠻ࠢࡾࢁࠧῗ").format(cmd, e))
  def shutdown(self):
    try:
      if self.bstack1llllllll1ll_opy_:
        self.logger.info(bstack11l11ll_opy_ (u"ࠦࡘࡺ࡯ࡱࡲ࡬ࡲ࡬ࠦࡐࡦࡴࡦࡽࠧῘ"))
        cmd = [self.binary_path, bstack11l11ll_opy_ (u"ࠧ࡫ࡸࡦࡥ࠽ࡷࡹࡵࡰࠣῙ")]
        self.bstack1lllll11ll11_opy_(cmd)
        self.bstack1llllllll1ll_opy_ = False
    except Exception as e:
      self.logger.error(bstack11l11ll_opy_ (u"ࠨࡆࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡶࡸࡴࡶࠠࡴࡧࡶࡷ࡮ࡵ࡮ࠡࡹ࡬ࡸ࡭ࠦࡣࡰ࡯ࡰࡥࡳࡪࠠ࠮ࠢࡾࢁ࠱ࠦࡅࡹࡥࡨࡴࡹ࡯࡯࡯࠼ࠣࡿࢂࠨῚ").format(cmd, e))
  def bstack11lll1111_opy_(self):
    if not self.bstack1l1111lll_opy_:
      return
    try:
      bstack1lllllll1l11_opy_ = 0
      while not self.bstack1llllllll1ll_opy_ and bstack1lllllll1l11_opy_ < self.bstack1llllllllll1_opy_:
        if self.bstack1lllllll1lll_opy_:
          self.logger.info(bstack11l11ll_opy_ (u"ࠢࡑࡧࡵࡧࡾࠦࡳࡦࡶࡸࡴࠥ࡬ࡡࡪ࡮ࡨࡨࠧΊ"))
          return
        time.sleep(1)
        bstack1lllllll1l11_opy_ += 1
      os.environ[bstack11l11ll_opy_ (u"ࠨࡒࡈࡖࡈ࡟࡟ࡃࡇࡖࡘࡤࡖࡌࡂࡖࡉࡓࡗࡓࠧ῜")] = str(self.bstack1llllll1l11l_opy_())
      self.logger.info(bstack11l11ll_opy_ (u"ࠤࡓࡩࡷࡩࡹࠡࡵࡨࡸࡺࡶࠠࡤࡱࡰࡴࡱ࡫ࡴࡦࡦࠥ῝"))
    except Exception as e:
      self.logger.error(bstack11l11ll_opy_ (u"࡙ࠥࡳࡧࡢ࡭ࡧࠣࡸࡴࠦࡳࡦࡶࡸࡴࠥࡶࡥࡳࡥࡼ࠰ࠥࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡࡽࢀࠦ῞").format(e))
  def bstack1llllll1l11l_opy_(self):
    if self.bstack1l1ll1l11_opy_:
      return
    try:
      bstack111111111l1_opy_ = [platform[bstack11l11ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡓࡧ࡭ࡦࠩ῟")].lower() for platform in self.config.get(bstack11l11ll_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨῠ"), [])]
      bstack1lllllll1111_opy_ = sys.maxsize
      bstack1lllllll11l1_opy_ = bstack11l11ll_opy_ (u"࠭ࠧῡ")
      for browser in bstack111111111l1_opy_:
        if browser in self.bstack1lllll11lll1_opy_:
          bstack11111111lll_opy_ = self.bstack1lllll11lll1_opy_[browser]
        if bstack11111111lll_opy_ < bstack1lllllll1111_opy_:
          bstack1lllllll1111_opy_ = bstack11111111lll_opy_
          bstack1lllllll11l1_opy_ = browser
      return bstack1lllllll11l1_opy_
    except Exception as e:
      self.logger.error(bstack11l11ll_opy_ (u"ࠢࡖࡰࡤࡦࡱ࡫ࠠࡵࡱࠣࡪ࡮ࡴࡤࠡࡤࡨࡷࡹࠦࡰ࡭ࡣࡷࡪࡴࡸ࡭࠭ࠢࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥࢁࡽࠣῢ").format(e))
  @classmethod
  def bstack1111ll1l11_opy_(self):
    return os.getenv(bstack11l11ll_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡑࡇࡕࡇ࡞࠭ΰ"), bstack11l11ll_opy_ (u"ࠩࡉࡥࡱࡹࡥࠨῤ")).lower()
  @classmethod
  def bstack1ll11llll_opy_(self):
    return os.getenv(bstack11l11ll_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡓࡉࡗࡉ࡙ࡠࡅࡄࡔ࡙࡛ࡒࡆࡡࡐࡓࡉࡋࠧῥ"), bstack11l11ll_opy_ (u"ࠫࠬῦ"))
  @classmethod
  def bstack11lllll111l_opy_(cls, value):
    cls.bstack11l1lll11_opy_ = value
  @classmethod
  def bstack1lllll1l111l_opy_(cls):
    return cls.bstack11l1lll11_opy_
  @classmethod
  def bstack11llll1llll_opy_(cls, value):
    cls.percy_build_id = value
  @classmethod
  def bstack1lllll1l1ll1_opy_(cls):
    return cls.percy_build_id