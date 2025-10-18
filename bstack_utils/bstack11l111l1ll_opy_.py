# coding: UTF-8
import sys
bstack1ll1111_opy_ = sys.version_info [0] == 2
bstack1ll_opy_ = 2048
bstack1ll1l1_opy_ = 7
def bstack11l111_opy_ (bstack1ll1_opy_):
    global bstack11l1l_opy_
    bstack11l1l1_opy_ = ord (bstack1ll1_opy_ [-1])
    bstack111ll_opy_ = bstack1ll1_opy_ [:-1]
    bstack11111ll_opy_ = bstack11l1l1_opy_ % len (bstack111ll_opy_)
    bstack1l1lll_opy_ = bstack111ll_opy_ [:bstack11111ll_opy_] + bstack111ll_opy_ [bstack11111ll_opy_:]
    if bstack1ll1111_opy_:
        bstack1lll1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack1ll_opy_ - (bstack1l111_opy_ + bstack11l1l1_opy_) % bstack1ll1l1_opy_) for bstack1l111_opy_, char in enumerate (bstack1l1lll_opy_)])
    else:
        bstack1lll1ll_opy_ = str () .join ([chr (ord (char) - bstack1ll_opy_ - (bstack1l111_opy_ + bstack11l1l1_opy_) % bstack1ll1l1_opy_) for bstack1l111_opy_, char in enumerate (bstack1l1lll_opy_)])
    return eval (bstack1lll1ll_opy_)
import sys
import logging
import tarfile
import io
import os
import time
import requests
import re
from requests_toolbelt.multipart.encoder import MultipartEncoder
from bstack_utils.constants import bstack11l11ll1ll1_opy_, bstack11l11l1ll11_opy_, bstack11l11ll11ll_opy_
import tempfile
import json
bstack11111l1l111_opy_ = os.getenv(bstack11l111_opy_ (u"ࠦࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡐࡔࡍ࡟ࡇࡋࡏࡉࠧệ"), None) or os.path.join(tempfile.gettempdir(), bstack11l111_opy_ (u"ࠧࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡩ࡫ࡢࡶࡩ࠱ࡰࡴ࡭ࠢỈ"))
bstack11111l1lll1_opy_ = os.path.join(bstack11l111_opy_ (u"ࠨ࡬ࡰࡩࠥỉ"), bstack11l111_opy_ (u"ࠧࡴࡦ࡮࠱ࡨࡲࡩ࠮ࡦࡨࡦࡺ࡭࠮࡭ࡱࡪࠫỊ"))
logging.Formatter.converter = time.gmtime
def get_logger(name=__name__, level=None):
  logger = logging.getLogger(name)
  if level:
    logging.basicConfig(
      level=level,
      format=bstack11l111_opy_ (u"ࠨࠧࠫࡥࡸࡩࡴࡪ࡯ࡨ࠭ࡸ࡛ࠦࠦࠪࡱࡥࡲ࡫ࠩࡴ࡟࡞ࠩ࠭ࡲࡥࡷࡧ࡯ࡲࡦࡳࡥࠪࡵࡠࠤ࠲ࠦࠥࠩ࡯ࡨࡷࡸࡧࡧࡦࠫࡶࠫị"),
      datefmt=bstack11l111_opy_ (u"ࠩࠨ࡝࠲ࠫ࡭࠮ࠧࡧࡘࠪࡎ࠺ࠦࡏ࠽ࠩࡘࡠࠧỌ"),
      stream=sys.stdout
    )
  return logger
def bstack1l1l111ll11_opy_():
  bstack11111ll1ll1_opy_ = os.environ.get(bstack11l111_opy_ (u"ࠥࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡅࡍࡓࡇࡒ࡚ࡡࡇࡉࡇ࡛ࡇࠣọ"), bstack11l111_opy_ (u"ࠦ࡫ࡧ࡬ࡴࡧࠥỎ"))
  return logging.DEBUG if bstack11111ll1ll1_opy_.lower() == bstack11l111_opy_ (u"ࠧࡺࡲࡶࡧࠥỏ") else logging.INFO
def bstack1ll1l11111l_opy_():
  global bstack11111l1l111_opy_
  if os.path.exists(bstack11111l1l111_opy_):
    os.remove(bstack11111l1l111_opy_)
  if os.path.exists(bstack11111l1lll1_opy_):
    os.remove(bstack11111l1lll1_opy_)
def bstack11l1ll1lll_opy_():
  for handler in logging.getLogger().handlers:
    logging.getLogger().removeHandler(handler)
def configure_logger(config, log_level):
  bstack11111l1111l_opy_ = log_level
  if bstack11l111_opy_ (u"࠭࡬ࡰࡩࡏࡩࡻ࡫࡬ࠨỐ") in config and config[bstack11l111_opy_ (u"ࠧ࡭ࡱࡪࡐࡪࡼࡥ࡭ࠩố")] in bstack11l11l1ll11_opy_:
    bstack11111l1111l_opy_ = bstack11l11l1ll11_opy_[config[bstack11l111_opy_ (u"ࠨ࡮ࡲ࡫ࡑ࡫ࡶࡦ࡮ࠪỒ")]]
  if config.get(bstack11l111_opy_ (u"ࠩࡧ࡭ࡸࡧࡢ࡭ࡧࡄࡹࡹࡵࡃࡢࡲࡷࡹࡷ࡫ࡌࡰࡩࡶࠫồ"), False):
    logging.getLogger().setLevel(bstack11111l1111l_opy_)
    return bstack11111l1111l_opy_
  global bstack11111l1l111_opy_
  bstack11l1ll1lll_opy_()
  bstack11111ll111l_opy_ = logging.Formatter(
    fmt=bstack11l111_opy_ (u"ࠪࠩ࠭ࡧࡳࡤࡶ࡬ࡱࡪ࠯ࡳࠡ࡝ࠨࠬࡳࡧ࡭ࡦࠫࡶࡡࡠࠫࠨ࡭ࡧࡹࡩࡱࡴࡡ࡮ࡧࠬࡷࡢࠦ࠭ࠡࠧࠫࡱࡪࡹࡳࡢࡩࡨ࠭ࡸ࠭Ổ"),
    datefmt=bstack11l111_opy_ (u"ࠫࠪ࡟࠭ࠦ࡯࠰ࠩࡩ࡚ࠥࡉ࠼ࠨࡑ࠿ࠫࡓ࡛ࠩổ"),
  )
  bstack11111ll1111_opy_ = logging.StreamHandler(sys.stdout)
  file_handler = logging.FileHandler(bstack11111l1l111_opy_)
  file_handler.setFormatter(bstack11111ll111l_opy_)
  bstack11111ll1111_opy_.setFormatter(bstack11111ll111l_opy_)
  file_handler.setLevel(logging.DEBUG)
  bstack11111ll1111_opy_.setLevel(log_level)
  file_handler.addFilter(lambda r: r.name != bstack11l111_opy_ (u"ࠬࡹࡥ࡭ࡧࡱ࡭ࡺࡳ࠮ࡸࡧࡥࡨࡷ࡯ࡶࡦࡴ࠱ࡶࡪࡳ࡯ࡵࡧ࠱ࡶࡪࡳ࡯ࡵࡧࡢࡧࡴࡴ࡮ࡦࡥࡷ࡭ࡴࡴࠧỖ"))
  logging.getLogger().setLevel(logging.DEBUG)
  bstack11111ll1111_opy_.setLevel(bstack11111l1111l_opy_)
  logging.getLogger().addHandler(bstack11111ll1111_opy_)
  logging.getLogger().addHandler(file_handler)
  return bstack11111l1111l_opy_
def bstack11111lll111_opy_(config):
  try:
    bstack11111l11l11_opy_ = set(bstack11l11ll11ll_opy_)
    bstack11111l1l1ll_opy_ = bstack11l111_opy_ (u"࠭ࠧỗ")
    with open(bstack11l111_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡹ࡮࡮ࠪỘ")) as bstack11111l11l1l_opy_:
      bstack11111ll11l1_opy_ = bstack11111l11l1l_opy_.read()
      bstack11111l1l1ll_opy_ = re.sub(bstack11l111_opy_ (u"ࡳࠩࡡࠬࡡࡹࠫࠪࡁࠦ࠲࠯ࠪ࡜࡯ࠩộ"), bstack11l111_opy_ (u"ࠩࠪỚ"), bstack11111ll11l1_opy_, flags=re.M)
      bstack11111l1l1ll_opy_ = re.sub(
        bstack11l111_opy_ (u"ࡵࠫࡣ࠮࡜ࡴ࠭ࠬࡃ࠭࠭ớ") + bstack11l111_opy_ (u"ࠫࢁ࠭Ờ").join(bstack11111l11l11_opy_) + bstack11l111_opy_ (u"ࠬ࠯࠮ࠫࠦࠪờ"),
        bstack11l111_opy_ (u"ࡸࠧ࡝࠴࠽ࠤࡠࡘࡅࡅࡃࡆࡘࡊࡊ࡝ࠨỞ"),
        bstack11111l1l1ll_opy_, flags=re.M | re.I
      )
    def bstack11111l11lll_opy_(dic):
      bstack11111l1ll11_opy_ = {}
      for key, value in dic.items():
        if key in bstack11111l11l11_opy_:
          bstack11111l1ll11_opy_[key] = bstack11l111_opy_ (u"ࠧ࡜ࡔࡈࡈࡆࡉࡔࡆࡆࡠࠫở")
        else:
          if isinstance(value, dict):
            bstack11111l1ll11_opy_[key] = bstack11111l11lll_opy_(value)
          else:
            bstack11111l1ll11_opy_[key] = value
      return bstack11111l1ll11_opy_
    bstack11111l1ll11_opy_ = bstack11111l11lll_opy_(config)
    return {
      bstack11l111_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡺ࡯࡯ࠫỠ"): bstack11111l1l1ll_opy_,
      bstack11l111_opy_ (u"ࠩࡩ࡭ࡳࡧ࡬ࡤࡱࡱࡪ࡮࡭࠮࡫ࡵࡲࡲࠬỡ"): json.dumps(bstack11111l1ll11_opy_)
    }
  except Exception as e:
    return {}
def bstack11111l111l1_opy_(inipath, rootpath):
  log_dir = os.path.join(os.getcwd(), bstack11l111_opy_ (u"ࠪࡰࡴ࡭ࠧỢ"))
  if not os.path.exists(log_dir):
    os.makedirs(log_dir)
  bstack11111ll1l11_opy_ = os.path.join(log_dir, bstack11l111_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࡣࡨࡵ࡮ࡧ࡫ࡪࡷࠬợ"))
  if not os.path.exists(bstack11111ll1l11_opy_):
    bstack11111l11ll1_opy_ = {
      bstack11l111_opy_ (u"ࠧ࡯࡮ࡪࡲࡤࡸ࡭ࠨỤ"): str(inipath),
      bstack11l111_opy_ (u"ࠨࡲࡰࡱࡷࡴࡦࡺࡨࠣụ"): str(rootpath)
    }
    with open(os.path.join(log_dir, bstack11l111_opy_ (u"ࠧࡱࡻࡷࡩࡸࡺ࡟ࡤࡱࡱࡪ࡮࡭ࡳ࠯࡬ࡶࡳࡳ࠭Ủ")), bstack11l111_opy_ (u"ࠨࡹࠪủ")) as bstack11111ll1l1l_opy_:
      bstack11111ll1l1l_opy_.write(json.dumps(bstack11111l11ll1_opy_))
def bstack11111l111ll_opy_():
  try:
    bstack11111ll1l11_opy_ = os.path.join(os.getcwd(), bstack11l111_opy_ (u"ࠩ࡯ࡳ࡬࠭Ứ"), bstack11l111_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶࡢࡧࡴࡴࡦࡪࡩࡶ࠲࡯ࡹ࡯࡯ࠩứ"))
    if os.path.exists(bstack11111ll1l11_opy_):
      with open(bstack11111ll1l11_opy_, bstack11l111_opy_ (u"ࠫࡷ࠭Ừ")) as bstack11111ll1l1l_opy_:
        bstack11111ll1lll_opy_ = json.load(bstack11111ll1l1l_opy_)
      return bstack11111ll1lll_opy_.get(bstack11l111_opy_ (u"ࠬ࡯࡮ࡪࡲࡤࡸ࡭࠭ừ"), bstack11l111_opy_ (u"࠭ࠧỬ")), bstack11111ll1lll_opy_.get(bstack11l111_opy_ (u"ࠧࡳࡱࡲࡸࡵࡧࡴࡩࠩử"), bstack11l111_opy_ (u"ࠨࠩỮ"))
  except:
    pass
  return None, None
def bstack11111ll11ll_opy_():
  try:
    bstack11111ll1l11_opy_ = os.path.join(os.getcwd(), bstack11l111_opy_ (u"ࠩ࡯ࡳ࡬࠭ữ"), bstack11l111_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶࡢࡧࡴࡴࡦࡪࡩࡶ࠲࡯ࡹ࡯࡯ࠩỰ"))
    if os.path.exists(bstack11111ll1l11_opy_):
      os.remove(bstack11111ll1l11_opy_)
  except:
    pass
def bstack1ll1l111_opy_(config):
  try:
    from bstack_utils.helper import bstack11111l11_opy_, bstack111111ll11_opy_
    from browserstack_sdk.sdk_cli.cli import cli
    global bstack11111l1l111_opy_
    if config.get(bstack11l111_opy_ (u"ࠫࡩ࡯ࡳࡢࡤ࡯ࡩࡆࡻࡴࡰࡅࡤࡴࡹࡻࡲࡦࡎࡲ࡫ࡸ࠭ự"), False):
      return
    uuid = os.getenv(bstack11l111_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡊࡘࡆࡤ࡛ࡕࡊࡆࠪỲ")) if os.getenv(bstack11l111_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡕࡖࡋࡇࠫỳ")) else bstack11111l11_opy_.get_property(bstack11l111_opy_ (u"ࠢࡴࡦ࡮ࡖࡺࡴࡉࡥࠤỴ"))
    if not uuid or uuid == bstack11l111_opy_ (u"ࠨࡰࡸࡰࡱ࠭ỵ"):
      return
    bstack11111l1ll1l_opy_ = [bstack11l111_opy_ (u"ࠩࡵࡩࡶࡻࡩࡳࡧࡰࡩࡳࡺࡳ࠯ࡶࡻࡸࠬỶ"), bstack11l111_opy_ (u"ࠪࡔ࡮ࡶࡦࡪ࡮ࡨࠫỷ"), bstack11l111_opy_ (u"ࠫࡵࡿࡰࡳࡱ࡭ࡩࡨࡺ࠮ࡵࡱࡰࡰࠬỸ"), bstack11111l1l111_opy_, bstack11111l1lll1_opy_]
    bstack11111l1l11l_opy_, root_path = bstack11111l111ll_opy_()
    if bstack11111l1l11l_opy_ != None:
      bstack11111l1ll1l_opy_.append(bstack11111l1l11l_opy_)
    if root_path != None:
      bstack11111l1ll1l_opy_.append(os.path.join(root_path, bstack11l111_opy_ (u"ࠬࡩ࡯࡯ࡨࡷࡩࡸࡺ࠮ࡱࡻࠪỹ")))
    bstack11l1ll1lll_opy_()
    logging.shutdown()
    output_file = os.path.join(tempfile.gettempdir(), bstack11l111_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰ࠳࡬ࡰࡩࡶ࠱ࠬỺ") + uuid + bstack11l111_opy_ (u"ࠧ࠯ࡶࡤࡶ࠳࡭ࡺࠨỻ"))
    with tarfile.open(output_file, bstack11l111_opy_ (u"ࠣࡹ࠽࡫ࡿࠨỼ")) as archive:
      for file in filter(lambda f: os.path.exists(f), bstack11111l1ll1l_opy_):
        try:
          archive.add(file,  arcname=os.path.basename(file))
        except:
          pass
      for name, data in bstack11111lll111_opy_(config).items():
        tarinfo = tarfile.TarInfo(name)
        bstack11111l1llll_opy_ = data.encode()
        tarinfo.size = len(bstack11111l1llll_opy_)
        archive.addfile(tarinfo, io.BytesIO(bstack11111l1llll_opy_))
    multipart_data = MultipartEncoder(
      fields= {
        bstack11l111_opy_ (u"ࠩࡧࡥࡹࡧࠧỽ"): (os.path.basename(output_file), open(os.path.abspath(output_file), bstack11l111_opy_ (u"ࠪࡶࡧ࠭Ỿ")), bstack11l111_opy_ (u"ࠫࡦࡶࡰ࡭࡫ࡦࡥࡹ࡯࡯࡯࠱ࡻ࠱࡬ࢀࡩࡱࠩỿ")),
        bstack11l111_opy_ (u"ࠬࡩ࡬ࡪࡧࡱࡸࡇࡻࡩ࡭ࡦࡘࡹ࡮ࡪࠧἀ"): uuid
      }
    )
    bstack11111l1l1l1_opy_ = bstack111111ll11_opy_(cli.config, [bstack11l111_opy_ (u"ࠨࡡࡱ࡫ࡶࠦἁ"), bstack11l111_opy_ (u"ࠢࡰࡤࡶࡩࡷࡼࡡࡣ࡫࡯࡭ࡹࡿࠢἂ"), bstack11l111_opy_ (u"ࠣࡷࡳࡰࡴࡧࡤࠣἃ")], bstack11l11ll1ll1_opy_)
    response = requests.post(
      bstack11l111_opy_ (u"ࠤࡾࢁ࠴ࡩ࡬ࡪࡧࡱࡸ࠲ࡲ࡯ࡨࡵ࠲ࡹࡵࡲ࡯ࡢࡦࠥἄ").format(bstack11111l1l1l1_opy_),
      data=multipart_data,
      headers={bstack11l111_opy_ (u"ࠪࡇࡴࡴࡴࡦࡰࡷ࠱࡙ࡿࡰࡦࠩἅ"): multipart_data.content_type},
      auth=(config[bstack11l111_opy_ (u"ࠫࡺࡹࡥࡳࡐࡤࡱࡪ࠭ἆ")], config[bstack11l111_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷࡐ࡫ࡹࠨἇ")])
    )
    os.remove(output_file)
    if response.status_code != 200:
      get_logger().debug(bstack11l111_opy_ (u"࠭ࡅࡳࡴࡲࡶࠥࡻࡰ࡭ࡱࡤࡨࠥࡲ࡯ࡨࡵ࠽ࠤࠬἈ") + response.status_code)
  except Exception as e:
    get_logger().debug(bstack11l111_opy_ (u"ࠧࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣ࡭ࡳࠦࡳࡦࡰࡧ࡭ࡳ࡭ࠠ࡭ࡱࡪࡷ࠿࠭Ἁ") + str(e))
  finally:
    try:
      bstack1ll1l11111l_opy_()
      bstack11111ll11ll_opy_()
    except:
      pass