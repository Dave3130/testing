# coding: UTF-8
import sys
bstack1111l1_opy_ = sys.version_info [0] == 2
bstack1l1ll11_opy_ = 2048
bstack11l11l_opy_ = 7
def bstack11111_opy_ (bstack11lll_opy_):
    global bstack111l1l1_opy_
    bstack1l1l1_opy_ = ord (bstack11lll_opy_ [-1])
    bstack1l111ll_opy_ = bstack11lll_opy_ [:-1]
    bstack1l1l11_opy_ = bstack1l1l1_opy_ % len (bstack1l111ll_opy_)
    bstack1l11l11_opy_ = bstack1l111ll_opy_ [:bstack1l1l11_opy_] + bstack1l111ll_opy_ [bstack1l1l11_opy_:]
    if bstack1111l1_opy_:
        bstack1llll11_opy_ = unicode () .join ([unichr (ord (char) - bstack1l1ll11_opy_ - (bstack1111ll1_opy_ + bstack1l1l1_opy_) % bstack11l11l_opy_) for bstack1111ll1_opy_, char in enumerate (bstack1l11l11_opy_)])
    else:
        bstack1llll11_opy_ = str () .join ([chr (ord (char) - bstack1l1ll11_opy_ - (bstack1111ll1_opy_ + bstack1l1l1_opy_) % bstack11l11l_opy_) for bstack1111ll1_opy_, char in enumerate (bstack1l11l11_opy_)])
    return eval (bstack1llll11_opy_)
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
from bstack_utils.helper import bstack1111ll1lll_opy_
from bstack_utils.measure import measure
from bstack_utils.bstack1l1l1ll11_opy_ import bstack1ll11llll_opy_
class bstack111ll1lll1_opy_:
  working_dir = os.getcwd()
  bstack11l1ll11l1_opy_ = False
  config = {}
  bstack1111l1ll111_opy_ = bstack11111_opy_ (u"ࠨࠩὺ")
  binary_path = bstack11111_opy_ (u"ࠩࠪύ")
  bstack1lllll1l11l1_opy_ = bstack11111_opy_ (u"ࠪࠫὼ")
  bstack11l1l1111_opy_ = False
  bstack1llllll11lll_opy_ = None
  bstack1llllll11ll1_opy_ = {}
  bstack1lllllll1l1l_opy_ = 300
  bstack1lllllllll11_opy_ = False
  logger = None
  bstack1lllll11l1l1_opy_ = False
  bstack1l11ll11l1_opy_ = False
  percy_build_id = None
  bstack1llllll11111_opy_ = bstack11111_opy_ (u"ࠫࠬώ")
  bstack11111111111_opy_ = {
    bstack11111_opy_ (u"ࠬࡩࡨࡳࡱࡰࡩࠬ὾") : 1,
    bstack11111_opy_ (u"࠭ࡦࡪࡴࡨࡪࡴࡾࠧ὿") : 2,
    bstack11111_opy_ (u"ࠧࡦࡦࡪࡩࠬᾀ") : 3,
    bstack11111_opy_ (u"ࠨࡵࡤࡪࡦࡸࡩࠨᾁ") : 4
  }
  def __init__(self) -> None: pass
  def bstack1lllllll11ll_opy_(self):
    bstack1lllll1ll111_opy_ = bstack11111_opy_ (u"ࠩࠪᾂ")
    bstack1llllll1ll1l_opy_ = sys.platform
    bstack1lllll11ll11_opy_ = bstack11111_opy_ (u"ࠪࡴࡪࡸࡣࡺࠩᾃ")
    if re.match(bstack11111_opy_ (u"ࠦࡩࡧࡲࡸ࡫ࡱࢀࡲࡧࡣࠡࡱࡶࠦᾄ"), bstack1llllll1ll1l_opy_) != None:
      bstack1lllll1ll111_opy_ = bstack11l11ll1l1l_opy_ + bstack11111_opy_ (u"ࠧ࠵ࡰࡦࡴࡦࡽ࠲ࡵࡳࡹ࠰ࡽ࡭ࡵࠨᾅ")
      self.bstack1llllll11111_opy_ = bstack11111_opy_ (u"࠭࡭ࡢࡥࠪᾆ")
    elif re.match(bstack11111_opy_ (u"ࠢ࡮ࡵࡺ࡭ࡳࢂ࡭ࡴࡻࡶࢀࡲ࡯࡮ࡨࡹࡿࡧࡾ࡭ࡷࡪࡰࡿࡦࡨࡩࡷࡪࡰࡿࡻ࡮ࡴࡣࡦࡾࡨࡱࡨࢂࡷࡪࡰ࠶࠶ࠧᾇ"), bstack1llllll1ll1l_opy_) != None:
      bstack1lllll1ll111_opy_ = bstack11l11ll1l1l_opy_ + bstack11111_opy_ (u"ࠣ࠱ࡳࡩࡷࡩࡹ࠮ࡹ࡬ࡲ࠳ࢀࡩࡱࠤᾈ")
      bstack1lllll11ll11_opy_ = bstack11111_opy_ (u"ࠤࡳࡩࡷࡩࡹ࠯ࡧࡻࡩࠧᾉ")
      self.bstack1llllll11111_opy_ = bstack11111_opy_ (u"ࠪࡻ࡮ࡴࠧᾊ")
    else:
      bstack1lllll1ll111_opy_ = bstack11l11ll1l1l_opy_ + bstack11111_opy_ (u"ࠦ࠴ࡶࡥࡳࡥࡼ࠱ࡱ࡯࡮ࡶࡺ࠱ࡾ࡮ࡶࠢᾋ")
      self.bstack1llllll11111_opy_ = bstack11111_opy_ (u"ࠬࡲࡩ࡯ࡷࡻࠫᾌ")
    return bstack1lllll1ll111_opy_, bstack1lllll11ll11_opy_
  def bstack1llllll1l111_opy_(self):
    try:
      bstack1llllll1l1ll_opy_ = [os.path.join(expanduser(bstack11111_opy_ (u"ࠨࡾࠣᾍ")), bstack11111_opy_ (u"ࠧ࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠧᾎ")), self.working_dir, tempfile.gettempdir()]
      for path in bstack1llllll1l1ll_opy_:
        if(self.bstack1llllll1111l_opy_(path)):
          return path
      raise bstack11111_opy_ (u"ࠣࡗࡱࡥࡧࡲࡥࠡࡶࡲࠤࡩࡵࡷ࡯࡮ࡲࡥࡩࠦࡰࡦࡴࡦࡽࠥࡨࡩ࡯ࡣࡵࡽࠧᾏ")
    except Exception as e:
      self.logger.error(bstack11111_opy_ (u"ࠤࡉࡥ࡮ࡲࡥࡥࠢࡷࡳࠥ࡬ࡩ࡯ࡦࠣࡥࡻࡧࡩ࡭ࡣࡥࡰࡪࠦࡰࡢࡶ࡫ࠤ࡫ࡵࡲࠡࡲࡨࡶࡨࡿࠠࡥࡱࡺࡲࡱࡵࡡࡥ࠮ࠣࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦ࠭ࠡࡽࢀࠦᾐ").format(e))
  def bstack1llllll1111l_opy_(self, path):
    try:
      if not os.path.exists(path):
        os.makedirs(path)
      return True
    except:
      return False
  def bstack1lllll1ll1l1_opy_(self, bstack1lllll11l111_opy_):
    return os.path.join(bstack1lllll11l111_opy_, self.bstack1111l1ll111_opy_ + bstack11111_opy_ (u"ࠥ࠲ࡪࡺࡡࡨࠤᾑ"))
  def bstack1lllll11ll1l_opy_(self, bstack1lllll11l111_opy_, bstack1lllllllll1l_opy_):
    if not bstack1lllllllll1l_opy_: return
    try:
      bstack1llllllll11l_opy_ = self.bstack1lllll1ll1l1_opy_(bstack1lllll11l111_opy_)
      with open(bstack1llllllll11l_opy_, bstack11111_opy_ (u"ࠦࡼࠨᾒ")) as f:
        f.write(bstack1lllllllll1l_opy_)
        self.logger.debug(bstack11111_opy_ (u"࡙ࠧࡡࡷࡧࡧࠤࡳ࡫ࡷࠡࡇࡗࡥ࡬ࠦࡦࡰࡴࠣࡴࡪࡸࡣࡺࠤᾓ"))
    except Exception as e:
      self.logger.error(bstack11111_opy_ (u"ࠨࡕ࡯ࡣࡥࡰࡪࠦࡴࡰࠢࡶࡥࡻ࡫ࠠࡵࡪࡨࠤࡪࡺࡡࡨ࠮ࠣࡩࡷࡸ࡯ࡳ࠼ࠣࡿࢂࠨᾔ").format(e))
  def bstack11111111ll1_opy_(self, bstack1lllll11l111_opy_):
    try:
      bstack1llllllll11l_opy_ = self.bstack1lllll1ll1l1_opy_(bstack1lllll11l111_opy_)
      if os.path.exists(bstack1llllllll11l_opy_):
        with open(bstack1llllllll11l_opy_, bstack11111_opy_ (u"ࠢࡳࠤᾕ")) as f:
          bstack1lllllllll1l_opy_ = f.read().strip()
          return bstack1lllllllll1l_opy_ if bstack1lllllllll1l_opy_ else None
    except Exception as e:
      self.logger.error(bstack11111_opy_ (u"ࠣࡈࡤ࡭ࡱ࡫ࡤࠡ࡮ࡲࡥࡩ࡯࡮ࡨࠢࡈࡘࡦ࡭ࠬࠡࡧࡵࡶࡴࡸ࠺ࠡࡽࢀࠦᾖ").format(e))
  def bstack111111111ll_opy_(self, bstack1lllll11l111_opy_, bstack1lllll1ll111_opy_):
    bstack1llllllllll1_opy_ = self.bstack11111111ll1_opy_(bstack1lllll11l111_opy_)
    if bstack1llllllllll1_opy_:
      try:
        bstack1llllllll1l1_opy_ = self.bstack1lllllll1ll1_opy_(bstack1llllllllll1_opy_, bstack1lllll1ll111_opy_)
        if not bstack1llllllll1l1_opy_:
          self.logger.debug(bstack11111_opy_ (u"ࠤࡓࡩࡷࡩࡹࠡࡤ࡬ࡲࡦࡸࡹࠡ࡫ࡶࠤࡺࡶࠠࡵࡱࠣࡨࡦࡺࡥࠡࠪࡈࡘࡦ࡭ࠠࡶࡰࡦ࡬ࡦࡴࡧࡦࡦࠬࠦᾗ"))
          return True
        self.logger.debug(bstack11111_opy_ (u"ࠥࡒࡪࡽࠠࡑࡧࡵࡧࡾࠦࡢࡪࡰࡤࡶࡾࠦࡶࡦࡴࡶ࡭ࡴࡴࠠࡢࡸࡤ࡭ࡱࡧࡢ࡭ࡧ࠯ࠤࡩࡵࡷ࡯࡮ࡲࡥࡩ࡯࡮ࡨࠢࡸࡴࡩࡧࡴࡦࠤᾘ"))
        return False
      except Exception as e:
        self.logger.warn(bstack11111_opy_ (u"ࠦࡋࡧࡩ࡭ࡧࡧࠤࡹࡵࠠࡤࡪࡨࡧࡰࠦࡦࡰࡴࠣࡦ࡮ࡴࡡࡳࡻࠣࡹࡵࡪࡡࡵࡧࡶ࠰ࠥࡻࡳࡪࡰࡪࠤࡪࡾࡩࡴࡶ࡬ࡲ࡬ࠦࡢࡪࡰࡤࡶࡾࡀࠠࡼࡿࠥᾙ").format(e))
    return False
  def bstack1lllllll1ll1_opy_(self, bstack1llllllllll1_opy_, bstack1lllll1ll111_opy_):
    try:
      headers = {
        bstack11111_opy_ (u"ࠧࡏࡦ࠮ࡐࡲࡲࡪ࠳ࡍࡢࡶࡦ࡬ࠧᾚ"): bstack1llllllllll1_opy_
      }
      response = bstack1111ll1lll_opy_(bstack11111_opy_ (u"࠭ࡇࡆࡖࠪᾛ"), bstack1lllll1ll111_opy_, {}, {bstack11111_opy_ (u"ࠢࡩࡧࡤࡨࡪࡸࡳࠣᾜ"): headers})
      if response.status_code == 304:
        return False
      return True
    except Exception as e:
      raise(bstack11111_opy_ (u"ࠣࡇࡵࡶࡴࡸࠠࡤࡪࡨࡧࡰ࡯࡮ࡨࠢࡩࡳࡷࠦࡐࡦࡴࡦࡽࠥࡨࡩ࡯ࡣࡵࡽࠥࡻࡰࡥࡣࡷࡩࡸࡀࠠࡼࡿࠥᾝ").format(e))
  @measure(event_name=EVENTS.bstack11l11lll1ll_opy_, stage=STAGE.bstack111l1l11l_opy_)
  def bstack11111111l11_opy_(self, bstack1lllll1ll111_opy_, bstack1lllll11ll11_opy_):
    try:
      bstack1lllll11l11l_opy_ = self.bstack1llllll1l111_opy_()
      bstack1lllll111l1l_opy_ = os.path.join(bstack1lllll11l11l_opy_, bstack11111_opy_ (u"ࠩࡳࡩࡷࡩࡹ࠯ࡼ࡬ࡴࠬᾞ"))
      bstack1lllll1ll11l_opy_ = os.path.join(bstack1lllll11l11l_opy_, bstack1lllll11ll11_opy_)
      if self.bstack111111111ll_opy_(bstack1lllll11l11l_opy_, bstack1lllll1ll111_opy_): # if bstack1llllllll111_opy_, bstack1llll11l11l_opy_ bstack1lllllllll1l_opy_ is bstack1lllll111lll_opy_ to bstack111l1ll111l_opy_ version available (response 304)
        if os.path.exists(bstack1lllll1ll11l_opy_):
          self.logger.info(bstack11111_opy_ (u"ࠥࡔࡪࡸࡣࡺࠢࡥ࡭ࡳࡧࡲࡺࠢࡩࡳࡺࡴࡤࠡ࡫ࡱࠤࢀࢃࠬࠡࡵ࡮࡭ࡵࡶࡩ࡯ࡩࠣࡨࡴࡽ࡮࡭ࡱࡤࡨࠧᾟ").format(bstack1lllll1ll11l_opy_))
          return bstack1lllll1ll11l_opy_
        if os.path.exists(bstack1lllll111l1l_opy_):
          self.logger.info(bstack11111_opy_ (u"ࠦࡕ࡫ࡲࡤࡻࠣࡾ࡮ࡶࠠࡧࡱࡸࡲࡩࠦࡩ࡯ࠢࡾࢁ࠱ࠦࡵ࡯ࡼ࡬ࡴࡵ࡯࡮ࡨࠤᾠ").format(bstack1lllll111l1l_opy_))
          return self.bstack1lllll1lll11_opy_(bstack1lllll111l1l_opy_, bstack1lllll11ll11_opy_)
      self.logger.info(bstack11111_opy_ (u"ࠧࡊ࡯ࡸࡰ࡯ࡳࡦࡪࡩ࡯ࡩࠣࡴࡪࡸࡣࡺࠢࡥ࡭ࡳࡧࡲࡺࠢࡩࡶࡴࡳࠠࡼࡿࠥᾡ").format(bstack1lllll1ll111_opy_))
      response = bstack1111ll1lll_opy_(bstack11111_opy_ (u"࠭ࡇࡆࡖࠪᾢ"), bstack1lllll1ll111_opy_, {}, {})
      if response.status_code == 200:
        bstack1llllll11l11_opy_ = response.headers.get(bstack11111_opy_ (u"ࠢࡆࡖࡤ࡫ࠧᾣ"), bstack11111_opy_ (u"ࠣࠤᾤ"))
        if bstack1llllll11l11_opy_:
          self.bstack1lllll11ll1l_opy_(bstack1lllll11l11l_opy_, bstack1llllll11l11_opy_)
        with open(bstack1lllll111l1l_opy_, bstack11111_opy_ (u"ࠩࡺࡦࠬᾥ")) as file:
          file.write(response.content)
        self.logger.info(bstack11111_opy_ (u"ࠥࡈࡴࡽ࡮࡭ࡱࡤࡨࡪࡪࠠࡱࡧࡵࡧࡾࠦࡢࡪࡰࡤࡶࡾࠦࡡ࡯ࡦࠣࡷࡦࡼࡥࡥࠢࡤࡸࠥࢁࡽࠣᾦ").format(bstack1lllll111l1l_opy_))
        return self.bstack1lllll1lll11_opy_(bstack1lllll111l1l_opy_, bstack1lllll11ll11_opy_)
      else:
        raise(bstack11111_opy_ (u"ࠦࡋࡧࡩ࡭ࡧࡧࠤࡹࡵࠠࡥࡱࡺࡲࡱࡵࡡࡥࠢࡷ࡬ࡪࠦࡦࡪ࡮ࡨ࠲࡙ࠥࡴࡢࡶࡸࡷࠥࡩ࡯ࡥࡧ࠽ࠤࢀࢃࠢᾧ").format(response.status_code))
    except Exception as e:
      self.logger.error(bstack11111_opy_ (u"࡛ࠧ࡮ࡢࡤ࡯ࡩࠥࡺ࡯ࠡࡦࡲࡻࡳࡲ࡯ࡢࡦࠣࡴࡪࡸࡣࡺࠢࡥ࡭ࡳࡧࡲࡺ࠼ࠣࡿࢂࠨᾨ").format(e))
  def bstack1lllll1l1111_opy_(self, bstack1lllll1ll111_opy_, bstack1lllll11ll11_opy_):
    try:
      retry = 2
      bstack1lllll1ll11l_opy_ = None
      bstack1lllll1l1l1l_opy_ = False
      while retry > 0:
        bstack1lllll1ll11l_opy_ = self.bstack11111111l11_opy_(bstack1lllll1ll111_opy_, bstack1lllll11ll11_opy_)
        bstack1lllll1l1l1l_opy_ = self.bstack1lllll1llll1_opy_(bstack1lllll1ll111_opy_, bstack1lllll11ll11_opy_, bstack1lllll1ll11l_opy_)
        if bstack1lllll1l1l1l_opy_:
          break
        retry -= 1
      return bstack1lllll1ll11l_opy_, bstack1lllll1l1l1l_opy_
    except Exception as e:
      self.logger.error(bstack11111_opy_ (u"ࠨࡕ࡯ࡣࡥࡰࡪࠦࡴࡰࠢࡪࡩࡹࠦࡰࡦࡴࡦࡽࠥࡨࡩ࡯ࡣࡵࡽࠥࡶࡡࡵࡪࠥᾩ").format(e))
    return bstack1lllll1ll11l_opy_, False
  def bstack1lllll1llll1_opy_(self, bstack1lllll1ll111_opy_, bstack1lllll11ll11_opy_, bstack1lllll1ll11l_opy_, bstack1lllll1lll1l_opy_ = 0):
    if bstack1lllll1lll1l_opy_ > 1:
      return False
    if bstack1lllll1ll11l_opy_ == None or os.path.exists(bstack1lllll1ll11l_opy_) == False:
      self.logger.warn(bstack11111_opy_ (u"ࠢࡑࡧࡵࡧࡾࠦࡰࡢࡶ࡫ࠤࡳࡵࡴࠡࡨࡲࡹࡳࡪࠬࠡࡴࡨࡸࡷࡿࡩ࡯ࡩࠣࡨࡴࡽ࡮࡭ࡱࡤࡨࠧᾪ"))
      return False
    bstack1llllll111l1_opy_ = bstack11111_opy_ (u"ࡳࠤࡡ࠲࠯ࡆࡰࡦࡴࡦࡽ࠴ࡩ࡬ࡪࠢ࡟ࡨ࠰ࡢ࠮࡝ࡦ࠮ࡠ࠳ࡢࡤࠬࠤᾫ")
    command = bstack11111_opy_ (u"ࠩࡾࢁࠥ࠳࠭ࡷࡧࡵࡷ࡮ࡵ࡮ࠨᾬ").format(bstack1lllll1ll11l_opy_)
    bstack111111111l1_opy_ = subprocess.check_output(command, shell=True, text=True)
    if re.match(bstack1llllll111l1_opy_, bstack111111111l1_opy_) != None:
      return True
    else:
      self.logger.error(bstack11111_opy_ (u"ࠥࡔࡪࡸࡣࡺࠢࡹࡩࡷࡹࡩࡰࡰࠣࡧ࡭࡫ࡣ࡬ࠢࡩࡥ࡮ࡲࡥࡥࠤᾭ"))
      return False
  def bstack1lllll1lll11_opy_(self, bstack1lllll111l1l_opy_, bstack1lllll11ll11_opy_):
    try:
      working_dir = os.path.dirname(bstack1lllll111l1l_opy_)
      shutil.unpack_archive(bstack1lllll111l1l_opy_, working_dir)
      bstack1lllll1ll11l_opy_ = os.path.join(working_dir, bstack1lllll11ll11_opy_)
      os.chmod(bstack1lllll1ll11l_opy_, 0o755)
      return bstack1lllll1ll11l_opy_
    except Exception as e:
      self.logger.error(bstack11111_opy_ (u"࡚ࠦࡴࡡࡣ࡮ࡨࠤࡹࡵࠠࡶࡰࡽ࡭ࡵࠦࡰࡦࡴࡦࡽࠥࡨࡩ࡯ࡣࡵࡽࠧᾮ"))
  def bstack1lllll1l1l11_opy_(self):
    try:
      bstack1111111111l_opy_ = self.config.get(bstack11111_opy_ (u"ࠬࡶࡥࡳࡥࡼࠫᾯ"))
      bstack1lllll1l1l11_opy_ = bstack1111111111l_opy_ or (bstack1111111111l_opy_ is None and self.bstack11l1ll11l1_opy_)
      if not bstack1lllll1l1l11_opy_ or self.config.get(bstack11111_opy_ (u"࠭ࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࠩᾰ"), None) not in bstack11l1l11111l_opy_:
        return False
      self.bstack11l1l1111_opy_ = True
      return True
    except Exception as e:
      self.logger.error(bstack11111_opy_ (u"ࠢࡖࡰࡤࡦࡱ࡫ࠠࡵࡱࠣࡨࡪࡺࡥࡤࡶࠣࡴࡪࡸࡣࡺ࠮ࠣࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡻࡾࠤᾱ").format(e))
  def bstack1llllll1llll_opy_(self):
    try:
      bstack1llllll1llll_opy_ = self.percy_capture_mode
      return bstack1llllll1llll_opy_
    except Exception as e:
      self.logger.error(bstack11111_opy_ (u"ࠣࡗࡱࡥࡧࡲࡥࠡࡶࡲࠤࡩ࡫ࡴࡦࡥࡷࠤࡵ࡫ࡲࡤࡻࠣࡧࡦࡶࡴࡶࡴࡨࠤࡲࡵࡤࡦ࠮ࠣࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡻࡾࠤᾲ").format(e))
  def init(self, bstack11l1ll11l1_opy_, config, logger):
    self.bstack11l1ll11l1_opy_ = bstack11l1ll11l1_opy_
    self.config = config
    self.logger = logger
    if not self.bstack1lllll1l1l11_opy_():
      return
    self.bstack1llllll11ll1_opy_ = config.get(bstack11111_opy_ (u"ࠩࡳࡩࡷࡩࡹࡐࡲࡷ࡭ࡴࡴࡳࠨᾳ"), {})
    self.percy_capture_mode = config.get(bstack11111_opy_ (u"ࠪࡴࡪࡸࡣࡺࡅࡤࡴࡹࡻࡲࡦࡏࡲࡨࡪ࠭ᾴ"))
    try:
      bstack1lllll1ll111_opy_, bstack1lllll11ll11_opy_ = self.bstack1lllllll11ll_opy_()
      self.bstack1111l1ll111_opy_ = bstack1lllll11ll11_opy_
      bstack1lllll1ll11l_opy_, bstack1lllll1l1l1l_opy_ = self.bstack1lllll1l1111_opy_(bstack1lllll1ll111_opy_, bstack1lllll11ll11_opy_)
      if bstack1lllll1l1l1l_opy_:
        self.binary_path = bstack1lllll1ll11l_opy_
        thread = Thread(target=self.bstack1lllll11llll_opy_)
        thread.start()
      else:
        self.bstack1lllll11l1l1_opy_ = True
        self.logger.error(bstack11111_opy_ (u"ࠦࡎࡴࡶࡢ࡮࡬ࡨࠥࡶࡥࡳࡥࡼࠤࡵࡧࡴࡩࠢࡩࡳࡺࡴࡤࠡ࠯ࠣࡿࢂ࠲ࠠࡖࡰࡤࡦࡱ࡫ࠠࡵࡱࠣࡷࡹࡧࡲࡵࠢࡓࡩࡷࡩࡹࠣ᾵").format(bstack1lllll1ll11l_opy_))
    except Exception as e:
      self.logger.error(bstack11111_opy_ (u"࡛ࠧ࡮ࡢࡤ࡯ࡩࠥࡺ࡯ࠡࡵࡷࡥࡷࡺࠠࡱࡧࡵࡧࡾ࠲ࠠࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣࡿࢂࠨᾶ").format(e))
  def bstack1lllll11l1ll_opy_(self):
    try:
      logfile = os.path.join(self.working_dir, bstack11111_opy_ (u"࠭࡬ࡰࡩࠪᾷ"), bstack11111_opy_ (u"ࠧࡱࡧࡵࡧࡾ࠴࡬ࡰࡩࠪᾸ"))
      os.makedirs(os.path.dirname(logfile)) if not os.path.exists(os.path.dirname(logfile)) else None
      self.logger.debug(bstack11111_opy_ (u"ࠣࡒࡸࡷ࡭࡯࡮ࡨࠢࡳࡩࡷࡩࡹࠡ࡮ࡲ࡫ࡸࠦࡡࡵࠢࡾࢁࠧᾹ").format(logfile))
      self.bstack1lllll1l11l1_opy_ = logfile
    except Exception as e:
      self.logger.error(bstack11111_opy_ (u"ࠤࡘࡲࡦࡨ࡬ࡦࠢࡷࡳࠥࡹࡥࡵࠢࡳࡩࡷࡩࡹࠡ࡮ࡲ࡫ࠥࡶࡡࡵࡪ࠯ࠤࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡼࡿࠥᾺ").format(e))
  @measure(event_name=EVENTS.bstack11l11l1ll1l_opy_, stage=STAGE.bstack111l1l11l_opy_)
  def bstack1lllll11llll_opy_(self):
    bstack1lllllll11l1_opy_ = self.bstack1lllll11lll1_opy_()
    if bstack1lllllll11l1_opy_ == None:
      self.bstack1lllll11l1l1_opy_ = True
      self.logger.error(bstack11111_opy_ (u"ࠥࡔࡪࡸࡣࡺࠢࡷࡳࡰ࡫࡮ࠡࡰࡲࡸࠥ࡬࡯ࡶࡰࡧ࠰ࠥࡌࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡࡵࡷࡥࡷࡺࠠࡱࡧࡵࡧࡾࠨΆ"))
      return False
    bstack1lllllll1l11_opy_ = [bstack11111_opy_ (u"ࠦࡦࡶࡰ࠻ࡧࡻࡩࡨࡀࡳࡵࡣࡵࡸࠧᾼ") if self.bstack11l1ll11l1_opy_ else bstack11111_opy_ (u"ࠬ࡫ࡸࡦࡥ࠽ࡷࡹࡧࡲࡵࠩ᾽")]
    bstack111111lllll_opy_ = self.bstack1llllll111ll_opy_()
    if bstack111111lllll_opy_ != None:
      bstack1lllllll1l11_opy_.append(bstack11111_opy_ (u"ࠨ࠭ࡤࠢࡾࢁࠧι").format(bstack111111lllll_opy_))
    env = os.environ.copy()
    env[bstack11111_opy_ (u"ࠢࡑࡇࡕࡇ࡞ࡥࡔࡐࡍࡈࡒࠧ᾿")] = bstack1lllllll11l1_opy_
    env[bstack11111_opy_ (u"ࠣࡖࡋࡣࡇ࡛ࡉࡍࡆࡢ࡙࡚ࡏࡄࠣ῀")] = os.environ.get(bstack11111_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡎࡕࡃࡡࡘ࡙ࡎࡊࠧ῁"), bstack11111_opy_ (u"ࠪࠫῂ"))
    bstack1llllllll1ll_opy_ = [self.binary_path]
    self.bstack1lllll11l1ll_opy_()
    self.bstack1llllll11lll_opy_ = self.bstack1lllll1l111l_opy_(bstack1llllllll1ll_opy_ + bstack1lllllll1l11_opy_, env)
    self.logger.debug(bstack11111_opy_ (u"ࠦࡘࡺࡡࡳࡶ࡬ࡲ࡬ࠦࡈࡦࡣ࡯ࡸ࡭ࠦࡃࡩࡧࡦ࡯ࠧῃ"))
    bstack1lllll1lll1l_opy_ = 0
    while self.bstack1llllll11lll_opy_.poll() == None:
      bstack1lllllllllll_opy_ = self.bstack1llllll11l1l_opy_()
      if bstack1lllllllllll_opy_:
        self.logger.debug(bstack11111_opy_ (u"ࠧࡎࡥࡢ࡮ࡷ࡬ࠥࡉࡨࡦࡥ࡮ࠤࡸࡻࡣࡤࡧࡶࡷ࡫ࡻ࡬ࠣῄ"))
        self.bstack1lllllllll11_opy_ = True
        return True
      bstack1lllll1lll1l_opy_ += 1
      self.logger.debug(bstack11111_opy_ (u"ࠨࡈࡦࡣ࡯ࡸ࡭ࠦࡃࡩࡧࡦ࡯ࠥࡘࡥࡵࡴࡼࠤ࠲ࠦࡻࡾࠤ῅").format(bstack1lllll1lll1l_opy_))
      time.sleep(2)
    self.logger.error(bstack11111_opy_ (u"ࠢࡇࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡷࡹࡧࡲࡵࠢࡳࡩࡷࡩࡹ࠭ࠢࡋࡩࡦࡲࡴࡩࠢࡆ࡬ࡪࡩ࡫ࠡࡈࡤ࡭ࡱ࡫ࡤࠡࡣࡩࡸࡪࡸࠠࡼࡿࠣࡥࡹࡺࡥ࡮ࡲࡷࡷࠧῆ").format(bstack1lllll1lll1l_opy_))
    self.bstack1lllll11l1l1_opy_ = True
    return False
  def bstack1llllll11l1l_opy_(self, bstack1lllll1lll1l_opy_ = 0):
    if bstack1lllll1lll1l_opy_ > 10:
      return False
    try:
      bstack1lllllll1111_opy_ = os.environ.get(bstack11111_opy_ (u"ࠨࡒࡈࡖࡈ࡟࡟ࡔࡇࡕ࡚ࡊࡘ࡟ࡂࡆࡇࡖࡊ࡙ࡓࠨῇ"), bstack11111_opy_ (u"ࠩ࡫ࡸࡹࡶ࠺࠰࠱࡯ࡳࡨࡧ࡬ࡩࡱࡶࡸ࠿࠻࠳࠴࠺ࠪῈ"))
      bstack1lllll111ll1_opy_ = bstack1lllllll1111_opy_ + bstack11l1l11l1l1_opy_
      response = requests.get(bstack1lllll111ll1_opy_)
      data = response.json()
      self.percy_build_id = data.get(bstack11111_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࠩΈ"), {}).get(bstack11111_opy_ (u"ࠫ࡮ࡪࠧῊ"), None)
      return True
    except:
      self.logger.debug(bstack11111_opy_ (u"ࠧࡋࡲࡳࡱࡵࠤࡴࡩࡣࡶࡴࡵࡩࡩࠦࡷࡩ࡫࡯ࡩࠥࡶࡲࡰࡥࡨࡷࡸ࡯࡮ࡨࠢ࡫ࡩࡦࡲࡴࡩࠢࡦ࡬ࡪࡩ࡫ࠡࡴࡨࡷࡵࡵ࡮ࡴࡧࠥΉ"))
      return False
  def bstack1lllll11lll1_opy_(self):
    bstack1lllll1ll1ll_opy_ = bstack11111_opy_ (u"࠭ࡡࡱࡲࠪῌ") if self.bstack11l1ll11l1_opy_ else bstack11111_opy_ (u"ࠧࡢࡷࡷࡳࡲࡧࡴࡦࠩ῍")
    bstack1llllll1l1l1_opy_ = bstack11111_opy_ (u"ࠣࡷࡱࡨࡪ࡬ࡩ࡯ࡧࡧࠦ῎") if self.config.get(bstack11111_opy_ (u"ࠩࡳࡩࡷࡩࡹࠨ῏")) is None else True
    bstack11ll111l11l_opy_ = bstack11111_opy_ (u"ࠥࡥࡵ࡯࠯ࡢࡲࡳࡣࡵ࡫ࡲࡤࡻ࠲࡫ࡪࡺ࡟ࡱࡴࡲ࡮ࡪࡩࡴࡠࡶࡲ࡯ࡪࡴ࠿࡯ࡣࡰࡩࡂࢁࡽࠧࡶࡼࡴࡪࡃࡻࡾࠨࡳࡩࡷࡩࡹ࠾ࡽࢀࠦῐ").format(self.config[bstack11111_opy_ (u"ࠫࡵࡸ࡯࡫ࡧࡦࡸࡓࡧ࡭ࡦࠩῑ")], bstack1lllll1ll1ll_opy_, bstack1llllll1l1l1_opy_)
    if self.percy_capture_mode:
      bstack11ll111l11l_opy_ += bstack11111_opy_ (u"ࠧࠬࡰࡦࡴࡦࡽࡤࡩࡡࡱࡶࡸࡶࡪࡥ࡭ࡰࡦࡨࡁࢀࢃࠢῒ").format(self.percy_capture_mode)
    uri = bstack1ll11llll_opy_(bstack11ll111l11l_opy_)
    try:
      response = bstack1111ll1lll_opy_(bstack11111_opy_ (u"࠭ࡇࡆࡖࠪΐ"), uri, {}, {bstack11111_opy_ (u"ࠧࡢࡷࡷ࡬ࠬ῔"): (self.config[bstack11111_opy_ (u"ࠨࡷࡶࡩࡷࡔࡡ࡮ࡧࠪ῕")], self.config[bstack11111_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴࡍࡨࡽࠬῖ")])})
      if response.status_code == 200:
        data = response.json()
        self.bstack11l1l1111_opy_ = data.get(bstack11111_opy_ (u"ࠪࡷࡺࡩࡣࡦࡵࡶࠫῗ"))
        self.percy_capture_mode = data.get(bstack11111_opy_ (u"ࠫࡵ࡫ࡲࡤࡻࡢࡧࡦࡶࡴࡶࡴࡨࡣࡲࡵࡤࡦࠩῘ"))
        os.environ[bstack11111_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡕࡋࡒࡄ࡛ࠪῙ")] = str(self.bstack11l1l1111_opy_)
        os.environ[bstack11111_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡖࡅࡓࡅ࡜ࡣࡈࡇࡐࡕࡗࡕࡉࡤࡓࡏࡅࡇࠪῚ")] = str(self.percy_capture_mode)
        if bstack1llllll1l1l1_opy_ == bstack11111_opy_ (u"ࠢࡶࡰࡧࡩ࡫࡯࡮ࡦࡦࠥΊ") and str(self.bstack11l1l1111_opy_).lower() == bstack11111_opy_ (u"ࠣࡶࡵࡹࡪࠨ῜"):
          self.bstack1l11ll11l1_opy_ = True
        if bstack11111_opy_ (u"ࠤࡷࡳࡰ࡫࡮ࠣ῝") in data:
          return data[bstack11111_opy_ (u"ࠥࡸࡴࡱࡥ࡯ࠤ῞")]
        else:
          raise bstack11111_opy_ (u"࡙ࠫࡵ࡫ࡦࡰࠣࡒࡴࡺࠠࡇࡱࡸࡲࡩࠦ࠭ࠡࡽࢀࠫ῟").format(data)
      else:
        raise bstack11111_opy_ (u"ࠧࡌࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡࡨࡨࡸࡨ࡮ࠠࡱࡧࡵࡧࡾࠦࡴࡰ࡭ࡨࡲ࠱ࠦࡒࡦࡵࡳࡳࡳࡹࡥࠡࡵࡷࡥࡹࡻࡳࠡ࠯ࠣࡿࢂ࠲ࠠࡓࡧࡶࡴࡴࡴࡳࡦࠢࡅࡳࡩࡿࠠ࠮ࠢࡾࢁࠧῠ").format(response.status_code, response.json())
    except Exception as e:
      self.logger.error(bstack11111_opy_ (u"ࠨࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥࡩࡲࡦࡣࡷ࡭ࡳ࡭ࠠࡱࡧࡵࡧࡾࠦࡰࡳࡱ࡭ࡩࡨࡺࠢῡ").format(e))
  def bstack1llllll111ll_opy_(self):
    bstack1lllll111l11_opy_ = os.path.join(tempfile.gettempdir(), bstack11111_opy_ (u"ࠢࡱࡧࡵࡧࡾࡉ࡯࡯ࡨ࡬࡫࠳ࡰࡳࡰࡰࠥῢ"))
    try:
      if bstack11111_opy_ (u"ࠨࡸࡨࡶࡸ࡯࡯࡯ࠩΰ") not in self.bstack1llllll11ll1_opy_:
        self.bstack1llllll11ll1_opy_[bstack11111_opy_ (u"ࠩࡹࡩࡷࡹࡩࡰࡰࠪῤ")] = 2
      with open(bstack1lllll111l11_opy_, bstack11111_opy_ (u"ࠪࡻࠬῥ")) as fp:
        json.dump(self.bstack1llllll11ll1_opy_, fp)
      return bstack1lllll111l11_opy_
    except Exception as e:
      self.logger.error(bstack11111_opy_ (u"࡚ࠦࡴࡡࡣ࡮ࡨࠤࡹࡵࠠࡤࡴࡨࡥࡹ࡫ࠠࡱࡧࡵࡧࡾࠦࡣࡰࡰࡩ࠰ࠥࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡࡽࢀࠦῦ").format(e))
  def bstack1lllll1l111l_opy_(self, cmd, env = os.environ.copy()):
    try:
      if self.bstack1llllll11111_opy_ == bstack11111_opy_ (u"ࠬࡽࡩ࡯ࠩῧ"):
        bstack1llllll1l11l_opy_ = [bstack11111_opy_ (u"࠭ࡣ࡮ࡦ࠱ࡩࡽ࡫ࠧῨ"), bstack11111_opy_ (u"ࠧ࠰ࡥࠪῩ")]
        cmd = bstack1llllll1l11l_opy_ + cmd
      cmd = bstack11111_opy_ (u"ࠨࠢࠪῪ").join(cmd)
      self.logger.debug(bstack11111_opy_ (u"ࠤࡕࡹࡳࡴࡩ࡯ࡩࠣࡿࢂࠨΎ").format(cmd))
      with open(self.bstack1lllll1l11l1_opy_, bstack11111_opy_ (u"ࠥࡥࠧῬ")) as bstack1lllllll111l_opy_:
        process = subprocess.Popen(cmd, shell=True, stdout=bstack1lllllll111l_opy_, text=True, stderr=bstack1lllllll111l_opy_, env=env, universal_newlines=True)
      return process
    except Exception as e:
      self.bstack1lllll11l1l1_opy_ = True
      self.logger.error(bstack11111_opy_ (u"ࠦࡋࡧࡩ࡭ࡧࡧࠤࡹࡵࠠࡴࡶࡤࡶࡹࠦࡰࡦࡴࡦࡽࠥࡽࡩࡵࡪࠣࡧࡲࡪࠠ࠮ࠢࡾࢁ࠱ࠦࡅࡹࡥࡨࡴࡹ࡯࡯࡯࠼ࠣࡿࢂࠨ῭").format(cmd, e))
  def shutdown(self):
    try:
      if self.bstack1lllllllll11_opy_:
        self.logger.info(bstack11111_opy_ (u"࡙ࠧࡴࡰࡲࡳ࡭ࡳ࡭ࠠࡑࡧࡵࡧࡾࠨ΅"))
        cmd = [self.binary_path, bstack11111_opy_ (u"ࠨࡥࡹࡧࡦ࠾ࡸࡺ࡯ࡱࠤ`")]
        self.bstack1lllll1l111l_opy_(cmd)
        self.bstack1lllllllll11_opy_ = False
    except Exception as e:
      self.logger.error(bstack11111_opy_ (u"ࠢࡇࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡷࡹࡵࡰࠡࡵࡨࡷࡸ࡯࡯࡯ࠢࡺ࡭ࡹ࡮ࠠࡤࡱࡰࡱࡦࡴࡤࠡ࠯ࠣࡿࢂ࠲ࠠࡆࡺࡦࡩࡵࡺࡩࡰࡰ࠽ࠤࢀࢃࠢ῰").format(cmd, e))
  def bstack1111lll111_opy_(self):
    if not self.bstack11l1l1111_opy_:
      return
    try:
      bstack1lllll1l11ll_opy_ = 0
      while not self.bstack1lllllllll11_opy_ and bstack1lllll1l11ll_opy_ < self.bstack1lllllll1l1l_opy_:
        if self.bstack1lllll11l1l1_opy_:
          self.logger.info(bstack11111_opy_ (u"ࠣࡒࡨࡶࡨࡿࠠࡴࡧࡷࡹࡵࠦࡦࡢ࡫࡯ࡩࡩࠨ῱"))
          return
        time.sleep(1)
        bstack1lllll1l11ll_opy_ += 1
      os.environ[bstack11111_opy_ (u"ࠩࡓࡉࡗࡉ࡙ࡠࡄࡈࡗ࡙ࡥࡐࡍࡃࡗࡊࡔࡘࡍࠨῲ")] = str(self.bstack1lllll1l1lll_opy_())
      self.logger.info(bstack11111_opy_ (u"ࠥࡔࡪࡸࡣࡺࠢࡶࡩࡹࡻࡰࠡࡥࡲࡱࡵࡲࡥࡵࡧࡧࠦῳ"))
    except Exception as e:
      self.logger.error(bstack11111_opy_ (u"࡚ࠦࡴࡡࡣ࡮ࡨࠤࡹࡵࠠࡴࡧࡷࡹࡵࠦࡰࡦࡴࡦࡽ࠱ࠦࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢࡾࢁࠧῴ").format(e))
  def bstack1lllll1l1lll_opy_(self):
    if self.bstack11l1ll11l1_opy_:
      return
    try:
      bstack1llllll1ll11_opy_ = [platform[bstack11111_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡔࡡ࡮ࡧࠪ῵")].lower() for platform in self.config.get(bstack11111_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩῶ"), [])]
      bstack1lllllll1lll_opy_ = sys.maxsize
      bstack1lllll1l1ll1_opy_ = bstack11111_opy_ (u"ࠧࠨῷ")
      for browser in bstack1llllll1ll11_opy_:
        if browser in self.bstack11111111111_opy_:
          bstack1lllll1lllll_opy_ = self.bstack11111111111_opy_[browser]
        if bstack1lllll1lllll_opy_ < bstack1lllllll1lll_opy_:
          bstack1lllllll1lll_opy_ = bstack1lllll1lllll_opy_
          bstack1lllll1l1ll1_opy_ = browser
      return bstack1lllll1l1ll1_opy_
    except Exception as e:
      self.logger.error(bstack11111_opy_ (u"ࠣࡗࡱࡥࡧࡲࡥࠡࡶࡲࠤ࡫࡯࡮ࡥࠢࡥࡩࡸࡺࠠࡱ࡮ࡤࡸ࡫ࡵࡲ࡮࠮ࠣࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡻࡾࠤῸ").format(e))
  @classmethod
  def bstack11l1l1l1l1_opy_(self):
    return os.getenv(bstack11111_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡒࡈࡖࡈ࡟ࠧΌ"), bstack11111_opy_ (u"ࠪࡊࡦࡲࡳࡦࠩῺ")).lower()
  @classmethod
  def bstack1l1l1l1l1_opy_(self):
    return os.getenv(bstack11111_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡔࡊࡘࡃ࡚ࡡࡆࡅࡕ࡚ࡕࡓࡇࡢࡑࡔࡊࡅࠨΏ"), bstack11111_opy_ (u"ࠬ࠭ῼ"))
  @classmethod
  def bstack11llll1l111_opy_(cls, value):
    cls.bstack1l11ll11l1_opy_ = value
  @classmethod
  def bstack11111111l1l_opy_(cls):
    return cls.bstack1l11ll11l1_opy_
  @classmethod
  def bstack11llll11ll1_opy_(cls, value):
    cls.percy_build_id = value
  @classmethod
  def bstack1llllll1lll1_opy_(cls):
    return cls.percy_build_id