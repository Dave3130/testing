# coding: UTF-8
import sys
bstack11l111_opy_ = sys.version_info [0] == 2
bstack1l11ll_opy_ = 2048
bstack1l1l11_opy_ = 7
def bstack11l1111_opy_ (bstack111l11l_opy_):
    global bstack1ll1l1l_opy_
    bstack1ll1ll_opy_ = ord (bstack111l11l_opy_ [-1])
    bstack1lll11_opy_ = bstack111l11l_opy_ [:-1]
    bstack111l111_opy_ = bstack1ll1ll_opy_ % len (bstack1lll11_opy_)
    bstack1l1l1ll_opy_ = bstack1lll11_opy_ [:bstack111l111_opy_] + bstack1lll11_opy_ [bstack111l111_opy_:]
    if bstack11l111_opy_:
        bstack1l11_opy_ = unicode () .join ([unichr (ord (char) - bstack1l11ll_opy_ - (bstack1llll_opy_ + bstack1ll1ll_opy_) % bstack1l1l11_opy_) for bstack1llll_opy_, char in enumerate (bstack1l1l1ll_opy_)])
    else:
        bstack1l11_opy_ = str () .join ([chr (ord (char) - bstack1l11ll_opy_ - (bstack1llll_opy_ + bstack1ll1ll_opy_) % bstack1l1l11_opy_) for bstack1llll_opy_, char in enumerate (bstack1l1l1ll_opy_)])
    return eval (bstack1l11_opy_)
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
from bstack_utils.helper import bstack111ll1l111_opy_
from bstack_utils.measure import measure
from bstack_utils.bstack11l1l1ll1l_opy_ import bstack1llll11l11_opy_
class bstack11l1lll111_opy_:
  working_dir = os.getcwd()
  bstack1111l111ll_opy_ = False
  config = {}
  bstack1111llllll1_opy_ = bstack11l1111_opy_ (u"ࠧࠨό")
  binary_path = bstack11l1111_opy_ (u"ࠨࠩὺ")
  bstack1lllllllll11_opy_ = bstack11l1111_opy_ (u"ࠩࠪύ")
  bstack1l111ll11_opy_ = False
  bstack1llllll1ll1l_opy_ = None
  bstack1llllll1l1l1_opy_ = {}
  bstack1llllll1l11l_opy_ = 300
  bstack1lllllll11ll_opy_ = False
  logger = None
  bstack1lllll11ll11_opy_ = False
  bstack11l1l11lll_opy_ = False
  percy_build_id = None
  bstack1llllll1l111_opy_ = bstack11l1111_opy_ (u"ࠪࠫὼ")
  bstack1llllll11l1l_opy_ = {
    bstack11l1111_opy_ (u"ࠫࡨ࡮ࡲࡰ࡯ࡨࠫώ") : 1,
    bstack11l1111_opy_ (u"ࠬ࡬ࡩࡳࡧࡩࡳࡽ࠭὾") : 2,
    bstack11l1111_opy_ (u"࠭ࡥࡥࡩࡨࠫ὿") : 3,
    bstack11l1111_opy_ (u"ࠧࡴࡣࡩࡥࡷ࡯ࠧᾀ") : 4
  }
  def __init__(self) -> None: pass
  def bstack111111111ll_opy_(self):
    bstack1llllll1l1ll_opy_ = bstack11l1111_opy_ (u"ࠨࠩᾁ")
    bstack1lllllll111l_opy_ = sys.platform
    bstack1lllll1lllll_opy_ = bstack11l1111_opy_ (u"ࠩࡳࡩࡷࡩࡹࠨᾂ")
    if re.match(bstack11l1111_opy_ (u"ࠥࡨࡦࡸࡷࡪࡰࡿࡱࡦࡩࠠࡰࡵࠥᾃ"), bstack1lllllll111l_opy_) != None:
      bstack1llllll1l1ll_opy_ = bstack11l1l11l11l_opy_ + bstack11l1111_opy_ (u"ࠦ࠴ࡶࡥࡳࡥࡼ࠱ࡴࡹࡸ࠯ࡼ࡬ࡴࠧᾄ")
      self.bstack1llllll1l111_opy_ = bstack11l1111_opy_ (u"ࠬࡳࡡࡤࠩᾅ")
    elif re.match(bstack11l1111_opy_ (u"ࠨ࡭ࡴࡹ࡬ࡲࢁࡳࡳࡺࡵࡿࡱ࡮ࡴࡧࡸࡾࡦࡽ࡬ࡽࡩ࡯ࡾࡥࡧࡨࡽࡩ࡯ࡾࡺ࡭ࡳࡩࡥࡽࡧࡰࡧࢁࡽࡩ࡯࠵࠵ࠦᾆ"), bstack1lllllll111l_opy_) != None:
      bstack1llllll1l1ll_opy_ = bstack11l1l11l11l_opy_ + bstack11l1111_opy_ (u"ࠢ࠰ࡲࡨࡶࡨࡿ࠭ࡸ࡫ࡱ࠲ࡿ࡯ࡰࠣᾇ")
      bstack1lllll1lllll_opy_ = bstack11l1111_opy_ (u"ࠣࡲࡨࡶࡨࡿ࠮ࡦࡺࡨࠦᾈ")
      self.bstack1llllll1l111_opy_ = bstack11l1111_opy_ (u"ࠩࡺ࡭ࡳ࠭ᾉ")
    else:
      bstack1llllll1l1ll_opy_ = bstack11l1l11l11l_opy_ + bstack11l1111_opy_ (u"ࠥ࠳ࡵ࡫ࡲࡤࡻ࠰ࡰ࡮ࡴࡵࡹ࠰ࡽ࡭ࡵࠨᾊ")
      self.bstack1llllll1l111_opy_ = bstack11l1111_opy_ (u"ࠫࡱ࡯࡮ࡶࡺࠪᾋ")
    return bstack1llllll1l1ll_opy_, bstack1lllll1lllll_opy_
  def bstack1lllll11l11l_opy_(self):
    try:
      bstack111111111l1_opy_ = [os.path.join(expanduser(bstack11l1111_opy_ (u"ࠧࢄࠢᾌ")), bstack11l1111_opy_ (u"࠭࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠭ᾍ")), self.working_dir, tempfile.gettempdir()]
      for path in bstack111111111l1_opy_:
        if(self.bstack1lllll1ll111_opy_(path)):
          return path
      raise bstack11l1111_opy_ (u"ࠢࡖࡰࡤࡦࡱ࡫ࠠࡵࡱࠣࡨࡴࡽ࡮࡭ࡱࡤࡨࠥࡶࡥࡳࡥࡼࠤࡧ࡯࡮ࡢࡴࡼࠦᾎ")
    except Exception as e:
      self.logger.error(bstack11l1111_opy_ (u"ࠣࡈࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤ࡫࡯࡮ࡥࠢࡤࡺࡦ࡯࡬ࡢࡤ࡯ࡩࠥࡶࡡࡵࡪࠣࡪࡴࡸࠠࡱࡧࡵࡧࡾࠦࡤࡰࡹࡱࡰࡴࡧࡤ࠭ࠢࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࠳ࠠࡼࡿࠥᾏ").format(e))
  def bstack1lllll1ll111_opy_(self, path):
    try:
      if not os.path.exists(path):
        os.makedirs(path)
      return True
    except:
      return False
  def bstack1lllll1ll1ll_opy_(self, bstack1lllll11l1ll_opy_):
    return os.path.join(bstack1lllll11l1ll_opy_, self.bstack1111llllll1_opy_ + bstack11l1111_opy_ (u"ࠤ࠱ࡩࡹࡧࡧࠣᾐ"))
  def bstack1lllll11llll_opy_(self, bstack1lllll11l1ll_opy_, bstack11111111l1l_opy_):
    if not bstack11111111l1l_opy_: return
    try:
      bstack1lllll11l111_opy_ = self.bstack1lllll1ll1ll_opy_(bstack1lllll11l1ll_opy_)
      with open(bstack1lllll11l111_opy_, bstack11l1111_opy_ (u"ࠥࡻࠧᾑ")) as f:
        f.write(bstack11111111l1l_opy_)
        self.logger.debug(bstack11l1111_opy_ (u"ࠦࡘࡧࡶࡦࡦࠣࡲࡪࡽࠠࡆࡖࡤ࡫ࠥ࡬࡯ࡳࠢࡳࡩࡷࡩࡹࠣᾒ"))
    except Exception as e:
      self.logger.error(bstack11l1111_opy_ (u"࡛ࠧ࡮ࡢࡤ࡯ࡩࠥࡺ࡯ࠡࡵࡤࡺࡪࠦࡴࡩࡧࠣࡩࡹࡧࡧ࠭ࠢࡨࡶࡷࡵࡲ࠻ࠢࡾࢁࠧᾓ").format(e))
  def bstack1lllll1llll1_opy_(self, bstack1lllll11l1ll_opy_):
    try:
      bstack1lllll11l111_opy_ = self.bstack1lllll1ll1ll_opy_(bstack1lllll11l1ll_opy_)
      if os.path.exists(bstack1lllll11l111_opy_):
        with open(bstack1lllll11l111_opy_, bstack11l1111_opy_ (u"ࠨࡲࠣᾔ")) as f:
          bstack11111111l1l_opy_ = f.read().strip()
          return bstack11111111l1l_opy_ if bstack11111111l1l_opy_ else None
    except Exception as e:
      self.logger.error(bstack11l1111_opy_ (u"ࠢࡇࡣ࡬ࡰࡪࡪࠠ࡭ࡱࡤࡨ࡮ࡴࡧࠡࡇࡗࡥ࡬࠲ࠠࡦࡴࡵࡳࡷࡀࠠࡼࡿࠥᾕ").format(e))
  def bstack1llllllll1l1_opy_(self, bstack1lllll11l1ll_opy_, bstack1llllll1l1ll_opy_):
    bstack1llllllllll1_opy_ = self.bstack1lllll1llll1_opy_(bstack1lllll11l1ll_opy_)
    if bstack1llllllllll1_opy_:
      try:
        bstack1lllll1l1ll1_opy_ = self.bstack1lllllllllll_opy_(bstack1llllllllll1_opy_, bstack1llllll1l1ll_opy_)
        if not bstack1lllll1l1ll1_opy_:
          self.logger.debug(bstack11l1111_opy_ (u"ࠣࡒࡨࡶࡨࡿࠠࡣ࡫ࡱࡥࡷࡿࠠࡪࡵࠣࡹࡵࠦࡴࡰࠢࡧࡥࡹ࡫ࠠࠩࡇࡗࡥ࡬ࠦࡵ࡯ࡥ࡫ࡥࡳ࡭ࡥࡥࠫࠥᾖ"))
          return True
        self.logger.debug(bstack11l1111_opy_ (u"ࠤࡑࡩࡼࠦࡐࡦࡴࡦࡽࠥࡨࡩ࡯ࡣࡵࡽࠥࡼࡥࡳࡵ࡬ࡳࡳࠦࡡࡷࡣ࡬ࡰࡦࡨ࡬ࡦ࠮ࠣࡨࡴࡽ࡮࡭ࡱࡤࡨ࡮ࡴࡧࠡࡷࡳࡨࡦࡺࡥࠣᾗ"))
        return False
      except Exception as e:
        self.logger.warn(bstack11l1111_opy_ (u"ࠥࡊࡦ࡯࡬ࡦࡦࠣࡸࡴࠦࡣࡩࡧࡦ࡯ࠥ࡬࡯ࡳࠢࡥ࡭ࡳࡧࡲࡺࠢࡸࡴࡩࡧࡴࡦࡵ࠯ࠤࡺࡹࡩ࡯ࡩࠣࡩࡽ࡯ࡳࡵ࡫ࡱ࡫ࠥࡨࡩ࡯ࡣࡵࡽ࠿ࠦࡻࡾࠤᾘ").format(e))
    return False
  def bstack1lllllllllll_opy_(self, bstack1llllllllll1_opy_, bstack1llllll1l1ll_opy_):
    try:
      headers = {
        bstack11l1111_opy_ (u"ࠦࡎ࡬࠭ࡏࡱࡱࡩ࠲ࡓࡡࡵࡥ࡫ࠦᾙ"): bstack1llllllllll1_opy_
      }
      response = bstack111ll1l111_opy_(bstack11l1111_opy_ (u"ࠬࡍࡅࡕࠩᾚ"), bstack1llllll1l1ll_opy_, {}, {bstack11l1111_opy_ (u"ࠨࡨࡦࡣࡧࡩࡷࡹࠢᾛ"): headers})
      if response.status_code == 304:
        return False
      return True
    except Exception as e:
      raise(bstack11l1111_opy_ (u"ࠢࡆࡴࡵࡳࡷࠦࡣࡩࡧࡦ࡯࡮ࡴࡧࠡࡨࡲࡶࠥࡖࡥࡳࡥࡼࠤࡧ࡯࡮ࡢࡴࡼࠤࡺࡶࡤࡢࡶࡨࡷ࠿ࠦࡻࡾࠤᾜ").format(e))
  @measure(event_name=EVENTS.bstack11l1l1111ll_opy_, stage=STAGE.bstack1111ll111_opy_)
  def bstack1llllll11l11_opy_(self, bstack1llllll1l1ll_opy_, bstack1lllll1lllll_opy_):
    try:
      bstack1111111111l_opy_ = self.bstack1lllll11l11l_opy_()
      bstack1lllllll1lll_opy_ = os.path.join(bstack1111111111l_opy_, bstack11l1111_opy_ (u"ࠨࡲࡨࡶࡨࡿ࠮ࡻ࡫ࡳࠫᾝ"))
      bstack1lllll1l11ll_opy_ = os.path.join(bstack1111111111l_opy_, bstack1lllll1lllll_opy_)
      if self.bstack1llllllll1l1_opy_(bstack1111111111l_opy_, bstack1llllll1l1ll_opy_): # if bstack1lllll111lll_opy_, bstack1lllll1l1ll_opy_ bstack11111111l1l_opy_ is bstack1lllll1l111l_opy_ to bstack111l1l11l1l_opy_ version available (response 304)
        if os.path.exists(bstack1lllll1l11ll_opy_):
          self.logger.info(bstack11l1111_opy_ (u"ࠤࡓࡩࡷࡩࡹࠡࡤ࡬ࡲࡦࡸࡹࠡࡨࡲࡹࡳࡪࠠࡪࡰࠣࡿࢂ࠲ࠠࡴ࡭࡬ࡴࡵ࡯࡮ࡨࠢࡧࡳࡼࡴ࡬ࡰࡣࡧࠦᾞ").format(bstack1lllll1l11ll_opy_))
          return bstack1lllll1l11ll_opy_
        if os.path.exists(bstack1lllllll1lll_opy_):
          self.logger.info(bstack11l1111_opy_ (u"ࠥࡔࡪࡸࡣࡺࠢࡽ࡭ࡵࠦࡦࡰࡷࡱࡨࠥ࡯࡮ࠡࡽࢀ࠰ࠥࡻ࡮ࡻ࡫ࡳࡴ࡮ࡴࡧࠣᾟ").format(bstack1lllllll1lll_opy_))
          return self.bstack1lllll1lll11_opy_(bstack1lllllll1lll_opy_, bstack1lllll1lllll_opy_)
      self.logger.info(bstack11l1111_opy_ (u"ࠦࡉࡵࡷ࡯࡮ࡲࡥࡩ࡯࡮ࡨࠢࡳࡩࡷࡩࡹࠡࡤ࡬ࡲࡦࡸࡹࠡࡨࡵࡳࡲࠦࡻࡾࠤᾠ").format(bstack1llllll1l1ll_opy_))
      response = bstack111ll1l111_opy_(bstack11l1111_opy_ (u"ࠬࡍࡅࡕࠩᾡ"), bstack1llllll1l1ll_opy_, {}, {})
      if response.status_code == 200:
        bstack1llllll11lll_opy_ = response.headers.get(bstack11l1111_opy_ (u"ࠨࡅࡕࡣࡪࠦᾢ"), bstack11l1111_opy_ (u"ࠢࠣᾣ"))
        if bstack1llllll11lll_opy_:
          self.bstack1lllll11llll_opy_(bstack1111111111l_opy_, bstack1llllll11lll_opy_)
        with open(bstack1lllllll1lll_opy_, bstack11l1111_opy_ (u"ࠨࡹࡥࠫᾤ")) as file:
          file.write(response.content)
        self.logger.info(bstack11l1111_opy_ (u"ࠤࡇࡳࡼࡴ࡬ࡰࡣࡧࡩࡩࠦࡰࡦࡴࡦࡽࠥࡨࡩ࡯ࡣࡵࡽࠥࡧ࡮ࡥࠢࡶࡥࡻ࡫ࡤࠡࡣࡷࠤࢀࢃࠢᾥ").format(bstack1lllllll1lll_opy_))
        return self.bstack1lllll1lll11_opy_(bstack1lllllll1lll_opy_, bstack1lllll1lllll_opy_)
      else:
        raise(bstack11l1111_opy_ (u"ࠥࡊࡦ࡯࡬ࡦࡦࠣࡸࡴࠦࡤࡰࡹࡱࡰࡴࡧࡤࠡࡶ࡫ࡩࠥ࡬ࡩ࡭ࡧ࠱ࠤࡘࡺࡡࡵࡷࡶࠤࡨࡵࡤࡦ࠼ࠣࡿࢂࠨᾦ").format(response.status_code))
    except Exception as e:
      self.logger.error(bstack11l1111_opy_ (u"࡚ࠦࡴࡡࡣ࡮ࡨࠤࡹࡵࠠࡥࡱࡺࡲࡱࡵࡡࡥࠢࡳࡩࡷࡩࡹࠡࡤ࡬ࡲࡦࡸࡹ࠻ࠢࡾࢁࠧᾧ").format(e))
  def bstack1llllllll11l_opy_(self, bstack1llllll1l1ll_opy_, bstack1lllll1lllll_opy_):
    try:
      retry = 2
      bstack1lllll1l11ll_opy_ = None
      bstack1llllll1lll1_opy_ = False
      while retry > 0:
        bstack1lllll1l11ll_opy_ = self.bstack1llllll11l11_opy_(bstack1llllll1l1ll_opy_, bstack1lllll1lllll_opy_)
        bstack1llllll1lll1_opy_ = self.bstack1lllll1l1lll_opy_(bstack1llllll1l1ll_opy_, bstack1lllll1lllll_opy_, bstack1lllll1l11ll_opy_)
        if bstack1llllll1lll1_opy_:
          break
        retry -= 1
      return bstack1lllll1l11ll_opy_, bstack1llllll1lll1_opy_
    except Exception as e:
      self.logger.error(bstack11l1111_opy_ (u"࡛ࠧ࡮ࡢࡤ࡯ࡩࠥࡺ࡯ࠡࡩࡨࡸࠥࡶࡥࡳࡥࡼࠤࡧ࡯࡮ࡢࡴࡼࠤࡵࡧࡴࡩࠤᾨ").format(e))
    return bstack1lllll1l11ll_opy_, False
  def bstack1lllll1l1lll_opy_(self, bstack1llllll1l1ll_opy_, bstack1lllll1lllll_opy_, bstack1lllll1l11ll_opy_, bstack1llllll111l1_opy_ = 0):
    if bstack1llllll111l1_opy_ > 1:
      return False
    if bstack1lllll1l11ll_opy_ == None or os.path.exists(bstack1lllll1l11ll_opy_) == False:
      self.logger.warn(bstack11l1111_opy_ (u"ࠨࡐࡦࡴࡦࡽࠥࡶࡡࡵࡪࠣࡲࡴࡺࠠࡧࡱࡸࡲࡩ࠲ࠠࡳࡧࡷࡶࡾ࡯࡮ࡨࠢࡧࡳࡼࡴ࡬ࡰࡣࡧࠦᾩ"))
      return False
    bstack1lllllllll1l_opy_ = bstack11l1111_opy_ (u"ࡲࠣࡠ࠱࠮ࡅࡶࡥࡳࡥࡼ࠳ࡨࡲࡩࠡ࡞ࡧ࠯ࡡ࠴࡜ࡥ࠭࡟࠲ࡡࡪࠫࠣᾪ")
    command = bstack11l1111_opy_ (u"ࠨࡽࢀࠤ࠲࠳ࡶࡦࡴࡶ࡭ࡴࡴࠧᾫ").format(bstack1lllll1l11ll_opy_)
    bstack1llllll111ll_opy_ = subprocess.check_output(command, shell=True, text=True)
    if re.match(bstack1lllllllll1l_opy_, bstack1llllll111ll_opy_) != None:
      return True
    else:
      self.logger.error(bstack11l1111_opy_ (u"ࠤࡓࡩࡷࡩࡹࠡࡸࡨࡶࡸ࡯࡯࡯ࠢࡦ࡬ࡪࡩ࡫ࠡࡨࡤ࡭ࡱ࡫ࡤࠣᾬ"))
      return False
  def bstack1lllll1lll11_opy_(self, bstack1lllllll1lll_opy_, bstack1lllll1lllll_opy_):
    try:
      working_dir = os.path.dirname(bstack1lllllll1lll_opy_)
      shutil.unpack_archive(bstack1lllllll1lll_opy_, working_dir)
      bstack1lllll1l11ll_opy_ = os.path.join(working_dir, bstack1lllll1lllll_opy_)
      os.chmod(bstack1lllll1l11ll_opy_, 0o755)
      return bstack1lllll1l11ll_opy_
    except Exception as e:
      self.logger.error(bstack11l1111_opy_ (u"࡙ࠥࡳࡧࡢ࡭ࡧࠣࡸࡴࠦࡵ࡯ࡼ࡬ࡴࠥࡶࡥࡳࡥࡼࠤࡧ࡯࡮ࡢࡴࡼࠦᾭ"))
  def bstack1lllll1l11l1_opy_(self):
    try:
      bstack1lllll1lll1l_opy_ = self.config.get(bstack11l1111_opy_ (u"ࠫࡵ࡫ࡲࡤࡻࠪᾮ"))
      bstack1lllll1l11l1_opy_ = bstack1lllll1lll1l_opy_ or (bstack1lllll1lll1l_opy_ is None and self.bstack1111l111ll_opy_)
      if not bstack1lllll1l11l1_opy_ or self.config.get(bstack11l1111_opy_ (u"ࠬ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࠨᾯ"), None) not in bstack11l11l11ll1_opy_:
        return False
      self.bstack1l111ll11_opy_ = True
      return True
    except Exception as e:
      self.logger.error(bstack11l1111_opy_ (u"ࠨࡕ࡯ࡣࡥࡰࡪࠦࡴࡰࠢࡧࡩࡹ࡫ࡣࡵࠢࡳࡩࡷࡩࡹ࠭ࠢࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥࢁࡽࠣᾰ").format(e))
  def bstack1lllll11l1l1_opy_(self):
    try:
      bstack1lllll11l1l1_opy_ = self.percy_capture_mode
      return bstack1lllll11l1l1_opy_
    except Exception as e:
      self.logger.error(bstack11l1111_opy_ (u"ࠢࡖࡰࡤࡦࡱ࡫ࠠࡵࡱࠣࡨࡪࡺࡥࡤࡶࠣࡴࡪࡸࡣࡺࠢࡦࡥࡵࡺࡵࡳࡧࠣࡱࡴࡪࡥ࠭ࠢࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥࢁࡽࠣᾱ").format(e))
  def init(self, bstack1111l111ll_opy_, config, logger):
    self.bstack1111l111ll_opy_ = bstack1111l111ll_opy_
    self.config = config
    self.logger = logger
    if not self.bstack1lllll1l11l1_opy_():
      return
    self.bstack1llllll1l1l1_opy_ = config.get(bstack11l1111_opy_ (u"ࠨࡲࡨࡶࡨࡿࡏࡱࡶ࡬ࡳࡳࡹࠧᾲ"), {})
    self.percy_capture_mode = config.get(bstack11l1111_opy_ (u"ࠩࡳࡩࡷࡩࡹࡄࡣࡳࡸࡺࡸࡥࡎࡱࡧࡩࠬᾳ"))
    try:
      bstack1llllll1l1ll_opy_, bstack1lllll1lllll_opy_ = self.bstack111111111ll_opy_()
      self.bstack1111llllll1_opy_ = bstack1lllll1lllll_opy_
      bstack1lllll1l11ll_opy_, bstack1llllll1lll1_opy_ = self.bstack1llllllll11l_opy_(bstack1llllll1l1ll_opy_, bstack1lllll1lllll_opy_)
      if bstack1llllll1lll1_opy_:
        self.binary_path = bstack1lllll1l11ll_opy_
        thread = Thread(target=self.bstack1llllll11ll1_opy_)
        thread.start()
      else:
        self.bstack1lllll11ll11_opy_ = True
        self.logger.error(bstack11l1111_opy_ (u"ࠥࡍࡳࡼࡡ࡭࡫ࡧࠤࡵ࡫ࡲࡤࡻࠣࡴࡦࡺࡨࠡࡨࡲࡹࡳࡪࠠ࠮ࠢࡾࢁ࠱ࠦࡕ࡯ࡣࡥࡰࡪࠦࡴࡰࠢࡶࡸࡦࡸࡴࠡࡒࡨࡶࡨࡿࠢᾴ").format(bstack1lllll1l11ll_opy_))
    except Exception as e:
      self.logger.error(bstack11l1111_opy_ (u"࡚ࠦࡴࡡࡣ࡮ࡨࠤࡹࡵࠠࡴࡶࡤࡶࡹࠦࡰࡦࡴࡦࡽ࠱ࠦࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢࡾࢁࠧ᾵").format(e))
  def bstack1lllll111ll1_opy_(self):
    try:
      logfile = os.path.join(self.working_dir, bstack11l1111_opy_ (u"ࠬࡲ࡯ࡨࠩᾶ"), bstack11l1111_opy_ (u"࠭ࡰࡦࡴࡦࡽ࠳ࡲ࡯ࡨࠩᾷ"))
      os.makedirs(os.path.dirname(logfile)) if not os.path.exists(os.path.dirname(logfile)) else None
      self.logger.debug(bstack11l1111_opy_ (u"ࠢࡑࡷࡶ࡬࡮ࡴࡧࠡࡲࡨࡶࡨࡿࠠ࡭ࡱࡪࡷࠥࡧࡴࠡࡽࢀࠦᾸ").format(logfile))
      self.bstack1lllllllll11_opy_ = logfile
    except Exception as e:
      self.logger.error(bstack11l1111_opy_ (u"ࠣࡗࡱࡥࡧࡲࡥࠡࡶࡲࠤࡸ࡫ࡴࠡࡲࡨࡶࡨࡿࠠ࡭ࡱࡪࠤࡵࡧࡴࡩ࠮ࠣࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡻࡾࠤᾹ").format(e))
  @measure(event_name=EVENTS.bstack11l11llll1l_opy_, stage=STAGE.bstack1111ll111_opy_)
  def bstack1llllll11ll1_opy_(self):
    bstack1lllllll1l11_opy_ = self.bstack1lllll1l1l1l_opy_()
    if bstack1lllllll1l11_opy_ == None:
      self.bstack1lllll11ll11_opy_ = True
      self.logger.error(bstack11l1111_opy_ (u"ࠤࡓࡩࡷࡩࡹࠡࡶࡲ࡯ࡪࡴࠠ࡯ࡱࡷࠤ࡫ࡵࡵ࡯ࡦ࠯ࠤࡋࡧࡩ࡭ࡧࡧࠤࡹࡵࠠࡴࡶࡤࡶࡹࠦࡰࡦࡴࡦࡽࠧᾺ"))
      return False
    bstack1llllll1111l_opy_ = [bstack11l1111_opy_ (u"ࠥࡥࡵࡶ࠺ࡦࡺࡨࡧ࠿ࡹࡴࡢࡴࡷࠦΆ") if self.bstack1111l111ll_opy_ else bstack11l1111_opy_ (u"ࠫࡪࡾࡥࡤ࠼ࡶࡸࡦࡸࡴࠨᾼ")]
    bstack11111l11l1l_opy_ = self.bstack1lllllll1111_opy_()
    if bstack11111l11l1l_opy_ != None:
      bstack1llllll1111l_opy_.append(bstack11l1111_opy_ (u"ࠧ࠳ࡣࠡࡽࢀࠦ᾽").format(bstack11111l11l1l_opy_))
    env = os.environ.copy()
    env[bstack11l1111_opy_ (u"ࠨࡐࡆࡔࡆ࡝ࡤ࡚ࡏࡌࡇࡑࠦι")] = bstack1lllllll1l11_opy_
    env[bstack11l1111_opy_ (u"ࠢࡕࡊࡢࡆ࡚ࡏࡌࡅࡡࡘ࡙ࡎࡊࠢ᾿")] = os.environ.get(bstack11l1111_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡍ࡛ࡂࡠࡗࡘࡍࡉ࠭῀"), bstack11l1111_opy_ (u"ࠩࠪ῁"))
    bstack1lllllll1ll1_opy_ = [self.binary_path]
    self.bstack1lllll111ll1_opy_()
    self.bstack1llllll1ll1l_opy_ = self.bstack1lllll1ll1l1_opy_(bstack1lllllll1ll1_opy_ + bstack1llllll1111l_opy_, env)
    self.logger.debug(bstack11l1111_opy_ (u"ࠥࡗࡹࡧࡲࡵ࡫ࡱ࡫ࠥࡎࡥࡢ࡮ࡷ࡬ࠥࡉࡨࡦࡥ࡮ࠦῂ"))
    bstack1llllll111l1_opy_ = 0
    while self.bstack1llllll1ll1l_opy_.poll() == None:
      bstack1lllll1111ll_opy_ = self.bstack1llllll1llll_opy_()
      if bstack1lllll1111ll_opy_:
        self.logger.debug(bstack11l1111_opy_ (u"ࠦࡍ࡫ࡡ࡭ࡶ࡫ࠤࡈ࡮ࡥࡤ࡭ࠣࡷࡺࡩࡣࡦࡵࡶࡪࡺࡲࠢῃ"))
        self.bstack1lllllll11ll_opy_ = True
        return True
      bstack1llllll111l1_opy_ += 1
      self.logger.debug(bstack11l1111_opy_ (u"ࠧࡎࡥࡢ࡮ࡷ࡬ࠥࡉࡨࡦࡥ࡮ࠤࡗ࡫ࡴࡳࡻࠣ࠱ࠥࢁࡽࠣῄ").format(bstack1llllll111l1_opy_))
      time.sleep(2)
    self.logger.error(bstack11l1111_opy_ (u"ࠨࡆࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡶࡸࡦࡸࡴࠡࡲࡨࡶࡨࡿࠬࠡࡊࡨࡥࡱࡺࡨࠡࡅ࡫ࡩࡨࡱࠠࡇࡣ࡬ࡰࡪࡪࠠࡢࡨࡷࡩࡷࠦࡻࡾࠢࡤࡸࡹ࡫࡭ࡱࡶࡶࠦ῅").format(bstack1llllll111l1_opy_))
    self.bstack1lllll11ll11_opy_ = True
    return False
  def bstack1llllll1llll_opy_(self, bstack1llllll111l1_opy_ = 0):
    if bstack1llllll111l1_opy_ > 10:
      return False
    try:
      bstack11111111111_opy_ = os.environ.get(bstack11l1111_opy_ (u"ࠧࡑࡇࡕࡇ࡞ࡥࡓࡆࡔ࡙ࡉࡗࡥࡁࡅࡆࡕࡉࡘ࡙ࠧῆ"), bstack11l1111_opy_ (u"ࠨࡪࡷࡸࡵࡀ࠯࠰࡮ࡲࡧࡦࡲࡨࡰࡵࡷ࠾࠺࠹࠳࠹ࠩῇ"))
      bstack1lllll1l1l11_opy_ = bstack11111111111_opy_ + bstack11l11l1l11l_opy_
      response = requests.get(bstack1lllll1l1l11_opy_)
      data = response.json()
      self.percy_build_id = data.get(bstack11l1111_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࠨῈ"), {}).get(bstack11l1111_opy_ (u"ࠪ࡭ࡩ࠭Έ"), None)
      return True
    except:
      self.logger.debug(bstack11l1111_opy_ (u"ࠦࡊࡸࡲࡰࡴࠣࡳࡨࡩࡵࡳࡴࡨࡨࠥࡽࡨࡪ࡮ࡨࠤࡵࡸ࡯ࡤࡧࡶࡷ࡮ࡴࡧࠡࡪࡨࡥࡱࡺࡨࠡࡥ࡫ࡩࡨࡱࠠࡳࡧࡶࡴࡴࡴࡳࡦࠤῊ"))
      return False
  def bstack1lllll1l1l1l_opy_(self):
    bstack1lllll1l1111_opy_ = bstack11l1111_opy_ (u"ࠬࡧࡰࡱࠩΉ") if self.bstack1111l111ll_opy_ else bstack11l1111_opy_ (u"࠭ࡡࡶࡶࡲࡱࡦࡺࡥࠨῌ")
    bstack1llllllll111_opy_ = bstack11l1111_opy_ (u"ࠢࡶࡰࡧࡩ࡫࡯࡮ࡦࡦࠥ῍") if self.config.get(bstack11l1111_opy_ (u"ࠨࡲࡨࡶࡨࡿࠧ῎")) is None else True
    bstack11ll111l111_opy_ = bstack11l1111_opy_ (u"ࠤࡤࡴ࡮࠵ࡡࡱࡲࡢࡴࡪࡸࡣࡺ࠱ࡪࡩࡹࡥࡰࡳࡱ࡭ࡩࡨࡺ࡟ࡵࡱ࡮ࡩࡳࡅ࡮ࡢ࡯ࡨࡁࢀࢃࠦࡵࡻࡳࡩࡂࢁࡽࠧࡲࡨࡶࡨࡿ࠽ࡼࡿࠥ῏").format(self.config[bstack11l1111_opy_ (u"ࠪࡴࡷࡵࡪࡦࡥࡷࡒࡦࡳࡥࠨῐ")], bstack1lllll1l1111_opy_, bstack1llllllll111_opy_)
    if self.percy_capture_mode:
      bstack11ll111l111_opy_ += bstack11l1111_opy_ (u"ࠦࠫࡶࡥࡳࡥࡼࡣࡨࡧࡰࡵࡷࡵࡩࡤࡳ࡯ࡥࡧࡀࡿࢂࠨῑ").format(self.percy_capture_mode)
    uri = bstack1llll11l11_opy_(bstack11ll111l111_opy_)
    try:
      response = bstack111ll1l111_opy_(bstack11l1111_opy_ (u"ࠬࡍࡅࡕࠩῒ"), uri, {}, {bstack11l1111_opy_ (u"࠭ࡡࡶࡶ࡫ࠫΐ"): (self.config[bstack11l1111_opy_ (u"ࠧࡶࡵࡨࡶࡓࡧ࡭ࡦࠩ῔")], self.config[bstack11l1111_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡌࡧࡼࠫ῕")])})
      if response.status_code == 200:
        data = response.json()
        self.bstack1l111ll11_opy_ = data.get(bstack11l1111_opy_ (u"ࠩࡶࡹࡨࡩࡥࡴࡵࠪῖ"))
        self.percy_capture_mode = data.get(bstack11l1111_opy_ (u"ࠪࡴࡪࡸࡣࡺࡡࡦࡥࡵࡺࡵࡳࡧࡢࡱࡴࡪࡥࠨῗ"))
        os.environ[bstack11l1111_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡔࡊࡘࡃ࡚ࠩῘ")] = str(self.bstack1l111ll11_opy_)
        os.environ[bstack11l1111_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡕࡋࡒࡄ࡛ࡢࡇࡆࡖࡔࡖࡔࡈࡣࡒࡕࡄࡆࠩῙ")] = str(self.percy_capture_mode)
        if bstack1llllllll111_opy_ == bstack11l1111_opy_ (u"ࠨࡵ࡯ࡦࡨࡪ࡮ࡴࡥࡥࠤῚ") and str(self.bstack1l111ll11_opy_).lower() == bstack11l1111_opy_ (u"ࠢࡵࡴࡸࡩࠧΊ"):
          self.bstack11l1l11lll_opy_ = True
        if bstack11l1111_opy_ (u"ࠣࡶࡲ࡯ࡪࡴࠢ῜") in data:
          return data[bstack11l1111_opy_ (u"ࠤࡷࡳࡰ࡫࡮ࠣ῝")]
        else:
          raise bstack11l1111_opy_ (u"ࠪࡘࡴࡱࡥ࡯ࠢࡑࡳࡹࠦࡆࡰࡷࡱࡨࠥ࠳ࠠࡼࡿࠪ῞").format(data)
      else:
        raise bstack11l1111_opy_ (u"ࠦࡋࡧࡩ࡭ࡧࡧࠤࡹࡵࠠࡧࡧࡷࡧ࡭ࠦࡰࡦࡴࡦࡽࠥࡺ࡯࡬ࡧࡱ࠰ࠥࡘࡥࡴࡲࡲࡲࡸ࡫ࠠࡴࡶࡤࡸࡺࡹࠠ࠮ࠢࡾࢁ࠱ࠦࡒࡦࡵࡳࡳࡳࡹࡥࠡࡄࡲࡨࡾࠦ࠭ࠡࡽࢀࠦ῟").format(response.status_code, response.json())
    except Exception as e:
      self.logger.error(bstack11l1111_opy_ (u"ࠧࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡ࡫ࡱࠤࡨࡸࡥࡢࡶ࡬ࡲ࡬ࠦࡰࡦࡴࡦࡽࠥࡶࡲࡰ࡬ࡨࡧࡹࠨῠ").format(e))
  def bstack1lllllll1111_opy_(self):
    bstack1lllll111l1l_opy_ = os.path.join(tempfile.gettempdir(), bstack11l1111_opy_ (u"ࠨࡰࡦࡴࡦࡽࡈࡵ࡮ࡧ࡫ࡪ࠲࡯ࡹ࡯࡯ࠤῡ"))
    try:
      if bstack11l1111_opy_ (u"ࠧࡷࡧࡵࡷ࡮ࡵ࡮ࠨῢ") not in self.bstack1llllll1l1l1_opy_:
        self.bstack1llllll1l1l1_opy_[bstack11l1111_opy_ (u"ࠨࡸࡨࡶࡸ࡯࡯࡯ࠩΰ")] = 2
      with open(bstack1lllll111l1l_opy_, bstack11l1111_opy_ (u"ࠩࡺࠫῤ")) as fp:
        json.dump(self.bstack1llllll1l1l1_opy_, fp)
      return bstack1lllll111l1l_opy_
    except Exception as e:
      self.logger.error(bstack11l1111_opy_ (u"࡙ࠥࡳࡧࡢ࡭ࡧࠣࡸࡴࠦࡣࡳࡧࡤࡸࡪࠦࡰࡦࡴࡦࡽࠥࡩ࡯࡯ࡨ࠯ࠤࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡼࡿࠥῥ").format(e))
  def bstack1lllll1ll1l1_opy_(self, cmd, env = os.environ.copy()):
    try:
      if self.bstack1llllll1l111_opy_ == bstack11l1111_opy_ (u"ࠫࡼ࡯࡮ࠨῦ"):
        bstack1llllllll1ll_opy_ = [bstack11l1111_opy_ (u"ࠬࡩ࡭ࡥ࠰ࡨࡼࡪ࠭ῧ"), bstack11l1111_opy_ (u"࠭࠯ࡤࠩῨ")]
        cmd = bstack1llllllll1ll_opy_ + cmd
      cmd = bstack11l1111_opy_ (u"ࠧࠡࠩῩ").join(cmd)
      self.logger.debug(bstack11l1111_opy_ (u"ࠣࡔࡸࡲࡳ࡯࡮ࡨࠢࡾࢁࠧῪ").format(cmd))
      with open(self.bstack1lllllllll11_opy_, bstack11l1111_opy_ (u"ࠤࡤࠦΎ")) as bstack11111111l11_opy_:
        process = subprocess.Popen(cmd, shell=True, stdout=bstack11111111l11_opy_, text=True, stderr=bstack11111111l11_opy_, env=env, universal_newlines=True)
      return process
    except Exception as e:
      self.bstack1lllll11ll11_opy_ = True
      self.logger.error(bstack11l1111_opy_ (u"ࠥࡊࡦ࡯࡬ࡦࡦࠣࡸࡴࠦࡳࡵࡣࡵࡸࠥࡶࡥࡳࡥࡼࠤࡼ࡯ࡴࡩࠢࡦࡱࡩࠦ࠭ࠡࡽࢀ࠰ࠥࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮࠻ࠢࡾࢁࠧῬ").format(cmd, e))
  def shutdown(self):
    try:
      if self.bstack1lllllll11ll_opy_:
        self.logger.info(bstack11l1111_opy_ (u"ࠦࡘࡺ࡯ࡱࡲ࡬ࡲ࡬ࠦࡐࡦࡴࡦࡽࠧ῭"))
        cmd = [self.binary_path, bstack11l1111_opy_ (u"ࠧ࡫ࡸࡦࡥ࠽ࡷࡹࡵࡰࠣ΅")]
        self.bstack1lllll1ll1l1_opy_(cmd)
        self.bstack1lllllll11ll_opy_ = False
    except Exception as e:
      self.logger.error(bstack11l1111_opy_ (u"ࠨࡆࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡶࡸࡴࡶࠠࡴࡧࡶࡷ࡮ࡵ࡮ࠡࡹ࡬ࡸ࡭ࠦࡣࡰ࡯ࡰࡥࡳࡪࠠ࠮ࠢࡾࢁ࠱ࠦࡅࡹࡥࡨࡴࡹ࡯࡯࡯࠼ࠣࡿࢂࠨ`").format(cmd, e))
  def bstack1ll1l11l11_opy_(self):
    if not self.bstack1l111ll11_opy_:
      return
    try:
      bstack1llllll1ll11_opy_ = 0
      while not self.bstack1lllllll11ll_opy_ and bstack1llllll1ll11_opy_ < self.bstack1llllll1l11l_opy_:
        if self.bstack1lllll11ll11_opy_:
          self.logger.info(bstack11l1111_opy_ (u"ࠢࡑࡧࡵࡧࡾࠦࡳࡦࡶࡸࡴࠥ࡬ࡡࡪ࡮ࡨࡨࠧ῰"))
          return
        time.sleep(1)
        bstack1llllll1ll11_opy_ += 1
      os.environ[bstack11l1111_opy_ (u"ࠨࡒࡈࡖࡈ࡟࡟ࡃࡇࡖࡘࡤࡖࡌࡂࡖࡉࡓࡗࡓࠧ῱")] = str(self.bstack1lllll11ll1l_opy_())
      self.logger.info(bstack11l1111_opy_ (u"ࠤࡓࡩࡷࡩࡹࠡࡵࡨࡸࡺࡶࠠࡤࡱࡰࡴࡱ࡫ࡴࡦࡦࠥῲ"))
    except Exception as e:
      self.logger.error(bstack11l1111_opy_ (u"࡙ࠥࡳࡧࡢ࡭ࡧࠣࡸࡴࠦࡳࡦࡶࡸࡴࠥࡶࡥࡳࡥࡼ࠰ࠥࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡࡽࢀࠦῳ").format(e))
  def bstack1lllll11ll1l_opy_(self):
    if self.bstack1111l111ll_opy_:
      return
    try:
      bstack1lllllll1l1l_opy_ = [platform[bstack11l1111_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡓࡧ࡭ࡦࠩῴ")].lower() for platform in self.config.get(bstack11l1111_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨ῵"), [])]
      bstack1lllll1ll11l_opy_ = sys.maxsize
      bstack1lllllll11l1_opy_ = bstack11l1111_opy_ (u"࠭ࠧῶ")
      for browser in bstack1lllllll1l1l_opy_:
        if browser in self.bstack1llllll11l1l_opy_:
          bstack1lllll111l11_opy_ = self.bstack1llllll11l1l_opy_[browser]
        if bstack1lllll111l11_opy_ < bstack1lllll1ll11l_opy_:
          bstack1lllll1ll11l_opy_ = bstack1lllll111l11_opy_
          bstack1lllllll11l1_opy_ = browser
      return bstack1lllllll11l1_opy_
    except Exception as e:
      self.logger.error(bstack11l1111_opy_ (u"ࠢࡖࡰࡤࡦࡱ࡫ࠠࡵࡱࠣࡪ࡮ࡴࡤࠡࡤࡨࡷࡹࠦࡰ࡭ࡣࡷࡪࡴࡸ࡭࠭ࠢࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥࢁࡽࠣῷ").format(e))
  @classmethod
  def bstack1ll1111ll1_opy_(self):
    return os.getenv(bstack11l1111_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡑࡇࡕࡇ࡞࠭Ὸ"), bstack11l1111_opy_ (u"ࠩࡉࡥࡱࡹࡥࠨΌ")).lower()
  @classmethod
  def bstack1lll1ll111_opy_(self):
    return os.getenv(bstack11l1111_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡓࡉࡗࡉ࡙ࡠࡅࡄࡔ࡙࡛ࡒࡆࡡࡐࡓࡉࡋࠧῺ"), bstack11l1111_opy_ (u"ࠫࠬΏ"))
  @classmethod
  def bstack11llll1l11l_opy_(cls, value):
    cls.bstack11l1l11lll_opy_ = value
  @classmethod
  def bstack1lllll11lll1_opy_(cls):
    return cls.bstack11l1l11lll_opy_
  @classmethod
  def bstack11llll1l111_opy_(cls, value):
    cls.percy_build_id = value
  @classmethod
  def bstack1llllll11111_opy_(cls):
    return cls.percy_build_id