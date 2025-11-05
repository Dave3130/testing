# coding: UTF-8
import sys
bstack11l1ll_opy_ = sys.version_info [0] == 2
bstack1111ll1_opy_ = 2048
bstack11llll_opy_ = 7
def bstack11ll1ll_opy_ (bstack1111l11_opy_):
    global bstack1l111l1_opy_
    bstack1llll11_opy_ = ord (bstack1111l11_opy_ [-1])
    bstack1l1lll1_opy_ = bstack1111l11_opy_ [:-1]
    bstack11111l1_opy_ = bstack1llll11_opy_ % len (bstack1l1lll1_opy_)
    bstack1111l_opy_ = bstack1l1lll1_opy_ [:bstack11111l1_opy_] + bstack1l1lll1_opy_ [bstack11111l1_opy_:]
    if bstack11l1ll_opy_:
        bstack11l11_opy_ = unicode () .join ([unichr (ord (char) - bstack1111ll1_opy_ - (bstack1l_opy_ + bstack1llll11_opy_) % bstack11llll_opy_) for bstack1l_opy_, char in enumerate (bstack1111l_opy_)])
    else:
        bstack11l11_opy_ = str () .join ([chr (ord (char) - bstack1111ll1_opy_ - (bstack1l_opy_ + bstack1llll11_opy_) % bstack11llll_opy_) for bstack1l_opy_, char in enumerate (bstack1111l_opy_)])
    return eval (bstack11l11_opy_)
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
from bstack_utils.helper import bstack11ll11ll1l_opy_
from bstack_utils.measure import measure
from bstack_utils.bstack1l1lll1lll_opy_ import bstack11l1l1l1l1_opy_
class bstack1ll11l1ll_opy_:
  working_dir = os.getcwd()
  bstack1l11111ll_opy_ = False
  config = {}
  bstack111l111111l_opy_ = bstack11ll1ll_opy_ (u"ࠩࠪύ")
  binary_path = bstack11ll1ll_opy_ (u"ࠪࠫὼ")
  bstack1lllll1lll11_opy_ = bstack11ll1ll_opy_ (u"ࠫࠬώ")
  bstack111llllll1_opy_ = False
  bstack1llllll1ll11_opy_ = None
  bstack1lllll1l1l1l_opy_ = {}
  bstack11111111111_opy_ = 300
  bstack11111111l1l_opy_ = False
  logger = None
  bstack1lllll1l1l11_opy_ = False
  bstack1l11ll1111_opy_ = False
  percy_build_id = None
  bstack1lllll111l1l_opy_ = bstack11ll1ll_opy_ (u"ࠬ࠭὾")
  bstack1lllll111ll1_opy_ = {
    bstack11ll1ll_opy_ (u"࠭ࡣࡩࡴࡲࡱࡪ࠭὿") : 1,
    bstack11ll1ll_opy_ (u"ࠧࡧ࡫ࡵࡩ࡫ࡵࡸࠨᾀ") : 2,
    bstack11ll1ll_opy_ (u"ࠨࡧࡧ࡫ࡪ࠭ᾁ") : 3,
    bstack11ll1ll_opy_ (u"ࠩࡶࡥ࡫ࡧࡲࡪࠩᾂ") : 4
  }
  def __init__(self) -> None: pass
  def bstack1lllll1ll1l1_opy_(self):
    bstack1lllll111l11_opy_ = bstack11ll1ll_opy_ (u"ࠪࠫᾃ")
    bstack1lllll1ll11l_opy_ = sys.platform
    bstack1lllll11l11l_opy_ = bstack11ll1ll_opy_ (u"ࠫࡵ࡫ࡲࡤࡻࠪᾄ")
    if re.match(bstack11ll1ll_opy_ (u"ࠧࡪࡡࡳࡹ࡬ࡲࢁࡳࡡࡤࠢࡲࡷࠧᾅ"), bstack1lllll1ll11l_opy_) != None:
      bstack1lllll111l11_opy_ = bstack11l11lll1ll_opy_ + bstack11ll1ll_opy_ (u"ࠨ࠯ࡱࡧࡵࡧࡾ࠳࡯ࡴࡺ࠱ࡾ࡮ࡶࠢᾆ")
      self.bstack1lllll111l1l_opy_ = bstack11ll1ll_opy_ (u"ࠧ࡮ࡣࡦࠫᾇ")
    elif re.match(bstack11ll1ll_opy_ (u"ࠣ࡯ࡶࡻ࡮ࡴࡼ࡮ࡵࡼࡷࢁࡳࡩ࡯ࡩࡺࢀࡨࡿࡧࡸ࡫ࡱࢀࡧࡩࡣࡸ࡫ࡱࢀࡼ࡯࡮ࡤࡧࡿࡩࡲࡩࡼࡸ࡫ࡱ࠷࠷ࠨᾈ"), bstack1lllll1ll11l_opy_) != None:
      bstack1lllll111l11_opy_ = bstack11l11lll1ll_opy_ + bstack11ll1ll_opy_ (u"ࠤ࠲ࡴࡪࡸࡣࡺ࠯ࡺ࡭ࡳ࠴ࡺࡪࡲࠥᾉ")
      bstack1lllll11l11l_opy_ = bstack11ll1ll_opy_ (u"ࠥࡴࡪࡸࡣࡺ࠰ࡨࡼࡪࠨᾊ")
      self.bstack1lllll111l1l_opy_ = bstack11ll1ll_opy_ (u"ࠫࡼ࡯࡮ࠨᾋ")
    else:
      bstack1lllll111l11_opy_ = bstack11l11lll1ll_opy_ + bstack11ll1ll_opy_ (u"ࠧ࠵ࡰࡦࡴࡦࡽ࠲ࡲࡩ࡯ࡷࡻ࠲ࡿ࡯ࡰࠣᾌ")
      self.bstack1lllll111l1l_opy_ = bstack11ll1ll_opy_ (u"࠭࡬ࡪࡰࡸࡼࠬᾍ")
    return bstack1lllll111l11_opy_, bstack1lllll11l11l_opy_
  def bstack1lllll11ll1l_opy_(self):
    try:
      bstack1llllllll11l_opy_ = [os.path.join(expanduser(bstack11ll1ll_opy_ (u"ࠢࡿࠤᾎ")), bstack11ll1ll_opy_ (u"ࠨ࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠨᾏ")), self.working_dir, tempfile.gettempdir()]
      for path in bstack1llllllll11l_opy_:
        if(self.bstack1lllll1ll111_opy_(path)):
          return path
      raise bstack11ll1ll_opy_ (u"ࠤࡘࡲࡦࡨ࡬ࡦࠢࡷࡳࠥࡪ࡯ࡸࡰ࡯ࡳࡦࡪࠠࡱࡧࡵࡧࡾࠦࡢࡪࡰࡤࡶࡾࠨᾐ")
    except Exception as e:
      self.logger.error(bstack11ll1ll_opy_ (u"ࠥࡊࡦ࡯࡬ࡦࡦࠣࡸࡴࠦࡦࡪࡰࡧࠤࡦࡼࡡࡪ࡮ࡤࡦࡱ࡫ࠠࡱࡣࡷ࡬ࠥ࡬࡯ࡳࠢࡳࡩࡷࡩࡹࠡࡦࡲࡻࡳࡲ࡯ࡢࡦ࠯ࠤࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠ࠮ࠢࡾࢁࠧᾑ").format(e))
  def bstack1lllll1ll111_opy_(self, path):
    try:
      if not os.path.exists(path):
        os.makedirs(path)
      return True
    except:
      return False
  def bstack1llllll11111_opy_(self, bstack1llllll111l1_opy_):
    return os.path.join(bstack1llllll111l1_opy_, self.bstack111l111111l_opy_ + bstack11ll1ll_opy_ (u"ࠦ࠳࡫ࡴࡢࡩࠥᾒ"))
  def bstack1lllll1ll1ll_opy_(self, bstack1llllll111l1_opy_, bstack1lllll111lll_opy_):
    if not bstack1lllll111lll_opy_: return
    try:
      bstack1llllll1l1l1_opy_ = self.bstack1llllll11111_opy_(bstack1llllll111l1_opy_)
      with open(bstack1llllll1l1l1_opy_, bstack11ll1ll_opy_ (u"ࠧࡽࠢᾓ")) as f:
        f.write(bstack1lllll111lll_opy_)
        self.logger.debug(bstack11ll1ll_opy_ (u"ࠨࡓࡢࡸࡨࡨࠥࡴࡥࡸࠢࡈࡘࡦ࡭ࠠࡧࡱࡵࠤࡵ࡫ࡲࡤࡻࠥᾔ"))
    except Exception as e:
      self.logger.error(bstack11ll1ll_opy_ (u"ࠢࡖࡰࡤࡦࡱ࡫ࠠࡵࡱࠣࡷࡦࡼࡥࠡࡶ࡫ࡩࠥ࡫ࡴࡢࡩ࠯ࠤࡪࡸࡲࡰࡴ࠽ࠤࢀࢃࠢᾕ").format(e))
  def bstack1lllll1lll1l_opy_(self, bstack1llllll111l1_opy_):
    try:
      bstack1llllll1l1l1_opy_ = self.bstack1llllll11111_opy_(bstack1llllll111l1_opy_)
      if os.path.exists(bstack1llllll1l1l1_opy_):
        with open(bstack1llllll1l1l1_opy_, bstack11ll1ll_opy_ (u"ࠣࡴࠥᾖ")) as f:
          bstack1lllll111lll_opy_ = f.read().strip()
          return bstack1lllll111lll_opy_ if bstack1lllll111lll_opy_ else None
    except Exception as e:
      self.logger.error(bstack11ll1ll_opy_ (u"ࠤࡉࡥ࡮ࡲࡥࡥࠢ࡯ࡳࡦࡪࡩ࡯ࡩࠣࡉ࡙ࡧࡧ࠭ࠢࡨࡶࡷࡵࡲ࠻ࠢࡾࢁࠧᾗ").format(e))
  def bstack1lllll1l1lll_opy_(self, bstack1llllll111l1_opy_, bstack1lllll111l11_opy_):
    bstack1lllll1llll1_opy_ = self.bstack1lllll1lll1l_opy_(bstack1llllll111l1_opy_)
    if bstack1lllll1llll1_opy_:
      try:
        bstack1lllllllllll_opy_ = self.bstack1lllll11ll11_opy_(bstack1lllll1llll1_opy_, bstack1lllll111l11_opy_)
        if not bstack1lllllllllll_opy_:
          self.logger.debug(bstack11ll1ll_opy_ (u"ࠥࡔࡪࡸࡣࡺࠢࡥ࡭ࡳࡧࡲࡺࠢ࡬ࡷࠥࡻࡰࠡࡶࡲࠤࡩࡧࡴࡦࠢࠫࡉ࡙ࡧࡧࠡࡷࡱࡧ࡭ࡧ࡮ࡨࡧࡧ࠭ࠧᾘ"))
          return True
        self.logger.debug(bstack11ll1ll_opy_ (u"ࠦࡓ࡫ࡷࠡࡒࡨࡶࡨࡿࠠࡣ࡫ࡱࡥࡷࡿࠠࡷࡧࡵࡷ࡮ࡵ࡮ࠡࡣࡹࡥ࡮ࡲࡡࡣ࡮ࡨ࠰ࠥࡪ࡯ࡸࡰ࡯ࡳࡦࡪࡩ࡯ࡩࠣࡹࡵࡪࡡࡵࡧࠥᾙ"))
        return False
      except Exception as e:
        self.logger.warn(bstack11ll1ll_opy_ (u"ࠧࡌࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡࡥ࡫ࡩࡨࡱࠠࡧࡱࡵࠤࡧ࡯࡮ࡢࡴࡼࠤࡺࡶࡤࡢࡶࡨࡷ࠱ࠦࡵࡴ࡫ࡱ࡫ࠥ࡫ࡸࡪࡵࡷ࡭ࡳ࡭ࠠࡣ࡫ࡱࡥࡷࡿ࠺ࠡࡽࢀࠦᾚ").format(e))
    return False
  def bstack1lllll11ll11_opy_(self, bstack1lllll1llll1_opy_, bstack1lllll111l11_opy_):
    try:
      headers = {
        bstack11ll1ll_opy_ (u"ࠨࡉࡧ࠯ࡑࡳࡳ࡫࠭ࡎࡣࡷࡧ࡭ࠨᾛ"): bstack1lllll1llll1_opy_
      }
      response = bstack11ll11ll1l_opy_(bstack11ll1ll_opy_ (u"ࠧࡈࡇࡗࠫᾜ"), bstack1lllll111l11_opy_, {}, {bstack11ll1ll_opy_ (u"ࠣࡪࡨࡥࡩ࡫ࡲࡴࠤᾝ"): headers})
      if response.status_code == 304:
        return False
      return True
    except Exception as e:
      raise(bstack11ll1ll_opy_ (u"ࠤࡈࡶࡷࡵࡲࠡࡥ࡫ࡩࡨࡱࡩ࡯ࡩࠣࡪࡴࡸࠠࡑࡧࡵࡧࡾࠦࡢࡪࡰࡤࡶࡾࠦࡵࡱࡦࡤࡸࡪࡹ࠺ࠡࡽࢀࠦᾞ").format(e))
  @measure(event_name=EVENTS.bstack11l11l1l111_opy_, stage=STAGE.bstack11l11ll1ll_opy_)
  def bstack111111111ll_opy_(self, bstack1lllll111l11_opy_, bstack1lllll11l11l_opy_):
    try:
      bstack1llllll11l11_opy_ = self.bstack1lllll11ll1l_opy_()
      bstack1lllll1l111l_opy_ = os.path.join(bstack1llllll11l11_opy_, bstack11ll1ll_opy_ (u"ࠪࡴࡪࡸࡣࡺ࠰ࡽ࡭ࡵ࠭ᾟ"))
      bstack1llllll11ll1_opy_ = os.path.join(bstack1llllll11l11_opy_, bstack1lllll11l11l_opy_)
      if self.bstack1lllll1l1lll_opy_(bstack1llllll11l11_opy_, bstack1lllll111l11_opy_): # if bstack11111111ll1_opy_, bstack1lllllll111_opy_ bstack1lllll111lll_opy_ is bstack1llllll1llll_opy_ to bstack111l111l1l1_opy_ version available (response 304)
        if os.path.exists(bstack1llllll11ll1_opy_):
          self.logger.info(bstack11ll1ll_opy_ (u"ࠦࡕ࡫ࡲࡤࡻࠣࡦ࡮ࡴࡡࡳࡻࠣࡪࡴࡻ࡮ࡥࠢ࡬ࡲࠥࢁࡽ࠭ࠢࡶ࡯࡮ࡶࡰࡪࡰࡪࠤࡩࡵࡷ࡯࡮ࡲࡥࡩࠨᾠ").format(bstack1llllll11ll1_opy_))
          return bstack1llllll11ll1_opy_
        if os.path.exists(bstack1lllll1l111l_opy_):
          self.logger.info(bstack11ll1ll_opy_ (u"ࠧࡖࡥࡳࡥࡼࠤࡿ࡯ࡰࠡࡨࡲࡹࡳࡪࠠࡪࡰࠣࡿࢂ࠲ࠠࡶࡰࡽ࡭ࡵࡶࡩ࡯ࡩࠥᾡ").format(bstack1lllll1l111l_opy_))
          return self.bstack1llllll1lll1_opy_(bstack1lllll1l111l_opy_, bstack1lllll11l11l_opy_)
      self.logger.info(bstack11ll1ll_opy_ (u"ࠨࡄࡰࡹࡱࡰࡴࡧࡤࡪࡰࡪࠤࡵ࡫ࡲࡤࡻࠣࡦ࡮ࡴࡡࡳࡻࠣࡪࡷࡵ࡭ࠡࡽࢀࠦᾢ").format(bstack1lllll111l11_opy_))
      response = bstack11ll11ll1l_opy_(bstack11ll1ll_opy_ (u"ࠧࡈࡇࡗࠫᾣ"), bstack1lllll111l11_opy_, {}, {})
      if response.status_code == 200:
        bstack1lllllll11ll_opy_ = response.headers.get(bstack11ll1ll_opy_ (u"ࠣࡇࡗࡥ࡬ࠨᾤ"), bstack11ll1ll_opy_ (u"ࠤࠥᾥ"))
        if bstack1lllllll11ll_opy_:
          self.bstack1lllll1ll1ll_opy_(bstack1llllll11l11_opy_, bstack1lllllll11ll_opy_)
        with open(bstack1lllll1l111l_opy_, bstack11ll1ll_opy_ (u"ࠪࡻࡧ࠭ᾦ")) as file:
          file.write(response.content)
        self.logger.info(bstack11ll1ll_opy_ (u"ࠦࡉࡵࡷ࡯࡮ࡲࡥࡩ࡫ࡤࠡࡲࡨࡶࡨࡿࠠࡣ࡫ࡱࡥࡷࡿࠠࡢࡰࡧࠤࡸࡧࡶࡦࡦࠣࡥࡹࠦࡻࡾࠤᾧ").format(bstack1lllll1l111l_opy_))
        return self.bstack1llllll1lll1_opy_(bstack1lllll1l111l_opy_, bstack1lllll11l11l_opy_)
      else:
        raise(bstack11ll1ll_opy_ (u"ࠧࡌࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡࡦࡲࡻࡳࡲ࡯ࡢࡦࠣࡸ࡭࡫ࠠࡧ࡫࡯ࡩ࠳ࠦࡓࡵࡣࡷࡹࡸࠦࡣࡰࡦࡨ࠾ࠥࢁࡽࠣᾨ").format(response.status_code))
    except Exception as e:
      self.logger.error(bstack11ll1ll_opy_ (u"ࠨࡕ࡯ࡣࡥࡰࡪࠦࡴࡰࠢࡧࡳࡼࡴ࡬ࡰࡣࡧࠤࡵ࡫ࡲࡤࡻࠣࡦ࡮ࡴࡡࡳࡻ࠽ࠤࢀࢃࠢᾩ").format(e))
  def bstack1lllllll1l11_opy_(self, bstack1lllll111l11_opy_, bstack1lllll11l11l_opy_):
    try:
      retry = 2
      bstack1llllll11ll1_opy_ = None
      bstack1lllllll1lll_opy_ = False
      while retry > 0:
        bstack1llllll11ll1_opy_ = self.bstack111111111ll_opy_(bstack1lllll111l11_opy_, bstack1lllll11l11l_opy_)
        bstack1lllllll1lll_opy_ = self.bstack1lllllll1l1l_opy_(bstack1lllll111l11_opy_, bstack1lllll11l11l_opy_, bstack1llllll11ll1_opy_)
        if bstack1lllllll1lll_opy_:
          break
        retry -= 1
      return bstack1llllll11ll1_opy_, bstack1lllllll1lll_opy_
    except Exception as e:
      self.logger.error(bstack11ll1ll_opy_ (u"ࠢࡖࡰࡤࡦࡱ࡫ࠠࡵࡱࠣ࡫ࡪࡺࠠࡱࡧࡵࡧࡾࠦࡢࡪࡰࡤࡶࡾࠦࡰࡢࡶ࡫ࠦᾪ").format(e))
    return bstack1llllll11ll1_opy_, False
  def bstack1lllllll1l1l_opy_(self, bstack1lllll111l11_opy_, bstack1lllll11l11l_opy_, bstack1llllll11ll1_opy_, bstack1llllll1l1ll_opy_ = 0):
    if bstack1llllll1l1ll_opy_ > 1:
      return False
    if bstack1llllll11ll1_opy_ == None or os.path.exists(bstack1llllll11ll1_opy_) == False:
      self.logger.warn(bstack11ll1ll_opy_ (u"ࠣࡒࡨࡶࡨࡿࠠࡱࡣࡷ࡬ࠥࡴ࡯ࡵࠢࡩࡳࡺࡴࡤ࠭ࠢࡵࡩࡹࡸࡹࡪࡰࡪࠤࡩࡵࡷ࡯࡮ࡲࡥࡩࠨᾫ"))
      return False
    bstack1lllll11l111_opy_ = bstack11ll1ll_opy_ (u"ࡴࠥࡢ࠳࠰ࡀࡱࡧࡵࡧࡾ࠵ࡣ࡭࡫ࠣࡠࡩ࠱࡜࠯࡞ࡧ࠯ࡡ࠴࡜ࡥ࠭ࠥᾬ")
    command = bstack11ll1ll_opy_ (u"ࠪࡿࢂࠦ࠭࠮ࡸࡨࡶࡸ࡯࡯࡯ࠩᾭ").format(bstack1llllll11ll1_opy_)
    bstack1llllll11lll_opy_ = subprocess.check_output(command, shell=True, text=True)
    if re.match(bstack1lllll11l111_opy_, bstack1llllll11lll_opy_) != None:
      return True
    else:
      self.logger.error(bstack11ll1ll_opy_ (u"ࠦࡕ࡫ࡲࡤࡻࠣࡺࡪࡸࡳࡪࡱࡱࠤࡨ࡮ࡥࡤ࡭ࠣࡪࡦ࡯࡬ࡦࡦࠥᾮ"))
      return False
  def bstack1llllll1lll1_opy_(self, bstack1lllll1l111l_opy_, bstack1lllll11l11l_opy_):
    try:
      working_dir = os.path.dirname(bstack1lllll1l111l_opy_)
      shutil.unpack_archive(bstack1lllll1l111l_opy_, working_dir)
      bstack1llllll11ll1_opy_ = os.path.join(working_dir, bstack1lllll11l11l_opy_)
      os.chmod(bstack1llllll11ll1_opy_, 0o755)
      return bstack1llllll11ll1_opy_
    except Exception as e:
      self.logger.error(bstack11ll1ll_opy_ (u"࡛ࠧ࡮ࡢࡤ࡯ࡩࠥࡺ࡯ࠡࡷࡱࡾ࡮ࡶࠠࡱࡧࡵࡧࡾࠦࡢࡪࡰࡤࡶࡾࠨᾯ"))
  def bstack1llllllll1l1_opy_(self):
    try:
      bstack111111111l1_opy_ = self.config.get(bstack11ll1ll_opy_ (u"࠭ࡰࡦࡴࡦࡽࠬᾰ"))
      bstack1llllllll1l1_opy_ = bstack111111111l1_opy_ or (bstack111111111l1_opy_ is None and self.bstack1l11111ll_opy_)
      if not bstack1llllllll1l1_opy_ or self.config.get(bstack11ll1ll_opy_ (u"ࠧࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࠪᾱ"), None) not in bstack11l1l1111l1_opy_:
        return False
      self.bstack111llllll1_opy_ = True
      return True
    except Exception as e:
      self.logger.error(bstack11ll1ll_opy_ (u"ࠣࡗࡱࡥࡧࡲࡥࠡࡶࡲࠤࡩ࡫ࡴࡦࡥࡷࠤࡵ࡫ࡲࡤࡻ࠯ࠤࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡼࡿࠥᾲ").format(e))
  def bstack1llllll1111l_opy_(self):
    try:
      bstack1llllll1111l_opy_ = self.percy_capture_mode
      return bstack1llllll1111l_opy_
    except Exception as e:
      self.logger.error(bstack11ll1ll_opy_ (u"ࠤࡘࡲࡦࡨ࡬ࡦࠢࡷࡳࠥࡪࡥࡵࡧࡦࡸࠥࡶࡥࡳࡥࡼࠤࡨࡧࡰࡵࡷࡵࡩࠥࡳ࡯ࡥࡧ࠯ࠤࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡼࡿࠥᾳ").format(e))
  def init(self, bstack1l11111ll_opy_, config, logger):
    self.bstack1l11111ll_opy_ = bstack1l11111ll_opy_
    self.config = config
    self.logger = logger
    if not self.bstack1llllllll1l1_opy_():
      return
    self.bstack1lllll1l1l1l_opy_ = config.get(bstack11ll1ll_opy_ (u"ࠪࡴࡪࡸࡣࡺࡑࡳࡸ࡮ࡵ࡮ࡴࠩᾴ"), {})
    self.percy_capture_mode = config.get(bstack11ll1ll_opy_ (u"ࠫࡵ࡫ࡲࡤࡻࡆࡥࡵࡺࡵࡳࡧࡐࡳࡩ࡫ࠧ᾵"))
    try:
      bstack1lllll111l11_opy_, bstack1lllll11l11l_opy_ = self.bstack1lllll1ll1l1_opy_()
      self.bstack111l111111l_opy_ = bstack1lllll11l11l_opy_
      bstack1llllll11ll1_opy_, bstack1lllllll1lll_opy_ = self.bstack1lllllll1l11_opy_(bstack1lllll111l11_opy_, bstack1lllll11l11l_opy_)
      if bstack1lllllll1lll_opy_:
        self.binary_path = bstack1llllll11ll1_opy_
        thread = Thread(target=self.bstack1lllll11lll1_opy_)
        thread.start()
      else:
        self.bstack1lllll1l1l11_opy_ = True
        self.logger.error(bstack11ll1ll_opy_ (u"ࠧࡏ࡮ࡷࡣ࡯࡭ࡩࠦࡰࡦࡴࡦࡽࠥࡶࡡࡵࡪࠣࡪࡴࡻ࡮ࡥࠢ࠰ࠤࢀࢃࠬࠡࡗࡱࡥࡧࡲࡥࠡࡶࡲࠤࡸࡺࡡࡳࡶࠣࡔࡪࡸࡣࡺࠤᾶ").format(bstack1llllll11ll1_opy_))
    except Exception as e:
      self.logger.error(bstack11ll1ll_opy_ (u"ࠨࡕ࡯ࡣࡥࡰࡪࠦࡴࡰࠢࡶࡸࡦࡸࡴࠡࡲࡨࡶࡨࡿࠬࠡࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤࢀࢃࠢᾷ").format(e))
  def bstack11111111l11_opy_(self):
    try:
      logfile = os.path.join(self.working_dir, bstack11ll1ll_opy_ (u"ࠧ࡭ࡱࡪࠫᾸ"), bstack11ll1ll_opy_ (u"ࠨࡲࡨࡶࡨࡿ࠮࡭ࡱࡪࠫᾹ"))
      os.makedirs(os.path.dirname(logfile)) if not os.path.exists(os.path.dirname(logfile)) else None
      self.logger.debug(bstack11ll1ll_opy_ (u"ࠤࡓࡹࡸ࡮ࡩ࡯ࡩࠣࡴࡪࡸࡣࡺࠢ࡯ࡳ࡬ࡹࠠࡢࡶࠣࡿࢂࠨᾺ").format(logfile))
      self.bstack1lllll1lll11_opy_ = logfile
    except Exception as e:
      self.logger.error(bstack11ll1ll_opy_ (u"࡙ࠥࡳࡧࡢ࡭ࡧࠣࡸࡴࠦࡳࡦࡶࠣࡴࡪࡸࡣࡺࠢ࡯ࡳ࡬ࠦࡰࡢࡶ࡫࠰ࠥࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡࡽࢀࠦΆ").format(e))
  @measure(event_name=EVENTS.bstack11l1l11l1l1_opy_, stage=STAGE.bstack11l11ll1ll_opy_)
  def bstack1lllll11lll1_opy_(self):
    bstack1llllllllll1_opy_ = self.bstack1llllll111ll_opy_()
    if bstack1llllllllll1_opy_ == None:
      self.bstack1lllll1l1l11_opy_ = True
      self.logger.error(bstack11ll1ll_opy_ (u"ࠦࡕ࡫ࡲࡤࡻࠣࡸࡴࡱࡥ࡯ࠢࡱࡳࡹࠦࡦࡰࡷࡱࡨ࠱ࠦࡆࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡶࡸࡦࡸࡴࠡࡲࡨࡶࡨࡿࠢᾼ"))
      return False
    bstack1lllllll111l_opy_ = [bstack11ll1ll_opy_ (u"ࠧࡧࡰࡱ࠼ࡨࡼࡪࡩ࠺ࡴࡶࡤࡶࡹࠨ᾽") if self.bstack1l11111ll_opy_ else bstack11ll1ll_opy_ (u"࠭ࡥࡹࡧࡦ࠾ࡸࡺࡡࡳࡶࠪι")]
    bstack11111l1llll_opy_ = self.bstack1lllll1l1ll1_opy_()
    if bstack11111l1llll_opy_ != None:
      bstack1lllllll111l_opy_.append(bstack11ll1ll_opy_ (u"ࠢ࠮ࡥࠣࡿࢂࠨ᾿").format(bstack11111l1llll_opy_))
    env = os.environ.copy()
    env[bstack11ll1ll_opy_ (u"ࠣࡒࡈࡖࡈ࡟࡟ࡕࡑࡎࡉࡓࠨ῀")] = bstack1llllllllll1_opy_
    env[bstack11ll1ll_opy_ (u"ࠤࡗࡌࡤࡈࡕࡊࡎࡇࡣ࡚࡛ࡉࡅࠤ῁")] = os.environ.get(bstack11ll1ll_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚ࡈࡖࡄࡢ࡙࡚ࡏࡄࠨῂ"), bstack11ll1ll_opy_ (u"ࠫࠬῃ"))
    bstack1lllllll11l1_opy_ = [self.binary_path]
    self.bstack11111111l11_opy_()
    self.bstack1llllll1ll11_opy_ = self.bstack1llllll11l1l_opy_(bstack1lllllll11l1_opy_ + bstack1lllllll111l_opy_, env)
    self.logger.debug(bstack11ll1ll_opy_ (u"࡙ࠧࡴࡢࡴࡷ࡭ࡳ࡭ࠠࡉࡧࡤࡰࡹ࡮ࠠࡄࡪࡨࡧࡰࠨῄ"))
    bstack1llllll1l1ll_opy_ = 0
    while self.bstack1llllll1ll11_opy_.poll() == None:
      bstack1lllllllll1l_opy_ = self.bstack1lllll11llll_opy_()
      if bstack1lllllllll1l_opy_:
        self.logger.debug(bstack11ll1ll_opy_ (u"ࠨࡈࡦࡣ࡯ࡸ࡭ࠦࡃࡩࡧࡦ࡯ࠥࡹࡵࡤࡥࡨࡷࡸ࡬ࡵ࡭ࠤ῅"))
        self.bstack11111111l1l_opy_ = True
        return True
      bstack1llllll1l1ll_opy_ += 1
      self.logger.debug(bstack11ll1ll_opy_ (u"ࠢࡉࡧࡤࡰࡹ࡮ࠠࡄࡪࡨࡧࡰࠦࡒࡦࡶࡵࡽࠥ࠳ࠠࡼࡿࠥῆ").format(bstack1llllll1l1ll_opy_))
      time.sleep(2)
    self.logger.error(bstack11ll1ll_opy_ (u"ࠣࡈࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤࡸࡺࡡࡳࡶࠣࡴࡪࡸࡣࡺ࠮ࠣࡌࡪࡧ࡬ࡵࡪࠣࡇ࡭࡫ࡣ࡬ࠢࡉࡥ࡮ࡲࡥࡥࠢࡤࡪࡹ࡫ࡲࠡࡽࢀࠤࡦࡺࡴࡦ࡯ࡳࡸࡸࠨῇ").format(bstack1llllll1l1ll_opy_))
    self.bstack1lllll1l1l11_opy_ = True
    return False
  def bstack1lllll11llll_opy_(self, bstack1llllll1l1ll_opy_ = 0):
    if bstack1llllll1l1ll_opy_ > 10:
      return False
    try:
      bstack1lllll1lllll_opy_ = os.environ.get(bstack11ll1ll_opy_ (u"ࠩࡓࡉࡗࡉ࡙ࡠࡕࡈࡖ࡛ࡋࡒࡠࡃࡇࡈࡗࡋࡓࡔࠩῈ"), bstack11ll1ll_opy_ (u"ࠪ࡬ࡹࡺࡰ࠻࠱࠲ࡰࡴࡩࡡ࡭ࡪࡲࡷࡹࡀ࠵࠴࠵࠻ࠫΈ"))
      bstack1llllll1l111_opy_ = bstack1lllll1lllll_opy_ + bstack11l1l11l11l_opy_
      response = requests.get(bstack1llllll1l111_opy_)
      data = response.json()
      self.percy_build_id = data.get(bstack11ll1ll_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࠪῊ"), {}).get(bstack11ll1ll_opy_ (u"ࠬ࡯ࡤࠨΉ"), None)
      return True
    except:
      self.logger.debug(bstack11ll1ll_opy_ (u"ࠨࡅࡳࡴࡲࡶࠥࡵࡣࡤࡷࡵࡶࡪࡪࠠࡸࡪ࡬ࡰࡪࠦࡰࡳࡱࡦࡩࡸࡹࡩ࡯ࡩࠣ࡬ࡪࡧ࡬ࡵࡪࠣࡧ࡭࡫ࡣ࡬ࠢࡵࡩࡸࡶ࡯࡯ࡵࡨࠦῌ"))
      return False
  def bstack1llllll111ll_opy_(self):
    bstack1lllllll1ll1_opy_ = bstack11ll1ll_opy_ (u"ࠧࡢࡲࡳࠫ῍") if self.bstack1l11111ll_opy_ else bstack11ll1ll_opy_ (u"ࠨࡣࡸࡸࡴࡳࡡࡵࡧࠪ῎")
    bstack1lllll1l11l1_opy_ = bstack11ll1ll_opy_ (u"ࠤࡸࡲࡩ࡫ࡦࡪࡰࡨࡨࠧ῏") if self.config.get(bstack11ll1ll_opy_ (u"ࠪࡴࡪࡸࡣࡺࠩῐ")) is None else True
    bstack11ll11111ll_opy_ = bstack11ll1ll_opy_ (u"ࠦࡦࡶࡩ࠰ࡣࡳࡴࡤࡶࡥࡳࡥࡼ࠳࡬࡫ࡴࡠࡲࡵࡳ࡯࡫ࡣࡵࡡࡷࡳࡰ࡫࡮ࡀࡰࡤࡱࡪࡃࡻࡾࠨࡷࡽࡵ࡫࠽ࡼࡿࠩࡴࡪࡸࡣࡺ࠿ࡾࢁࠧῑ").format(self.config[bstack11ll1ll_opy_ (u"ࠬࡶࡲࡰ࡬ࡨࡧࡹࡔࡡ࡮ࡧࠪῒ")], bstack1lllllll1ll1_opy_, bstack1lllll1l11l1_opy_)
    if self.percy_capture_mode:
      bstack11ll11111ll_opy_ += bstack11ll1ll_opy_ (u"ࠨࠦࡱࡧࡵࡧࡾࡥࡣࡢࡲࡷࡹࡷ࡫࡟࡮ࡱࡧࡩࡂࢁࡽࠣΐ").format(self.percy_capture_mode)
    uri = bstack11l1l1l1l1_opy_(bstack11ll11111ll_opy_)
    try:
      response = bstack11ll11ll1l_opy_(bstack11ll1ll_opy_ (u"ࠧࡈࡇࡗࠫ῔"), uri, {}, {bstack11ll1ll_opy_ (u"ࠨࡣࡸࡸ࡭࠭῕"): (self.config[bstack11ll1ll_opy_ (u"ࠩࡸࡷࡪࡸࡎࡢ࡯ࡨࠫῖ")], self.config[bstack11ll1ll_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵࡎࡩࡾ࠭ῗ")])})
      if response.status_code == 200:
        data = response.json()
        self.bstack111llllll1_opy_ = data.get(bstack11ll1ll_opy_ (u"ࠫࡸࡻࡣࡤࡧࡶࡷࠬῘ"))
        self.percy_capture_mode = data.get(bstack11ll1ll_opy_ (u"ࠬࡶࡥࡳࡥࡼࡣࡨࡧࡰࡵࡷࡵࡩࡤࡳ࡯ࡥࡧࠪῙ"))
        os.environ[bstack11ll1ll_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡖࡅࡓࡅ࡜ࠫῚ")] = str(self.bstack111llllll1_opy_)
        os.environ[bstack11ll1ll_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡐࡆࡔࡆ࡝ࡤࡉࡁࡑࡖࡘࡖࡊࡥࡍࡐࡆࡈࠫΊ")] = str(self.percy_capture_mode)
        if bstack1lllll1l11l1_opy_ == bstack11ll1ll_opy_ (u"ࠣࡷࡱࡨࡪ࡬ࡩ࡯ࡧࡧࠦ῜") and str(self.bstack111llllll1_opy_).lower() == bstack11ll1ll_opy_ (u"ࠤࡷࡶࡺ࡫ࠢ῝"):
          self.bstack1l11ll1111_opy_ = True
        if bstack11ll1ll_opy_ (u"ࠥࡸࡴࡱࡥ࡯ࠤ῞") in data:
          return data[bstack11ll1ll_opy_ (u"ࠦࡹࡵ࡫ࡦࡰࠥ῟")]
        else:
          raise bstack11ll1ll_opy_ (u"࡚ࠬ࡯࡬ࡧࡱࠤࡓࡵࡴࠡࡈࡲࡹࡳࡪࠠ࠮ࠢࡾࢁࠬῠ").format(data)
      else:
        raise bstack11ll1ll_opy_ (u"ࠨࡆࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡩࡩࡹࡩࡨࠡࡲࡨࡶࡨࡿࠠࡵࡱ࡮ࡩࡳ࠲ࠠࡓࡧࡶࡴࡴࡴࡳࡦࠢࡶࡸࡦࡺࡵࡴࠢ࠰ࠤࢀࢃࠬࠡࡔࡨࡷࡵࡵ࡮ࡴࡧࠣࡆࡴࡪࡹࠡ࠯ࠣࡿࢂࠨῡ").format(response.status_code, response.json())
    except Exception as e:
      self.logger.error(bstack11ll1ll_opy_ (u"ࠢࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣ࡭ࡳࠦࡣࡳࡧࡤࡸ࡮ࡴࡧࠡࡲࡨࡶࡨࡿࠠࡱࡴࡲ࡮ࡪࡩࡴࠣῢ").format(e))
  def bstack1lllll1l1ll1_opy_(self):
    bstack1llllll1ll1l_opy_ = os.path.join(tempfile.gettempdir(), bstack11ll1ll_opy_ (u"ࠣࡲࡨࡶࡨࡿࡃࡰࡰࡩ࡭࡬࠴ࡪࡴࡱࡱࠦΰ"))
    try:
      if bstack11ll1ll_opy_ (u"ࠩࡹࡩࡷࡹࡩࡰࡰࠪῤ") not in self.bstack1lllll1l1l1l_opy_:
        self.bstack1lllll1l1l1l_opy_[bstack11ll1ll_opy_ (u"ࠪࡺࡪࡸࡳࡪࡱࡱࠫῥ")] = 2
      with open(bstack1llllll1ll1l_opy_, bstack11ll1ll_opy_ (u"ࠫࡼ࠭ῦ")) as fp:
        json.dump(self.bstack1lllll1l1l1l_opy_, fp)
      return bstack1llllll1ll1l_opy_
    except Exception as e:
      self.logger.error(bstack11ll1ll_opy_ (u"࡛ࠧ࡮ࡢࡤ࡯ࡩࠥࡺ࡯ࠡࡥࡵࡩࡦࡺࡥࠡࡲࡨࡶࡨࡿࠠࡤࡱࡱࡪ࠱ࠦࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢࡾࢁࠧῧ").format(e))
  def bstack1llllll11l1l_opy_(self, cmd, env = os.environ.copy()):
    try:
      if self.bstack1lllll111l1l_opy_ == bstack11ll1ll_opy_ (u"࠭ࡷࡪࡰࠪῨ"):
        bstack1lllll11l1l1_opy_ = [bstack11ll1ll_opy_ (u"ࠧࡤ࡯ࡧ࠲ࡪࡾࡥࠨῩ"), bstack11ll1ll_opy_ (u"ࠨ࠱ࡦࠫῪ")]
        cmd = bstack1lllll11l1l1_opy_ + cmd
      cmd = bstack11ll1ll_opy_ (u"ࠩࠣࠫΎ").join(cmd)
      self.logger.debug(bstack11ll1ll_opy_ (u"ࠥࡖࡺࡴ࡮ࡪࡰࡪࠤࢀࢃࠢῬ").format(cmd))
      with open(self.bstack1lllll1lll11_opy_, bstack11ll1ll_opy_ (u"ࠦࡦࠨ῭")) as bstack1lllll11l1ll_opy_:
        process = subprocess.Popen(cmd, shell=True, stdout=bstack1lllll11l1ll_opy_, text=True, stderr=bstack1lllll11l1ll_opy_, env=env, universal_newlines=True)
      return process
    except Exception as e:
      self.bstack1lllll1l1l11_opy_ = True
      self.logger.error(bstack11ll1ll_opy_ (u"ࠧࡌࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡࡵࡷࡥࡷࡺࠠࡱࡧࡵࡧࡾࠦࡷࡪࡶ࡫ࠤࡨࡳࡤࠡ࠯ࠣࡿࢂ࠲ࠠࡆࡺࡦࡩࡵࡺࡩࡰࡰ࠽ࠤࢀࢃࠢ΅").format(cmd, e))
  def shutdown(self):
    try:
      if self.bstack11111111l1l_opy_:
        self.logger.info(bstack11ll1ll_opy_ (u"ࠨࡓࡵࡱࡳࡴ࡮ࡴࡧࠡࡒࡨࡶࡨࡿࠢ`"))
        cmd = [self.binary_path, bstack11ll1ll_opy_ (u"ࠢࡦࡺࡨࡧ࠿ࡹࡴࡰࡲࠥ῰")]
        self.bstack1llllll11l1l_opy_(cmd)
        self.bstack11111111l1l_opy_ = False
    except Exception as e:
      self.logger.error(bstack11ll1ll_opy_ (u"ࠣࡈࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤࡸࡺ࡯ࡱࠢࡶࡩࡸࡹࡩࡰࡰࠣࡻ࡮ࡺࡨࠡࡥࡲࡱࡲࡧ࡮ࡥࠢ࠰ࠤࢀࢃࠬࠡࡇࡻࡧࡪࡶࡴࡪࡱࡱ࠾ࠥࢁࡽࠣ῱").format(cmd, e))
  def bstack1ll1lll1ll_opy_(self):
    if not self.bstack111llllll1_opy_:
      return
    try:
      bstack1111111111l_opy_ = 0
      while not self.bstack11111111l1l_opy_ and bstack1111111111l_opy_ < self.bstack11111111111_opy_:
        if self.bstack1lllll1l1l11_opy_:
          self.logger.info(bstack11ll1ll_opy_ (u"ࠤࡓࡩࡷࡩࡹࠡࡵࡨࡸࡺࡶࠠࡧࡣ࡬ࡰࡪࡪࠢῲ"))
          return
        time.sleep(1)
        bstack1111111111l_opy_ += 1
      os.environ[bstack11ll1ll_opy_ (u"ࠪࡔࡊࡘࡃ࡚ࡡࡅࡉࡘ࡚࡟ࡑࡎࡄࡘࡋࡕࡒࡎࠩῳ")] = str(self.bstack1llllll1l11l_opy_())
      self.logger.info(bstack11ll1ll_opy_ (u"ࠦࡕ࡫ࡲࡤࡻࠣࡷࡪࡺࡵࡱࠢࡦࡳࡲࡶ࡬ࡦࡶࡨࡨࠧῴ"))
    except Exception as e:
      self.logger.error(bstack11ll1ll_opy_ (u"࡛ࠧ࡮ࡢࡤ࡯ࡩࠥࡺ࡯ࠡࡵࡨࡸࡺࡶࠠࡱࡧࡵࡧࡾ࠲ࠠࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣࡿࢂࠨ῵").format(e))
  def bstack1llllll1l11l_opy_(self):
    if self.bstack1l11111ll_opy_:
      return
    try:
      bstack1llllllll1ll_opy_ = [platform[bstack11ll1ll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡎࡢ࡯ࡨࠫῶ")].lower() for platform in self.config.get(bstack11ll1ll_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪῷ"), [])]
      bstack1llllllll111_opy_ = sys.maxsize
      bstack1lllllll1111_opy_ = bstack11ll1ll_opy_ (u"ࠨࠩῸ")
      for browser in bstack1llllllll1ll_opy_:
        if browser in self.bstack1lllll111ll1_opy_:
          bstack1lllll1l1111_opy_ = self.bstack1lllll111ll1_opy_[browser]
        if bstack1lllll1l1111_opy_ < bstack1llllllll111_opy_:
          bstack1llllllll111_opy_ = bstack1lllll1l1111_opy_
          bstack1lllllll1111_opy_ = browser
      return bstack1lllllll1111_opy_
    except Exception as e:
      self.logger.error(bstack11ll1ll_opy_ (u"ࠤࡘࡲࡦࡨ࡬ࡦࠢࡷࡳࠥ࡬ࡩ࡯ࡦࠣࡦࡪࡹࡴࠡࡲ࡯ࡥࡹ࡬࡯ࡳ࡯࠯ࠤࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡼࡿࠥΌ").format(e))
  @classmethod
  def bstack11l1111ll_opy_(self):
    return os.getenv(bstack11ll1ll_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡓࡉࡗࡉ࡙ࠨῺ"), bstack11ll1ll_opy_ (u"ࠫࡋࡧ࡬ࡴࡧࠪΏ")).lower()
  @classmethod
  def bstack11ll1l111l_opy_(self):
    return os.getenv(bstack11ll1ll_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡕࡋࡒࡄ࡛ࡢࡇࡆࡖࡔࡖࡔࡈࡣࡒࡕࡄࡆࠩῼ"), bstack11ll1ll_opy_ (u"࠭ࠧ´"))
  @classmethod
  def bstack11llll1ll1l_opy_(cls, value):
    cls.bstack1l11ll1111_opy_ = value
  @classmethod
  def bstack1lllllllll11_opy_(cls):
    return cls.bstack1l11ll1111_opy_
  @classmethod
  def bstack11llll1lll1_opy_(cls, value):
    cls.percy_build_id = value
  @classmethod
  def bstack1lllll1l11ll_opy_(cls):
    return cls.percy_build_id